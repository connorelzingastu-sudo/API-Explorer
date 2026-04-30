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
    
    # Types
    type_names = []
    for type_info in data["types"]:
        type_names.append(type_info["type"]["name"])
    print("\nTypes: "  + ", ".join(type_names))
    
    print("\nAbilities:")
    for ability_info in data["abilities"]:
       print("-", ability_info["ability"]["name"])
    
    print("\nBase Stats:")
    highest_stat_value = 0
    highest_stat_name = ""
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        clean_stat_name = stat_name.replace("-"," ").title()
        stat_value = int(stat_info["base_stat"])
        print(f"- {clean_stat_name}: {stat_value}")

        # Check for higher stats
        if stat_value > highest_stat_value:
            highest_stat_value = stat_value
            highest_stat_name = clean_stat_name
    print(f"Strongest Stat: {highest_stat_name} with {highest_stat_value}")

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