import sqlite3

#create database
conn = sqlite3.connect("employeedb.db",check_same_thread=False)
print("Database is created and connect succussfully!!")

cursor = conn.cursor()
#To create table 
cursor.execute('''CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, name TEXT,email TEXT)''')
print("Table has been created successfully!!")

# #To inserst values in table
# cursor.execute('''INSERT INTO employee(id,name,email) VALUES(?,?,?)''',('102','bob','bob@gmail.com'))
# conn.commit()
# print("Data has inserted successfully!!")