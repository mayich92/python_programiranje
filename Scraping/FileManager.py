import os

# TODO
# provjera postoji li putanja +
# otvaranje fh +
# zapis podataka u datoteku +
# nadodavanje podataka u datoteku +
# čitanje iz datoteke +
# zatvaranje fh +

# class CustomError(Exception):
#     pass

def path_exists(path):
    '''Funkcija koja vraća True ili False, ovisno o tome je li ulazna putanja postojeća'''
    return os.path.exists(path)

def open_file(path, mode, encoding_arg='utf-8'):
    if path_exists(path) or mode == 'w':
        f = open(path, mode, encoding=encoding_arg)
        return f
    else:
        # raise CustomError('Putanja ne postoji!')
        raise ValueError('Putanja ne postoji!')

def write_to_file(file_connection, data):
    try:
        file_connection.write(data)
    except Exception as ex:
        print("Dogodila se greška pri pisanju u datoteku: ", ex)
    # file_connection.close()

# def append_to_file(file_connection, data):
#     try:
#         file_connection.write(data)
#     except Exception as ex:
#         print("Dogodila se greška: ", ex)
#     # file_connection.close()

def close_file(file_connection):
    try:
        file_connection.close()
    except Exception as ex:
        print("Dogodila se greška pri pokušaju zatvaranja datoteke: ", ex)

def read_from_file(file_connection):
    try:
        data = file_connection.read()
        return data
    except Exception as ex:
        print("Dogodila se greška pri čitanju iz datoteke: ", ex)