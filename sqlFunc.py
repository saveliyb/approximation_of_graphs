import sqlite3
import traceback
import sys
import json

def create_table_sql():
    try:
        sqlite_connection = sqlite3.connect('sqlite_create_tables.sql')
        sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    coefficients TEXT NOT NULL
                                    );'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        pass
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def write_sql(name, lst):
    try:
        data = json.dumps(lst)
        # print(j, type(j))
        sqlite_connection = sqlite3.connect('sqlite_create_tables.sql')
        cursor = sqlite_connection.cursor()
        # print("База данных подключена к SQLite")
        sqlite_insert_query = """INSERT INTO sqlitedb_developers 
                                (name, coefficients) VALUES (?, ?)"""

        count = cursor.execute(sqlite_insert_query, [name, data])
        sqlite_connection.commit()
        # print("Запись успешно вставлена в таблицу sqlitedb_developers ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        pass
        # exc_type, exc_value, exc_tb = sys.exc_info()
        # print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")


def read_Sql():
    try:
        sqlite_connection = sqlite3.connect('sqlite_create_tables.sql')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # print(records)

        cursor.close()

    except sqlite3.Error as error:
        pass
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print(records)
            return records
# create_table_sql()
# write_sql('amogus', 1, 9, 5)
# print(read_Sql())
