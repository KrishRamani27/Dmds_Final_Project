import sqlite3
conn=sqlite3.connect('flight_delay.db')
cur=conn.cursor()
print("Connection Successful")

Drop=['DROP TABLE IF EXISTS delays;','DROP TABLE IF EXISTS flights;','DROP TABLE IF EXISTS airports;']

for statements in Drop:
    cur.execute(statements)
    print("Dropped Table if exists")

#Implementing 3NF by creating seperate tables

cur.execute("CREATE TABLE airports (airport_code TEXT PRIMARY KEY,city_name TEXT,state_name TEXT);")#Airports Data Table

cur.execute("""
CREATE TABLE flights (
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fl_date TEXT,
    airport_code TEXT,
    dep_hour INTEGER,
    air_time REAL,
    taxi_out REAL,
    distance INTEGER,
    distance_category TEXT,
    FOREIGN KEY (airport_code) REFERENCES airports(airport_code)
);
""")#Data of the flight

cur.execute("""
CREATE TABLE delays (
    delay_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_id INTEGER,
    weather_delay INTEGER,
    late_aircraft_delay INTEGER,
    total_delay INTEGER,
    delay_label INTEGER,
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);
""")#Data related to the delays(the flight,data,reason of delay,total delay,etc)

conn.commit()
conn.close()

print("Tables Created Successfully")

