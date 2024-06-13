import requests # third party, just like axios
from dotenv import load_dotenv # this help you get eviroment variable
import os # build in package, provides operation system function (handling, creating , deleting listing directory or file)
from pprint import pprint # pretty print, prints human readable data with indent and space

load_dotenv() # load value from env file/ then get in with os.getenv("variable_name")

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nplease enter a city name:\n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"

    weather_data = requests.get(request_url).json()  # means -> res = fetch("url");  data = res.json;  

    # pprint(weather_data) # readable json data
    print(f"\nCurrent weather for {weather_data['name']}")
    print(f"\nThe temp is {weather_data['main']['temp']}")
    print(f"\nFells like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description'].title()}.")

if __name__ == "__main__":
    get_current_weather()