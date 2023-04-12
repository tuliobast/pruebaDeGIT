import sqlite3

def crear_alumno(id, nombre, apellido):   
    conn = sqlite3.connect('bdalumnos.db',  isolation_level=None)
    cursor = conn.cursor() 
    query = 'INSERT INTO alumnos(id, Nombre, Apellido) VALUES(?, ?, ?)'
    cursor.execute(query, (id, nombre, apellido))
    cursor.close()
    conn.close()

crear_alumno(1, 'tulio', 'bastidas')
crear_alumno(2, 'ale', 'garcia')
crear_alumno(3, 'zuhe', 'alvarez')
crear_alumno(4, 'pepe', 'muleiro')
crear_alumno(5, 'jose', 'benitez')
crear_alumno(6, 'adrian', 'gonzalez')
crear_alumno(7, 'julio', 'andrade')
crear_alumno(8, 'carlos', 'navarr')

def ver_alumno():
    conn = sqlite3.connect('bdalumnos.db')
    cursor = conn.cursor() 
    query = 'SELECT * FROM alumnos'

    rows = cursor.execute(query)
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

ver_alumno()