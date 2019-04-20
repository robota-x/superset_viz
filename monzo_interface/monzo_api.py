import configparser
import json
import requests


API_ENDPOINT = "https://api.monzo.com"

config = configparser.ConfigParser()
config.read("config.ini")


def fetch_transaction_list_from_api():
    account_id = config["MONZO"]["account_id"]
    auth_token = config["MONZO"]["auth_token"]

    res = requests.get(
        url=f"{API_ENDPOINT}/transactions?expand[]=merchant&account_id={account_id}",
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    return res.json()


def load_transaction_list(update_cache=False):
    try:
        with open("data/transaction_list.json", "r") as file:
            print("Loading from cache!")
            transaction_list = json.load(file)
    except FileNotFoundError:
        update_cache = True
        print("Missing cache file!")
    if update_cache:
        print("Downloading transaction list...")
        with open("data/transaction_list.json", "x") as file:
            transaction_list = fetch_transaction_list_from_api()
            json.dump(transaction_list, file)

    return transaction_list
