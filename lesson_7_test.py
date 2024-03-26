# СУБД - Система Управления Базой Данных
# БД - База Данных
# Перед началом не забудьте скачать SQLite и SQLite Viewer(если вы не скачали на уроке P.S: Бакай я на уроке показывал обязательно посмотри запись)
# CRUD - Create, Read, Update, Delete


import sqlite3

connect = sqlite3.connect("test.db")
cursor = connect.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
#                id INTEGER PRIMARY KEY,
#                name VARCHAR(100) NOT NULL,
#                surname VARCHAR(100) NOT NULL,
#                age INTEGER NOT NULL,
#                email TEXT NOT NULL,
#                balance DOUBLE (8,2) DEFAULT 0.0,
#                props VARCHAR (20) NOT NULL,
#                is_active BOOLEAN DEFAULT FALSE
# );
# """)

"""
INTEGER - REAL

BLOB - бинарные данные 

"""

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               login TEXT,
               password TEXT,
               cash BIGINT
)""")

connect.commit()

users_login = input("Введите логин: ")
users_password = input("Введите пароль: ")

cursor.execute("SELECT login FROM users")
if cursor.fetchone() is None:
    cursor.execute(f"INSERT INTO users VALUES (?, ?, ?)", (users_login, users_password, 0))
else:
    print("Такая запись существует")