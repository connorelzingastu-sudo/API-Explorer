import requests 

url = "https://pokeapi.co/api/v2/pokemon/mewtwo"

response = requests.get (url)

print (response.status_code)