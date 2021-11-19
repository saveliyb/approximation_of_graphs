import sqlite3
import json


def create_table_sql():
    try:
        sqlite_connection = sqlite3.connect("sqlite_create_tables.sql")
        sqlite_create_table_query = """CREATE TABLE sqlitedb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    coefficients TEXT NOT NULL,
                                    x_belong TEXT NOT NULL
                                    );"""

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error:
        pass
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def write_sql(name, lst, x):
    try:
        data = json.dumps(lst)
        x_belongs = json.dumps(x)
        sqlite_connection = sqlite3.connect("sqlite_create_tables.sql")
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """INSERT INTO sqlitedb_developers 
                                (name, coefficients, x_belong) VALUES (?, ?, ?)"""

        cursor.execute(sqlite_insert_query, [name, data, x_belongs])
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error:
        pass

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def read_Sql():
    try:
        sqlite_connection = sqlite3.connect("sqlite_create_tables.sql")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        cursor.close()

    except sqlite3.Error:
        pass
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            return records
