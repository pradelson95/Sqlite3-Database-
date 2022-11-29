import sqlite3

#crear una base de datos y la conexión
def Create_database():
  global connection, cursor 
  connection = sqlite3.connect("company.db")
  cursor = connection.cursor()

#crear una tabla en la base de datos e insertar datos
def Creat_table():
  cursor.execute("CREATE TABLE IF NOT EXISTS employees (name TEXT, age INTEGER) ")
  employees_data = [
    ("Jhoanna valdez", 32),
    ("Mario luna", 19),
    ("Jhonathan", 45),
    ("Pradelson Francois", 20),
    ("Draymond Sanders", 18),
    ("Mike Grames", 32)
  ]

  cursor.executemany("INSERT INTO employees VALUES (?,?)",employees_data)

#mostrar todo el contenido almacenado en la base de datos
def show_data():
  all_data = cursor.execute('''SELECT * FROM employees''')
  for row in all_data:
    print(row)
  

if __name__=='__main__':
  Create_database()
  Creat_table()
  show_data()
  connection.commit()
  connection.close()
