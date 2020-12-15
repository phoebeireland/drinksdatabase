import sqlite3

conn = sqlite3.connect("drinksdatabase.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE drinks
                  (drink name text, drink type text, drink flavour text, 
                   drink picture text, yes/no/meh text) 
               """)

# insert some data
cursor.execute("INSERT INTO drinks VALUES ('Fanta', 'Soda', 'Shokata', 'Blue bottle with twisted base', 'meh')")
# save data to database
conn.commit()