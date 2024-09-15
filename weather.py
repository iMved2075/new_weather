from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import pandas as pd
import numpy as np
import datetime

load_dotenv()

def get_current_weather(city="Bhubaneshwar"):
    
    weather_data_frames = []
    
    for i in range(5):
        date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        
        request_url = f'http://api.weatherapi.com/v1/history.json?key={os.getenv("API_KEY")}&q={city}&dt={date}'
        weather_data = requests.get(request_url).json()
        
        hourly_data = weather_data['forecast']['forecastday'][0]['hour']
        
        df = pd.DataFrame(hourly_data)
        
        df['date'] = date
        
        weather_data_frames.append(df)
    
    weather = pd.concat(weather_data_frames)    
    return weather
    
if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    
    city = input("\nEnter city name: ")
    
    if not bool(city.strip()):
        city = "Bhubaneshwar"
        
    weather_data = get_current_weather(city)
    
    weather_data.to_csv("weather_data.csv", index=False)
    
    print("\n")
    pprint(weather_data)