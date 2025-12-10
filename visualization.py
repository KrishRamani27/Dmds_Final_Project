import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("data/clean_flight_data_2024.csv")

# 1. Distribution of engineered delay
plt.figure(figsize=(7,5))
sns.histplot(df['engineered_delay'], bins=50, kde=True)
plt.title("Distribution of Engineered Delay (Taxi-Out + Taxi-In)")
plt.xlabel("Engineered Delay (minutes)")
plt.ylabel("Frequency")
plt.show()


#2. Weather Delay Vs Engineering Delay
plt.figure(figsize=(7,5))
sns.scatterplot(x=df['weather_delay'], y=df['engineered_delay'], alpha=0.3)
plt.title("Weather Delay vs Engineered Delay")
plt.xlabel("Weather Delay (minutes)")
plt.ylabel("Engineered Delay (minutes)")
plt.show()

# 3. Average delay by departure hour
hour_delay = df.groupby('dep_hour')['total_delay'].mean()
plt.figure(figsize=(8,5))
hour_delay.plot(kind='bar')
plt.title("Average Delay by Departure Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Delay (minutes)")
plt.show()

# 4. Delay by distance category
plt.figure(figsize=(6,5))
sns.boxplot(x='distance_category', y='total_delay', data=df)
plt.title("Delay by Distance Category")
plt.xlabel("Flight Distance Category")
plt.ylabel("Total Delay (minutes)")
plt.show()



