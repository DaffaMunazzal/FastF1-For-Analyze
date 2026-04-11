from flask import Flask, jsonify
from flask_cors import CORS  # <--- INI TAMBAHAN BARU
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
CORS(app) # <--- INI TAMBAHAN BARU: Mengizinkan akses dari Live Server

# Koneksi ke MariaDB
engine = create_engine('mysql+pymysql://root:@localhost/f1_analysis')

# Membuat Endpoint API untuk data pembalap
@app.route('/api/drivers', methods=['GET'])
def get_drivers():
    try:
        # Menarik data dari MariaDB menggunakan Pandas
        query = "SELECT * FROM drivers"
        df = pd.read_sql(query, con=engine)
        
        # Mengubah data tabel menjadi format JSON agar bisa dibaca oleh HTML/JavaScript
        data = df.to_dict(orient='records')
        
        return jsonify({
            "status": "success",
            "total_drivers": len(data),
            "data": data
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

#Mengirim data waktu lap ke frontend untuk ditampilkan di grafik
@app.route('/api/laptimes', methods=['GET'])
def get_laptimes():
    try:
        # Query SQL dengan JOIN untuk menggabungkan waktu lap dan warna tim pembalap
        query = """
        SELECT l.driver_code, l.lap_number, l.lap_time, d.team_color
        FROM lap_times l
        JOIN drivers d ON l.driver_code = d.driver_code
        WHERE l.race_id = 202401 -- Fokus ke ID Balapan GP Bahrain
        ORDER BY l.lap_number
        """
        df = pd.read_sql(query, con=engine)

        # Menerjemahkan waktu "1:35.123" menjadi detik murni (95.123) agar bisa digambar grafik
        def time_to_seconds(time_str):
            if pd.isna(time_str) or time_str == 'None': return None
            parts = str(time_str).split(':')
            if len(parts) == 2:
                return float(parts[0]) * 60 + float(parts[1])
            return None
            
        df['lap_time_seconds'] = df['lap_time'].apply(time_to_seconds)

        # Menyusun data sesuai format yang diminta oleh Chart.js
        chart_data = []
        # Kita filter 3 pembalap top saja agar grafiknya tidak terlalu ruwet saat pertama dibuka
        top_drivers = ['VER', 'PER', 'SAI'] 
        
        for driver in top_drivers:
            driver_data = df[df['driver_code'] == driver]
            if not driver_data.empty:
                chart_data.append({
                    "label": driver,
                    "data": driver_data['lap_time_seconds'].tolist(),
                    "borderColor": f"#{driver_data['team_color'].iloc[0]}",
                    "fill": False,
                    "tension": 0.3 # Membuat garis agak melengkung mulus
                })

        return jsonify({
            "status": "success", 
            "laps": list(range(1, 58)), # Label sumbu X (Lap 1-57)
            "datasets": chart_data
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Menjalankan server
if __name__ == '__main__':
    # debug=True membuat server otomatis restart jika ada perubahan kode
    app.run(debug=True, port=5000)