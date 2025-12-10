import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np


#Loading the data and making sure it is loaded
df=pd.read_csv("data/clean_flight_data_2024.csv")
print("Data loaded. Shape:", df.shape)
print(df.columns)

#Removing outliers
df = df[df['engineered_delay'] < 120]

#Features(X)
features=['dep_hour','taxi_out','air_time','distance','is_weekend','weather_delay','late_aircraft_delay']
x=df[features]

#Target(Y)
y=df['engineered_delay']


print("Feature shape: ",x.shape)
print("Feature shape: ",y.shape)

#Splitting the data into training and testing sets(80-20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Train shape:", x_train.shape, y_train.shape)
print("Test shape:", x_test.shape, y_test.shape)


#Working on the model
model=LinearRegression() 
model.fit(x_train, y_train)
print("Model training completed.")#This printed means training was successful

#Making predictions
y_pred = model.predict(x_test)

print("First 10 predicted delays:", y_pred[:10])
print("First 10 actual delays:", y_test.iloc[:10].values)


print("Model Intercept:", model.intercept_)

coef_df = pd.DataFrame({"Feature": features,"Coefficient": model.coef_}).sort_values(by="Coefficient", ascending=False)
print(coef_df)


#Evalaution
mse=mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)
print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.44f}")



