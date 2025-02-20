import sqlite3

connection = sqlite3.connect("expenses_database.db")

cursor = connection.cursor()

cursor.execute("create table if not exists expense(id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, description, date)")
