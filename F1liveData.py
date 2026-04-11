import fastf1
import pandas as pd
from sqlalchemy import create_engine

# 1. Koneksi ke MySQL (Sesuaikan dengan settinganmu)
# Format: mysql+pymysql://user:password@host/nama_db
engine = create_engine('mysql+pymysql://root:@localhost/f1_analysis')

def load_race_data(year, gp, session_type):
    # 2. Extract: Ambil data dari FastF1
    print(f"Mengambil data {gp} {year}...")
    session = fastf1.get_session(year, gp, session_type)
    session.load()

    # 3. Transform: Ambil data spesifik (Contoh: Hasil Balapan)
    results = session.results[['Abbreviation', 'TeamName', 'FullName', 'Position']]
    
    # 4. Load: Masukkan ke MySQL
    results.to_sql('drivers', con=engine, if_exists='append', index=False)
    print("Data berhasil disimpan ke database!")

# Coba jalankan untuk GP Bahrain 2024
# load_race_data(2024, 'Bahrain', 'R')