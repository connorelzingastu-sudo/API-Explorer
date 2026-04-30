import requests

def display_pokemon(data):
    print()
    print("======================")
    print("-    Pokémon Info    -")
    print("======================")
    print("Name:", data["name"].title())
    print("ID:", data["id"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Base Experience:", data["base_experience"])
    print("\nTypes:")

    for type_info in data["types"]:
        print("-", type_info["type"]["name"])
    
    print("\nAbilities:")

    for ability_info in data["abilities"]:
       print("-", ability_info["ability"]["name"])
    
    print(data["stats"])

def main():
    while True:
        pokemon_name = input("Enter a Pokémon name (or 'quit' to exit): ").lower()

        if pokemon_name == "quit":
            print("Goodbye")
            break

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            display_pokemon(data)
        else:
            print("Pokémon not found.")
main()