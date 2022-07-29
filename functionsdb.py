import sqlite3 as sq
from main import *

def createDB(filename):
    conn = sq.Connection(filename)
    conn.commit()
    conn.close()


def create_table(filename, tablename):
    conn = sq.Connection(filename)
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE {tablename}(
        id INTEGER PRIMARY KEY ,
        nombre TEXT NOT NULL, 
        apellido TEXT NOT NULL
        );"""
    )
    conn.commit()
    conn.close()


def insert_user(k, nombre, apellido, filename):
    conn = sq.Connection(filename)
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO Alumnos(id, nombre, apellido)
        VALUES ({k}, "{nombre}", "{apellido}");
        """
    )
    conn.commit()
    conn.close()


def insert_many_user(filename):
    conn = sq.Connection(filename)
    cursor = conn.cursor()
    query = 'SELECT id FROM Alumnos '
    rows = cursor.execute(query)
    lst = list(rows)
    leng = len(lst)
    if leng == 0:
        index = 1
    else:
        l = list(map(int, max(lst)))
        index = l[0] + 1
        conn.close()

    n = int(input('Numero de ingresos que va a realizar: '))
    for i in range(index, index + n):
        nombre = input('Nombre:')
        apellido = input('Apellido: ')
        insert_user(i, nombre, apellido, filename)


def verificar(user, passwrd, filename):
    conn = sq.Connection(filename)
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username="{user}" AND password="{passwrd}"'
    rows = cursor.execute(query)
    data = rows.fetchone()

    conn.close()

    if data is None:
        return False
    return True


def buscar_nombre(filename):
    nombre = input('Nombre del usuario que desea buscar: ')
    conn = sq.Connection(filename)
    cursor = conn.cursor()

    query = f'SELECT id, nombre, apellido FROM Alumnos WHERE nombre="{nombre}"'
    rows = cursor.execute(query)
    data = rows.fetchone()
    if data is not None:
        print('id:', data[0])
        print('Nombre:', data[1])
        print('Apellido:', data[2])
    else:
        print('Usuario no encontrado')
        buscar_nombre(filename)

    cursor.close()
    conn.close()


def main():
    pass


if __name__ == '__main__':
    main()
