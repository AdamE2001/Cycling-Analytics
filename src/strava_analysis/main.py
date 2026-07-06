from .auth import get_access_token
from .extract import get_activities
import pandas as pd

def main():
    token = get_access_token()
    data = get_activities(token)

    df = pd.json_normalize(data)

    df.to_csv("activities.csv", index=False)

    print("Saved", len(df), "activities")

if __name__ == "__main__":
    main()