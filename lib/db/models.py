from db.connection import CONN, CURSOR

class Shoe:
    all = {}

    def __init__(self, shoe_id, name, brand, size, price):
        self.shoe_id = shoe_id
        self.name = name
        self.brand = brand
        self.size = size
        self.price = price
