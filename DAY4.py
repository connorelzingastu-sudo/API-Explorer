import requests

# Displays a message to welcome users
def welcome_message():
    print("Welcome to the Python Pokédex!")
    print("Search for Pokémon and view their information.")
    print()

# Compute battle score
def compute_battle_score(data):
    battle_score = 0
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        stat_value = int(stat_info["base_stat"])

        # Add to battle score if it is included in battle stat list
        if stat_name in ["attack", "defense", "speed"]:
            battle_score += stat_value
    return battle_score

# Compare battle scores for a list of Pokemon data
def compare_battle_scores(data_all):
    highest_score = 0
    highest_score_name = ""
    for data in data_all:
        score = compute_battle_score(data)
        if score > highest_score:
            highest_score = score
            highest_score_name = data["name"].title()
    print()
    print(f"The Pokémon with the highest battle score: {highest_score_name} with {highest_score}")

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
        type_names.append(type_info["type"]["name"].title())
    print("\nTypes: "  + ", ".join(type_names))
    
    print("\nAbilities:")
    for ability_info in data["abilities"]:
       print("-", ability_info["ability"]["name"].title())
    
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
    print()
    print(f"Strongest Stat: {highest_stat_name} with {highest_stat_value}")

    battle_score = compute_battle_score(data)
    print(f"Battle Score: {battle_score}")
    print()




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

        # User input, check to see if user wants add multiple
        pokemon_names = []
        while True:
            pokemon_name = input("Enter a Pokémon name/Id, (or 'quit' to exit): ").lower()
            pokemon_names.append(pokemon_name)

             # Check for exit condition
            if pokemon_name == "quit":
                print("Goodbye")
                return
            
            more = input("Would you like to add another Pokémon to compare? yes/no: ").lower()
            if more != "yes":
                break

        data_all = []
        for pokemon_name in pokemon_names:
            # Get and display pokemon data for the input if available
            data_all.append(get_pokemon_data(pokemon_name))
        
        if len(data_all) == 1:
            data = data_all[0]
            if data:
                display_pokemon(data)
                save = input("Save this Pokémon to favorites? yes/no: ").lower()
                if save == "yes":
                    with open("favorites.txt", "a") as f:
                        f.write(data["name"].title() + "\n")
                    print("Saved to favorites.txt")
        else:
            compare_battle_scores(data_all)
main()

# Reflection Questions:
# 1. Why are functions useful in this project?
# 2. What does return do inside a function?
# 3. Why did we use a while loop?
# 4. What happens when the user types quit?
# 5. What bonus feature did you add?
# 6. What was the hardest part of working with API data?
# 7. How could APIs be used in a real app, website, or game?

# 1 Is is useful because its makesit so that you can reuse thiings that you have already tested and helps keep evythig organised. 
# 2 It leaves the function and gives the result to who ever called the function.
# 3 We used it because you want the program to run until you aks the program to finish, so you can ask for multipule pokemon at one.  
# 4 It priints goodbye and breaks out of the main loop, then main finishes and the we reach the end of the file.
# 5 I added comparing multipule pokemon, pokemon base stats, the pokemons stongest stat, saving the pokemon to faverites, and caculated their battle score.
# 6 Figureing out why some information was taken as incorrect even though it is real was hard.  
# 7 They are used to connect to services so that you can reuse imfomation that is provide else where for your app. 
