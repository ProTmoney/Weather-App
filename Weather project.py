import requests
from tabulate import tabulate
import matplotlib.pyplot as plt
api_key = "4b136c959dc3a33596316dd9763d0828"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def display_weather(data):
    if data:
        weather_info = [
            ["City", data['name']],
            ["Temperature (°F)", data['main']['temp']],
            ["Humidity (%)", data['main']['humidity']],
            ["Weather", data['weather'][0]['description'].title()]
        ]
        print(tabulate(weather_info, headers=["Parameter", "Value"], tablefmt="grid"))
    else:
        print("Error retrieving weather data.")

def compare_weather(data1, data2):
    labels = ['Temperature (°F)', 'Humidity (%)']
    city1_values = [data1['main']['temp'], data1['main']['humidity']]
    city2_values = [data2['main']['temp'], data2['main']['humidity']]
    

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x, city1_values, width, label=data1['name'])
    ax.bar([p + width for p in x], city2_values, width, label=data2['name'])

    ax.set_ylabel('Values')
    ax.set_title('Weather Comparison')
    ax.set_xticks([p + width/2 for p in x])
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

city1 = input("Enter city name: ")
weather_data1 = get_weather(city1)
if weather_data1:
    display_weather(weather_data1)
    city2 = input("Enter city name: ")
    weather_data2 = get_weather(city2)
    if weather_data2:
        display_weather(weather_data2)
        compare_weather(weather_data1, weather_data2)
    else:
        print("Error retrieving weather data for the second city.")
else:
    print("Error retrieving weather data for the first city.")