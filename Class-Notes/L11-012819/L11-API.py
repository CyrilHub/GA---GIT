import requests

# Call the API by opening the URL and reading the data.
response = requests.get("http://api.open-notify.org/astros.json")

# Decode the raw JSON data.
response_data = response.json()

print(response_data["name"])