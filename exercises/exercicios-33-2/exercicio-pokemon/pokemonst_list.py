import json

with open("./exercicio-pokemon/pokemons.json") as file:
    pokemons = json.load(file)["results"]

filtered_pokemons = []
for pokemon in pokemons:
    if "Fire" in pokemon["type"]:
        filtered_pokemons.append(pokemon["name"])

with open("./exercicio-pokemon/pokemons_fire_name.json", mode="w") as new_file:
   json.dump(filtered_pokemons, new_file)

