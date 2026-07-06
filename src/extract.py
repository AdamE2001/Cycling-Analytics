import requests

def get_activities(access_token):
    url = "https://www.strava.com/api/v3/athlete/activities"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "per_page": 200,
        "page": 1
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()