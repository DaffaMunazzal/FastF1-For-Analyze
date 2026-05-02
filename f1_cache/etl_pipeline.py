import fastf1
import pandas as pd
from sqlalchemy import create_engine

# 1. SETUP CACHE & KONEKSI DATABASE
# Mengaktifkan cache agar penarikan data selanjutnya jauh lebih cepat
fastf1.Cache.enable_cache('f1_cache') 

# Koneksi ke MariaDB/MySQL (Sesuaikan username/password jika perlu)
# Format: mysql+pymysql://user:password@localhost/nama_db
engine = create_engine('mysql+pymysql://root:@localhost/f1_analysis')

def load_drivers_data(year, gp):
    print(f"Memulai proses ETL untuk GP {gp} {year}...")
    
    # 2. EXTRACT: Menarik data balapan (R = Race)
    session = fastf1.get_session(year, gp, 'R')
    session.load(telemetry=False, weather=False) # Matikan telemetri dulu agar cepat
    
    # 3. TRANSFORM: Membersihkan dan menyesuaikan data dengan tabel MySQL kita
    results = session.results
    
    # Mengambil kolom yang kita butuhkan saja
    drivers_df = results[['Abbreviation', 'DriverNumber', 'TeamName', 'TeamColor']].copy()
    
    # Mengganti nama kolom Pandas agar persis dengan nama kolom di tabel MariaDB
    drivers_df.rename(columns={
        'Abbreviation': 'driver_code',
        'DriverNumber': 'driver_number',
        'TeamName': 'team_name',
        'TeamColor': 'team_color'
    }, inplace=True)
    
    # Pastikan tidak ada duplikat pembalap
    drivers_df = drivers_df.drop_duplicates(subset=['driver_code'])
    
    print("Data berhasil di-Transform. Bersiap memasukkan ke database...")
    
    # 4. LOAD: Memasukkan data ke tabel 'drivers' di MySQL
    try:
        # if_exists='append' berarti kita menambahkan data ke tabel yang sudah ada
        drivers_df.to_sql('drivers', con=engine, if_exists='append', index=False)
        print("✅ SUKSES! Data pembalap berhasil disimpan ke database.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan ke database: {e}")

# Eksekusi fungsi untuk GP Bahrain 2024
if __name__ == '__main__':
    load_drivers_data(2024, 'Bahrain')