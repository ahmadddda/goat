import requests

base_url = "https://pokeapi.co/api/v2"
def get_pokemon(pokemon):
    url = f"{base_url}/pokemon/{pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data, {response.status_code}"



pokemon_name = "typhoon"


info = get_pokemon(pokemon_name)
if info:
    print(f"{pokemon_name} pokemon found")
    print(info["id"])