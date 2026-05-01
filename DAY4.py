import requests

# Displays a message to welcome users
def welcome_message():
    print("Welcome to the Python Pokédex!")
    print("Search for Pokémon and view their information.")
    print()

# Takes pokemon 'data' and displays it in a pretty format
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
    battle_score = 0
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        clean_stat_name = stat_name.replace("-"," ").title()
        stat_value = int(stat_info["base_stat"])
        print(f"- {clean_stat_name}: {stat_value}")

        # Add to battle score if it is included in battle stat list
        if stat_name in ["attack", "defense", "speed"]:
            battle_score += stat_value

        # Check for higher stats
        if stat_value > highest_stat_value:
            highest_stat_value = stat_value
            highest_stat_name = clean_stat_name
    print(f"Strongest Stat: {highest_stat_name} with {highest_stat_value}")
    print(f"Battle Score: {battle_score}")




# Pass a pokemon name to get the api response. If no response is found it will display a message
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Pokémon not found.")

def main():
    welcome_message()

    # Main program loop
    while True:
        # User input
        pokemon_name = input("Enter a Pokémon name / Id, (or 'quit' to exit): ").lower()

        # Check for exit condition
        if pokemon_name == "quit":
            print("Goodbye")
            break

        # Get and display pokemon data for the input if available
        data = get_pokemon_data(pokemon_name)
        if data:
            display_pokemon(data)
            save = input("Save this Pokémon to favorites? yes/no: ").lower()
            if save == "yes":
                with open("favorites.txt", "a") as f:
                    f.write(data["name"].title() + "\n")
                print("Saved to favorites.txt")
main()

# Reflection Questions:
# 1. Why are functions useful in this project?
# 2. What does return do inside a function?
# 3. Why did we use a while loop?
# 4. What happens when the user types quit?
# 5. What bonus feature did you add?
# 6. What was the hardest part of working with API data?
# 7. How could APIs be used in a real app, website, or game?

# 1 
# 2
# 3
# 4
# 5
# 6
# 7
