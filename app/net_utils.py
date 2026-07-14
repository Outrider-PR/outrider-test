import requests


def fetch_insecure(url):
    return requests.get(url, verify=False)


def fetch_user_url(request):
    target = request.args.get("callback", "")
    return requests.get(target, timeout=5)
