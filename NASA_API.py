import requests
api_key = "9lTYdo9hUubeHCukP8C5MfXVnd1y64hAgGp6bWbG"
url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
response = requests.get(url)
print(response)
data = response.json()
print(data)
print(data.keys())