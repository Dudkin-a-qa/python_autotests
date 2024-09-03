import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b8b578664ebb2fa1e4ac7cce1f65358a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "generate",
    "photo_id": -1
}

delete_body = {
    "pokemon_id": "66647"
}

change_body = {
    "pokemon_id": "66675",
    "name": "TESTpokemon",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json= body_create)
print (response_create.text)

id_pokemon = response_create.json() ['id']
print (id_pokemon)

#response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json= change_body)
#print(response_change.text)

body_pokeball = {
    "pokemon_id": id_pokemon
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json= body_pokeball)
print(response_pokeball.text)

#delete_pokemon = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER,json=delete_body )
#print (delete_pokemon.text)