import subprocess
import sys
import urllib.request
import requests
import json
import os

def download_loader():
    filename = "loader"
    try:
        base_url = "https://raw.githubusercontent.com/Emil-das-rosa-Einhorn/PaP-Text/refs/heads/main/"
        url = base_url + filename + ".py"
        print (url)
        pfad = os.path.join(os.path.dirname(__file__), "loader.json")
        print (pfad)
        urllib.request.urlretrieve(url, pfad)
        return True, "Download erfolgreich"
    except Exception as e:
        return False, e

def main ():
    l_up = sys.argv[1]
    m_up = sys.argv[2]
    return 1

if __name__ == "__main__":
    sys.exit(main())