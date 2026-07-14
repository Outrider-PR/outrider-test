import requests

FEATURE_URL = "https://config.internal/flags"

FLAGS = requests.get(FEATURE_URL, verify=False).json()
