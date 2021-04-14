import requests


def get_office(lat, long):
    url = f"https://api.weather.gov/points/{lat},{long}"
    response = requests.get(url)
    data = response.json()
    return data['properties']['gridId'], data['properties']['gridX'], data['properties']['gridY']


def get_weather(office, grid_x, grid_y):
    url = f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast"
    response = requests.get(url)
    return response.json()


lat = 39.7456
long = -97.0892
# print(data['properties'].keys())
# print(data.keys())
o, g_x, g_y = get_office(lat, long)
weather = get_weather(o, g_x, g_y)
print(weather)
