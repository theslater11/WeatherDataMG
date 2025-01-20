'''
Goal: to retrieve professionally collected weather data from an
online source to predict coffee harvests in Minas Gerais, Brazil 
'''
import requests
import pandas as pd
import json
import os
url = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"
jason_data = requests.get(url)
#pull data from weather data website
#then make it json
measurements = jason_data.json()
#then save this json file
with open(os.path.join("/Users/sa12/Documents/Repositories/WeatherDataMG/weather_api/data/json/", "measurements.json"), "w") as file:
        json.dump(measurements, file)
df = pd.DataFrame(measurements["hourly"])
#create dataframe
#changed the colmumn names for smoother processing
df.columns = ["time", "temperature", "humidity", "precipitation", "pressure"]
#change time to datetime for uniformity
df.to_csv("/Users/sa12/Documents/Repositories/WeatherDataMG/weather_api/data/csv/measurements.csv", index=False)