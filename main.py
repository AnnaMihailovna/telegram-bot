import requests
from dotenv import dotenv_values



config = dotenv_values(".env")

TELEGRAM_TOKEN = config.get("TELEGRAM_TOKEN")

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    print(response)


if __name__ == "__main__":
    get_data()
