import sqlite3
from DB import main

def load_row(name, table):
    main.startdb()
    db = sqlite3.connect("D:/PycharmProjects/Bank/bank.db")
    cursor = db.cursor()
    match table:
         case "userinfo":
            cursor.execute(f"""
            SELECT * FROM userinfo
            """)
         case "currbalance":
             cursor.execute(f"""
             SELECT * FROM currbalance
             WHERE userid in (
             SELECT id FROM userinfo
             WHERE name = '{name}'
             );
             """)
         case _:
            print("Enter a valid choice!")
            exit()
    db.commit()
    print(cursor.fetchall())
    db.close()