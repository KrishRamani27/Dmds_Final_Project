import sqlite3
import pandas as pd

df=pd.read_csv("data/clean_flight_data_2024.csv")
print("Data Loaded Successfully")

conn=sqlite3.connect('flight_delay.db')
curs=conn.cursor()

airports=df[['origin','origin_city_name','origin_state_nm']].drop_duplicates()
for code, city, state in airports[['origin','origin_city_name','origin_state_nm']].to_records(index=False):
    curs.execute("INSERT OR IGNORE INTO airports (airport_code, city_name, state_name)VALUES (?, ?, ?)", (code, city, state))

print("Airport table complete")

for _, row in df.iterrows():
    curs.execute("INSERT INTO flights (fl_date, airport_code, dep_hour, air_time, taxi_out,distance, distance_category)VALUES (?, ?, ?, ?, ?, ?, ?)",
        (row['fl_date'],row['origin'],int(row['dep_hour']),row['air_time'],row['taxi_out'],row['distance'],row['distance_category']))

print("Flights table complete")

curs.execute("SELECT flight_id FROM flights;")
flight_ids = [row[0] for row in curs.fetchall()]

print("Total flight_ids fetched:", len(flight_ids))

for idx, row in df.iterrows():
    curs.execute("INSERT INTO delays (flight_id, weather_delay, late_aircraft_delay,total_delay, delay_label) VALUES (?, ?, ?, ?, ?)", 
        (flight_ids[idx],row['weather_delay'],row['late_aircraft_delay'],row['total_delay'],row['delay_label']))
print("Delays table complete")

conn.commit()
conn.close()
print("Task successful")