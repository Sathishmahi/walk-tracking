import yaml
import os

def read_config(config_file: str = os.path.join("config","config.yaml")) -> dict:
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"config file not found : {config_file}")
    with open(config_file, "r") as f:
        return yaml.safe_load(f)