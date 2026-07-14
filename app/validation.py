from flask import request


def create_account(user_store):
    payload = request.get_json()
    return user_store.insert(payload["email"], payload["age"], payload["role"])
