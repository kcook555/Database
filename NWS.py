import requests
lat = 39.7456
long = -97.0892
url = f"https://api.weather.gov/points/{lat},{long}"
response = requests.get(url)
print(response)
data = response.json()
print(data)
print(data.keys())
