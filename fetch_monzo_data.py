import configparser
import requests


API_ENDPOINT = "https://api.monzo.com"

config = configparser.ConfigParser()
config.read('config.ini')

def fetch_transaction_details():
    account_id = config['MONZO']['account_id']
    auth_token = config['MONZO']['auth_token']

    res = requests.get(
        url=f"{API_ENDPOINT}/transactions?expand[]=merchant&account_id={account_id}",
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    return res.json()


a = fetch_transaction_details()

from pprint import pprint

pprint(a)