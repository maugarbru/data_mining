import traceback
import sys

# Nombre de la base de datos
database = "fuels.db"

# Commodities identificados del dataset segun el diccionario de datos
commodities = [
    ["CL=F", "Crude_Oil"],
    ["NG=F", "Natural_Gas"],
    ["HO=F", "Heating_Oil"],
    ["BZ=F", "Brent_Crude_Oil"],
    ["RB=F", "RBOB_Gasoline"],
]


# Funcion para imprimir los errores de SQL
def imprimir_error(error):
    print("******************")
    print("SQLite error: %s" % (" ".join(error.args)))
    print("SQLite traceback: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("******************")
