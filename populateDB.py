import sqlite3
import csv
from util import imprimir_error, commodities, database

connection = sqlite3.connect(database)

# Popular la tabla de commodities con los conocidos del dataset
try:
    contador = 0
    for commodity in commodities:
        connection.execute(
            "INSERT INTO commodity(ticker,fuel_name) values (?,?)",
            (commodity[0], commodity[1]),
        )
        contador += 1
    connection.commit()
    print("SUCCESS: Datos insertados en commodity")
    print("Cantidad de datos insertados: ", contador)
except sqlite3.Error as er:
    imprimir_error(er)

# Popular las transaction_records con el csv del dataset
try:
    with open("all_fuels_data.csv", newline="") as File:
        reader = csv.reader(File)
        contador = 0
        for row in reader:
            connection.execute(
                "INSERT INTO transaction_record (date, open_value, high, low, close_value, volume, commodity) values (?,?,?,?,?,?,?)",
                (row[2], row[3], row[4], row[5], row[6], row[7], row[0]),
            )
            contador += 1
        connection.commit()
        print("SUCCESS: Datos insertados en transaction_record")
        print("Cantidad de datos insertados: ", contador)
except sqlite3.Error as er:
    imprimir_error(er)

connection.close()
