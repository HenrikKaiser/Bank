import sqlite3
from DB import main
import datetime

def save_row(name, bank, table):
    main.startdb()
    db = sqlite3.connect("D:/PycharmProjects/Bank/bank.db")
    cursor = db.cursor()
    match table:
        case "userinfo":
            cursor.execute(f"""
            INSERT INTO userinfo(
            name,
            bank)
            VALUES (
            '{name}',
            '{bank}'
            );
            """)
        case "currbalance":
            date = datetime.datetime.now()
            day = date.day
            month = date.month
            year = date.year
            hour = date.hour
            minute = date.minute
            try:
                cursor.execute(f"""SELECT BALANCE FROM currbalance
                                 WHERE userid in (
                                 SELECT id FROM userinfo
                                 WHERE name = '{name}'
                                 )  
                                 ORDER BY column DESC LIMIT 1;""")
                temp = cursor.fetchall()
            except sqlite3.OperationalError:
                temp = 0
            while True:
                try:
                    amount = int(input("Enter the amount: "))
                    break
                except ValueError:
                    print("Enter a number!")
            balance = temp + amount
            cursor.execute(f"""
                SELECT id FROM userinfo
                WHERE name = '{name}';
                """)
            if not cursor.fetchall():
                print("NO")
                cursor.execute(f"""
                            INSERT INTO userinfo(
                            name,
                            bank)
                            VALUES (
                            '{name}',
                            '{bank}'
                            );
                            """, )
                cursor.execute(f"""
                                SELECT id FROM userinfo
                                WHERE name = '{name}'
                                """)
            userid =  cursor.fetchall()
            cursor.execute(f"""
                            INSERT INTO currbalance
                            VALUES (
                            {day}, {month}, {year}, {hour}, {minute}, {userid}, {balance}
                            );
                            """)
    db.commit()
    db.close()