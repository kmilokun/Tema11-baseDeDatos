from functionsdb import *

DB = 'alumnos.db'


def menu():
    print('¿Qué accion desea realizar?')
    print('1. Ingresar alumnos a la base de datos.')
    print('2. Buscar alumno en la base de datos.')
    print('3. Salir.')
    comand = int(input('>>>'))

    match comand:
        case 1:
            print('\n'*100)
            insert_many_user(DB)
        case 2:
            print('\n' * 100)
            buscar_nombre(DB)
        case 3:
            quit()
        case _:
            print('\n' * 100)
            print('Comando no encontrado')
            menu()


def main():
    menu()


if __name__ == '__main__':
    # createDB(DB)
    # create_table(DB, 'Alumnos')
    # insert_many_user(DB)
    main()
