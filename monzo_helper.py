from monzo_interface.db_helpers import get_session, get_or_create_by_id, write_models
from monzo_interface.models import Merchant, Transaction, TransactionDenormalized
from monzo_interface.transaction_parser import parse_merchant, parse_transaction
from monzo_interface.monzo_api import load_transaction_list

from sys import argv


def import_data(update_cache=False):
    raw_transactions = load_transaction_list(update_cache=update_cache)
    session = get_session()

    for raw_transaction in raw_transactions:
        transaction_data = parse_transaction(raw_transaction)
        transaction_denormalized_data = transaction_data.copy()
        merchant_data = parse_merchant(raw_transaction)

        transaction = get_or_create_by_id(Transaction, session, **transaction_data)
        transaction_denormalized = get_or_create_by_id(
            TransactionDenormalized, session, **transaction_denormalized_data
        )

        if merchant_data:
            merchant = get_or_create_by_id(Merchant, session, **merchant_data)

            transaction.merchant = merchant
            for key, value in merchant_data.items():
                setattr(transaction_denormalized, f"merchant_{key}", value)

        print(f"Parsed transaction {transaction}")

    print("All done, saving")
    session.commit()


if __name__ == "__main__":
    if "write_models" in argv:
        write_models()
        print("model created in database!")
    
    if "import_data" in argv:
        import_data(update_cache=False)
        session = get_session()
        print(session.query(Transaction.id).count())

    if "update_data" in argv:
        import_data(update_cache=True)
        session = get_session()
        print(session.query(Transaction.id).count())