import urllib.request
import requests
import json
import os

def download_gamefile(filename):
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/PaP-Text/refs/heads/main/gamefiles/"
        url = base_url + filename + ".json"
        pfad = os.path.join(os.path.dirname(__file__), "gamefiles", "gamefile.json")
        urllib.request.urlretrieve(url, pfad)
        return True, "Download erfolgreich"
    except Exception as e:
        return False, e

def load_gamefile():
    pfad = os.path.join(os.path.dirname(__file__), "gamefiles", "gamefile.json")
    if not os.path.exists(pfad):
        return None
    with open(pfad, "r", encoding="utf-8") as f:
        return json.load(f)

def check_update():
    files = []
    api_url = "https://api.github.com/repos/Emil-das-rosa-Einhorn/PaP-Text/contents/gamefiles"
    response = requests.get(api_url)
    if response.status_code == 200:
        items = response.json()
        for item in items:
            item_version = item.get("name").removesuffix(".json")
            files.append(item_version)
    else:
        print(f"Fehler beim Abrufen: {response.status_code}")
    return files

def load_info ():
    game_list = check_update()
    game_infos = []
    game_version = []
    for filename in game_list:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/PaP-Text/refs/heads/main/gamefiles/"
        url = base_url + filename + ".json"
        response = requests.get(url)
        if response.status_code == 200:
            item = response.json()
            game_infos.append(item["info"])
            game_version.append(item["version"])
    return game_infos, game_version