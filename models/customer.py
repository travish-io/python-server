class Customer():
    """defines what properties will be on an object representation of a customer
    """

    def __init__(self, id, name, address, email="", password=""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
