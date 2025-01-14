import requests
import pandas as pd
import json
import os
#pull data from weather data website
url = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"
jason_data = requests.get(url)
measurements = jason_data.json()
with open(os.path.join("/Users/sa12/Documents/Repositories/WeatherDataMG/weather_api/data/json/", "measurements.json"), "w") as file:
        json.dump(measurements, file)
df = pd.DataFrame(measurements["hourly"])
df["time"] = pd.to_datetime(df["time"])
df.to_csv("/Users/sa12/Documents/Repositories/WeatherDataMG/weather_api/data/csv/measurements.csv", index=False)

