import sqlite3
from DB import main
import loaddb
import savedb
def dbcontroll():
    choice = input("save or load?: ")
    match choice:
        case "1":
            name = input("Choose a name: ")
            bank = input("Choose your bank: ")
            table = input("choose your table: ")
            savedb.save_row(name, bank, table)
        case "2":
            name = input("Choose a name: ")
            table = input("choose your table: ")
            loaddb.load_row(name, table)
        case _:
            print("Enter a valid choice")
            dbcontroll()

dbcontroll()

