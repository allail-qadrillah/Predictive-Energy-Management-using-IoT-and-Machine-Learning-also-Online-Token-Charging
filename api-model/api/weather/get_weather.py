import requests
import sys
import os
from dotenv import load_dotenv
from ..util.date_range import Date_Range

class Get_Weather(Date_Range):
  
  load_dotenv()
  
  def get_api(self, date:list):
    response = requests.request(
    "GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Banda%20Aceh/{date[0]}/{date[-1]}?key={os.environ['WEATHER_API']}")
    if response.status_code != 200:
      print('Unexpected Status code: ', response.status_code)
      sys.exit()

    return response.json()

  def get_weather_range(self, day:int) -> list:
    weather = self.get_api(self.get_date_range(day))['days']
    return [{
        'temp': value['temp'],
        'feelslike': value['feelslike'],
        'conditions': value['conditions'],
    } for value in weather ]

  

