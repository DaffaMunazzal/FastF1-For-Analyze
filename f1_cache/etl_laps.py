import fastf1
import pandas as pd
from sqlalchemy import create_engine

# Aktifkan cache agar tidak perlu download ulang dari awal
fastf1.Cache.enable_cache('f1_cache') 

# Koneksi ke MariaDB
engine = create_engine('mysql+pymysql://root:@localhost/f1_analysis')

def load_race_and_laps(year, gp):
    print(f"Menarik data balapan dan lap time untuk {gp} {year}...")
    session = fastf1.get_session(year, gp, 'R')
    session.load(telemetry=False, weather=False)

    # ==========================================
    # 1. EXTRACT & LOAD: TABEL 'races' (Parent)
    # ==========================================
    event = session.event
    # Kita buat ID Unik. Contoh: Tahun 2024 Seri ke-1 -> 202401
    race_id = int(f"{year}{event['RoundNumber']:02d}") 
    
    race_data = pd.DataFrame({
        'race_id': [race_id],
        'year': [year],
        'gp_name': [event['EventName']],
        'round': [event['RoundNumber']]
    })
    
    try:
        race_data.to_sql('races', con=engine, if_exists='append', index=False)
        print("✅ Data Balapan (races) berhasil ditambahkan!")
    except Exception as e:
        print("ℹ️ Info: Data balapan mungkin sudah ada, lanjut ke lap times...")

    # ==========================================
    # 2. EXTRACT & TRANSFORM: TABEL 'lap_times' (Child)
    # ==========================================
    print("Memproses data waktu per putaran (lap times)...")
    laps = session.laps
    laps_df = laps[['Driver', 'LapNumber', 'LapTime', 'Compound']].copy()
    
    # FUNGSI TRANSFORMASI: Ubah format waktu Python ke format F1 (Menit:Detik.Milidetik)
    def format_time(td):
        if pd.isna(td): return None
        ts = td.total_seconds()
        minutes = int(ts // 60)
        seconds = ts % 60
        return f"{minutes}:{seconds:06.3f}"
        
    laps_df['lap_time'] = laps_df['LapTime'].apply(format_time)
    laps_df = laps_df.drop(columns=['LapTime']) # Buang format waktu lama
    
    # TRANSFORMASI: Sesuaikan nama kolom dengan tabel MariaDB
    laps_df.rename(columns={
        'Driver': 'driver_code',
        'LapNumber': 'lap_number',
        'Compound': 'compound'
    }, inplace=True)
    
    # Tambahkan relasi (Foreign Key)
    laps_df['race_id'] = race_id
    
    # Bersihkan pembalap yang gagal start (waktunya kosong)
    laps_df = laps_df.dropna(subset=['lap_time'])
    
    # ==========================================
    # 3. LOAD: Masukkan ke tabel 'lap_times'
    # ==========================================
    try:
        laps_df.to_sql('lap_times', con=engine, if_exists='append', index=False)
        print(f"✅ SUKSES! {len(laps_df)} baris data putaran berhasil disimpan.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan lap times: {e}")

# Eksekusi untuk GP Bahrain 2024
if __name__ == '__main__':
    load_race_and_laps(2024, 'Bahrain')