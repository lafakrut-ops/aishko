import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("DROP TABLE first_table;")
connection.commit()
connection.close()

