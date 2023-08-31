import sqlite3
from util import imprimir_error, database

connection = sqlite3.connect(database)

# Consultar la tabla de commodities
try:
    cursor = connection.execute("SELECT ticker,fuel_name FROM commodity")
    print("---")
    print("SUCCESS: Datos obtenidos de commodity")
    for fila in cursor:
        print(fila)
except sqlite3.Error as er:
    imprimir_error(er)

# Consultar la tabla de transaction_records
try:
    cursor = connection.execute("""
        SELECT 
            ticker, fuel_name, date, MIN(low)
        FROM transaction_record 
        INNER JOIN commodity ON commodity.ticker = transaction_record.commodity
        GROUP BY ticker
    """)
    print("---")
    print("SUCCESS: Datos obtenidos de transaction_record")
    for fila in cursor:
        print(fila)
except sqlite3.Error as er:
    imprimir_error(er)

connection.close()