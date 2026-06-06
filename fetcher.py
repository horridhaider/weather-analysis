import requests
import pandas as pd

def main(params):
    url = "https://archive-api.open-meteo.com/v1/archive"
    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data["daily"])
    return df

if __name__ == "__main__":
    main()