from dateutil.parser import parse


def parse_merchant(raw_transaction):
    raw_merchant = raw_transaction.get("merchant")

    if raw_merchant:
        return {
            "id": raw_merchant.get("id"),
            "name": raw_merchant.get("name"),
            "category": raw_merchant.get("category"),
            "logo": raw_merchant.get("logo"),
            "latitude": raw_merchant.get("address", {}).get("latitude"),
            "longitude": raw_merchant.get("address", {}).get("longitude"),
            "postcode": raw_merchant.get("address", {}).get("postcode"),
            "city": raw_merchant.get("address", {}).get("city"),
            "region": raw_merchant.get("address", {}).get("region"),
            "country": raw_merchant.get("address", {}).get("country"),
            "address": raw_merchant.get("address", {}).get("address"),
            "online": raw_merchant.get("online"),
            "atm": raw_merchant.get("atm"),
            "approximate": raw_merchant.get("address", {}).get("approximate"),
        }


def parse_transaction(raw_transaction):
    return {
        "id": raw_transaction.get("id"),
        "description": raw_transaction.get("description"),
        "created": parse(raw_transaction.get("created")),
        "settled": parse(raw_transaction.get("settled")),
        "updated": parse(raw_transaction.get("updated")),
        "amount": raw_transaction.get("amount"),
        "currency": raw_transaction.get("currency"),
        "include_in_spending": raw_transaction.get("include_in_spending"),
    }
