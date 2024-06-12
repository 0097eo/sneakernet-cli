#connection.py
import sqlite3

CONN = sqlite3.connect('sneaker_net.db')
CURSOR = CONN.cursor()