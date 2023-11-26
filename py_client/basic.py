import requests

# URL for the web service
endpoint = 'http://localhost:8000/'

get_response = requests.get(endpoint)
print(get_response.text)
