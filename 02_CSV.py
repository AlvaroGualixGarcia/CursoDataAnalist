#leer csv e insertarlo en la BD
import sqlite3 as sql
import csv
conexion = sqlite3.connect(r"C:Users\Alvar\documents\ejemplo.db")
cursor = conexion.cursor()
archivo = open(r"ruta a tu csv")
filas = csv.readder(archivo)
cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", filas)
cursor.execute("SELECT * FROM estudiantes")
print(cursor.fetchall())
conexion.commit()
conexion.close()
