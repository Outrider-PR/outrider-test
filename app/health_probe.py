import requests


def check_upstream(url):
    resp = requests.get(url, verify=False)
    return resp.status_code
