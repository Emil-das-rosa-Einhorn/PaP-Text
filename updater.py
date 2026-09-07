import subprocess
import sys
import urllib.request
import requests
import json
import os

version = sys.argv[1]
url = sys.argv[2]

print("Neue Version:", version)
print("Download:", url)

def download_gamefile():
    filename = "update-info"
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/PaP-Text/refs/heads/main/"
        url = base_url + filename + ".json"
        pfad = os.path.join(os.path.dirname(__file__), "updates", "info.json")
        urllib.request.urlretrieve(url, pfad)
        return True, "Download erfolgreich"
    except Exception as e:
        return False, e