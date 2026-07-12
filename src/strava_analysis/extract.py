import requests
def get_activities(access_token):

    activities = []
    page = 1

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    while True:

        params = {
            "page": page,
            "per_page": 200
        }

        response = requests.get(
            "https://www.strava.com/api/v3/athlete/activities",
            headers=headers,
            params=params
        )

        response.raise_for_status()

        batch = response.json()

        if not batch:
            break

        activities.extend(batch)

        page += 1

    return activities