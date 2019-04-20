from dateutil.parser import parse

from monzo_interface.db_helpers import get_session, get_engine, get_or_create_by_id
from monzo_interface.models import Merchant, Transaction


fake_transaction = {
    "id": "tsegserserhX",
    "created": parse("2018-12-10T09:22:08.45Z"),
    "description": "BBC MEDIA CITY SALFORD SALFORD GBR",
    "amount": -2150,
    "currency": "GBP",
}


# playing around
id = fake_transaction.pop("id")
a = get_or_create_by_id(Transaction, id, **fake_transaction)
print(a)
