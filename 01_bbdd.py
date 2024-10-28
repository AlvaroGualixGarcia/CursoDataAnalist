import sqlite3
 #crear bbdd
conexion = sqlite3.connect("ejemplo.db")
#crear cursor
cursor = conexion.cursor()
#---------------------------------------------------------------------------------------------------------------------------------
#crear tabla
#cursor.execute("CREATE TABLE estudiantes (email VARCHAR(100), carrera VARCHAR(100),nombre VARCHAR(100), edad INT )")
#--------------------------------------------------------------------------------------------------------------------------------
#insertar datos en la tabla
#cursor.execute("INSERT INTO estudiantes VALUES ('Alvaro@gmail.com', 'Ciencia de datos', 'Alvaro Gualix', 34)")
#guardar cambios en la tabla
#conexion.commit()
#--------------------------------------------------------------------------------------------------------------------------------
#leer contenido de la tabla
#cursor.execute("SELECT * FROM estudiantes")
#usuarios = cursor.fetchone() #Solo muestra el primero
#print(usuarios)
#--------------------------------------------------------------------------------------------------------------------------------
#introducir multiples datos
usuarios = [
    ("Javi@gmail.com", "Ciencia de datos", "Javier Navarro", 32),
    ("anna@gmail.com", "Ciencia de datos", "Anna Stroevich", 33),
    ("luis@gmail.com", "Ciencia de datos", "Luis errejon", 30),
    ("Cris@gmail.com", "Ciencia de datos", "Cristina Sanchez", 34)
]
#cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", usuarios)
#conexion.commit()
cursor.execute("SELECT * FROM estudiantes")
usuarios = cursor.fetchall() #muestra todos
for u in usuarios:
    print(u)
#print(usuarios)
#--------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------
#cerrar conexion BBDD
conexion.close()