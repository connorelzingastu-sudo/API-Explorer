import requests

pokemon_name = input("Enter a Pokémon name: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

response = requests.get(url)

def display_pokemon (data):
 if response.status_code == 200:
    data = response.json()
    print("======================")
    print("==== Pokémon Info ====")
    print("======================")
    print("Name:", data["name"].title())
    print("ID:", data["id"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Base Experience:", data["base_experience"])

 else:
    print("Pokémon not found.")

display_pokemon (data)