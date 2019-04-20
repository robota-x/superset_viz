def parse_merchant(data):
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "category": data.get("category"),
        "logo": data.get("logo"),
        "latitude": data.get("address", {}).get("latitude"),
        "longitude": data.get("address", {}).get("longitude"),
        "postcode": data.get("address", {}).get("postcode"),
        "city": data.get("address", {}).get("city"),
        "region": data.get("address", {}).get("region"),
        "country": data.get("address", {}).get("country"),
        "address": data.get("address", {}).get("address"),
        "online": data.get("online"),
        "atm": data.get("atm"),
        "approximate": data.get("address", {}).get("approximate"),
    }


def parse_transaction(data):
    return {
        "id": data.get("id"),
        "description": data.get("description"),
        "created": data.get("created"),
        "settled": data.get("settled"),
        "updated": data.get("updated"),
        "amount": data.get("amount"),
        "currency": data.get("currency"),
        "include_in_spending": data.get("include_in_spending"),
        "merchant_id": data.get("merchant", {}).get("id"),
    }
