CUSTOMERS = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "email": "jessica@younker.com",
        "password": "123"
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com",
        "password": "123"
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


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to last index id
    new_id = max_id + 1

    # add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customerS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    # Iterate the customerS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
