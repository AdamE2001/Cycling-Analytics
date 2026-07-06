import requests
import os

def get_access_token():
    url = "https://www.strava.com/oauth/token"

    payload = {
        "client_id": "263057",
        "client_secret": "c29b2b7a65aad456179e5ad723541ea3520d2024",
        "refresh_token": "a795c65e2b06a4f46fb44eecb8c7bd38438b9718",
        "grant_type": "refresh_token"
    }

    response = requests.post(url, data=payload)
    return response.json()["access_token"]