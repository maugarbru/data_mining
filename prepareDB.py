import sqlite3
from util import imprimir_error, database

connection = sqlite3.connect(database)

# Crear la tabla de commodities
try:
    connection.execute(
        """CREATE TABLE commodity (
            ticker          TEXT PRIMARY KEY,
            fuel_name       TEXT NOT NULL UNIQUE
        )"""
    )
    print("SUCCESS: Se creo la tabla commodity")
except sqlite3.Error as er:
    imprimir_error(er)

# Crear la tabla de transaction_records
try:
    connection.execute(
        """CREATE TABLE transaction_record (
            codigo          INTEGER PRIMARY KEY,
            date            TEXT NOT NULL,
            open_value      REAL NOT NULL,
            high            REAL NOT NULL,
            low             REAL NOT NULL,
            close_value     REAL NOT NULL,
            volume          REAL NOT NULL,
            commodity       TEXT,
            FOREIGN KEY(commodity) REFERENCES commodity(ticker)
        )"""
    )
    print("SUCCESS: Se creo la tabla transaction_record")
except sqlite3.Error as er:
    imprimir_error(er)

connection.close()
