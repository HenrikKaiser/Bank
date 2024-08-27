import sqlite3

def startdb():
    db  = sqlite3.connect("D:/PycharmProjects/Bank/bank.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS userinfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20),
    bank VARCHAR(20)
    );""")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS currbalance (
    day INTEGER,
    month INTEGER,
    year INTEGER,
    hour INTEGER,
    minute INTEGER,
    userid INTEGER, 
    balance INTEGER DEFAULT 0,
    FOREIGN KEY(userid) REFERENCES userinfo(id)
    );""")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS transactions (
            day INTEGER,
            month INTEGER,
            year INTEGER,
            hour INTEGER,
            minute INTEGER,
            transactor INTEGER, 
            receiver INTEGER,
            amount INTEGER,
            FOREIGN KEY(transactor) REFERENCES userinfo(id)
            FOREIGN KEY(receiver) REFERENCES userinfo(id) 
    );""")
    db.commit()
    db.close()







