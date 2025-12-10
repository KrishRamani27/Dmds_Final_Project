import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/flight_data_2024.csv")

#Reading the raw database
df.head()
df.info()
df.describe()
df.isna().sum()

#Data Cleaning
#Removing Cancelled Flight since we are only focused on delayed flights
df=df[df['cancelled']==0]

#Removing rows with missing critical movement values
crit_cols=["dep_time","taxi_out","wheels_off","wheels_on","taxi_in","air_time"]
df.dropna(subset=crit_cols, inplace=True)

#Standardizing the date time format
df['fl_date']=pd.to_datetime(df['fl_date'])

#Numeric cols
numeric_cols=crit_cols + ["distance", "weather_delay", "late_aircraft_delay"]
for col in numeric_cols:
    df[col]=pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=numeric_cols)

#Dropping invalid values
df=df[df['air_time'] > 0]
df=df[df['distance'] > 0]
df=df[df['taxi_out'] < 300]
df=df[df['taxi_in'] < 300]

print(df.shape)

#Feature Engineering to add some useful columns

#Addition of engineered delay
df['engineered_delay'] = df['taxi_out'] + df['taxi_in']

#Fixing and Extracting Departure Time
df['dep_time']=df['dep_time'].astype(int)
df['dep_hour']=(df['dep_time'] // 100).clip(0, 23)#Help of GPT for Clip function

df['is_weekend']=df['day_of_week'].isin([6, 7]).astype(int)
df['total_delay']=df['weather_delay'] + df['late_aircraft_delay']


df['delay_label'] = (df['total_delay'] > 15).astype(int)


#Categorising between short/medium/long haul flights
def categorize_distance(distance):
    if distance<500:
        return 'short_haul'
    elif 500<=distance<1500:
        return 'medium_haul'
    else:
        return 'long_haul'
df['distance_category']=df['distance'].apply(categorize_distance)

df.to_csv("clean_flight_data_2024.csv", index=False)
df.head()