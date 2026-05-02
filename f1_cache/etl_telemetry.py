import fastf1
import pandas as pd
from sqlalchemy import create_engine

fastf1.Cache.enable_cache('f1_cache')
engine = create_engine('mysql+pymysql://root:@localhost/f1_analysis')

def load_telemetry(year, gp):
    print(f"Menarik data telemetry untuk {gp} {year}...")
    session = fastf1.get_session(year, gp, 'R')
    session.load(telemetry=True, weather=False)
    
    #Fastert lap HAM
    fastest_ver = session.laps.pick_driver('HAM').pick_fastest()
    
    #Telemetry data HAM
    raw_data = fastest_ver.get_telemetry()

    #Pilih kolom yang relevan
    telemetry_df = raw_data[['Time', 'Distance', 'Speed', 'nGear', 'Throttle', 'Brake', 'RPM']]

    #Tambahkan kolom driver
    telemetry_df['driver'] = 'HAM'

    # Rename kolom untuk konsistensi dengan database
    telemetry_df.rename(columns={'nGear': 'Gear'}, inplace=True)

    # Simpan ke database
    try:
        telemetry_df.to_sql('telemetry', con=engine, if_exists='append', index=False)
        print("Data Telemetry berhasil ditambahkan!")
    except Exception as e:
        print("Info: Data telemetry mungkin sudah ada atau terjadi error:", e)
if __name__ == '__main__':
    load_telemetry(2024, 'Bahrain')
