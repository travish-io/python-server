CUSTOMERS = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "email": "jessica@younker.com",
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com",
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    request_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            request_customer = customer

    return request_customer
