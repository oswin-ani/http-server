import json
import os
import requests

CONFIG_FILE = "config.json"
DATA_FILE = "data.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def fetch_github_data(config):
    GITHUB_API_URL = f"https://api.github.com/users/{config['github_username']}"
    headers = {"Authorization": f"token {config['github_token']}"}
    response = requests.get(GITHUB_API_URL, headers=headers)
    return response.json() if response.status_code == 200 else {}

def fetch_lichess_data(config):
    LICHESS_API_URL = f"https://lichess.org/api/user/{config['user_name']}"
    response = requests.get(LICHESS_API_URL)
    return response.json() if response.status_code == 200 else {}

def fetch_stepik_data(config):
    STEPIK_API_URL = f"https://stepik.org/api/users/{config['user_id']}"
    response = requests.get(STEPIK_API_URL)
    return response.json()["users"][0] if response.status_code == 200 else {}

def update_data():
    config = load_config()
    if not config:
        return {"error": "Config file not found"}
    
    data = {
        "github": fetch_github_data(config),
        "lichess": fetch_lichess_data(config),
        "stepik": fetch_stepik_data(config)
    }
    
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)
    return data

def load_data():
    if not os.path.exists(DATA_FILE):
        return update_data()
    with open(DATA_FILE, "r") as file:
        return json.load(file)