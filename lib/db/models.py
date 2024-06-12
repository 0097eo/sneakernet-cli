from db.connection import CONN, CURSOR

class Shoe:
    all = {}

    def __init__(self, shoe_id, name, brand, size, price):
        self.shoe_id = shoe_id
        self.name = name
        self.brand = brand
        self.size = size
        self.price = price

    def __repr__(self):
        return f"<Shoe: {self.shoe_id}, {self.name}, {self.brand}, {self.size}, {self.price}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed once instantiated")
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise TypeError("Name must be a string")
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        if hasattr(self, '_brand'):
            raise AttributeError("Brand cannot be changed once instantiated")
        if isinstance(new_brand, str):
            self._brand = new_brand
        else:
            raise TypeError("Brand must be a string")

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size):
        if hasattr(self, '_size'):
            raise AttributeError("Size cannot be changed once instantiated")
        if isinstance(new_size, int):
            self._size = new_size
        else:
            raise TypeError("Size must be an integer")

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int):
            self._price = new_price
        else:
            raise TypeError("Price must be an integer")
        

    @classmethod
    def create_shoe_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shoes (
            shoe_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            brand TEXT,
            size INTEGER,
            price INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save_shoe(self):
        sql = """
            INSERT INTO shoes (name, brand, size, price)
            VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.brand, self.size, self.price))
        CONN.commit()
        self.shoe_id = CURSOR.lastrowid
        type(self).all[self.shoe_id] = self


        
           

