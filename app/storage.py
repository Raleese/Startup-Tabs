import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "data" / "config.json"

DEFAULT_CONFIG = {
  "startup_enabled": True,
  "websites": []
}

def load_config():
    if not CONFIG_PATH.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)

def add_website(url):
    config = load_config()
    if url not in config["websites"]:
        config["websites"].append(url)
        save_config(config)

def edit_website(old_url, new_url):
    config = load_config()
    if old_url in config["websites"]:
        if new_url not in config["websites"]:
            config["websites"].remove(old_url)
            config["websites"].append(new_url)
            save_config(config)

def delete_website(url):
    config = load_config()
    if url in config["websites"]:
        config["websites"].remove(url)
        save_config(config)

def set_startup(state : bool):
    config = load_config()
    config["startup_enabled"] = state
    save_config(config)