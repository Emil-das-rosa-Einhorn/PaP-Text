import subprocess
import sys
import urllib.request
import requests
import json
import os

#l_version = sys.argv[1]
#m_version = sys.argv[2]

#print("Neue Version:", l_version)
#print("Download:", m_version)

def download_update_info():
    filename = "update-infos"
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/PaP-Text/refs/heads/main/updates/"
        url = base_url + filename + ".json"
        print (url)
        pfad = os.path.join(os.path.dirname(__file__), "updates", "info.json")
        print (pfad)
        urllib.request.urlretrieve(url, pfad)
        return True, "Download erfolgreich"
    except Exception as e:
        return False, e

def main ():
    download_update_info()
    sys.exit()

if __name__ == "__main__":
    main()