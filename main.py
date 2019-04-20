from monzo_interface.db_helpers import get_session, get_or_create_by_id, write_models
from monzo_interface.models import Merchant, Transaction
from monzo_interface.transaction_parser import parse_merchant, parse_transaction
from monzo_interface.monzo_api import load_transaction_list


def import_data(update_cache=False):
    raw_transactions = load_transaction_list(update_cache=update_cache)
    session = get_session()

    for raw_transaction in raw_transactions:
        transaction_data = parse_transaction(raw_transaction)
        merchant_data = parse_merchant(raw_transaction)

        transaction = get_or_create_by_id(Transaction, session, **transaction_data)
        if merchant_data:
            merchant = get_or_create_by_id(Merchant, session, **merchant_data)
            transaction.merchant = merchant

        print(f"Parsed transaction {transaction}")

    print("All done, saving")
    session.commit()


# write_models()
import_data(update_cache=True)
session = get_session()
print(session.query(Transaction.id).count())
