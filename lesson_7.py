# СУБД - Система Управления Базой Данных
# БД - База Данных
# Перед началом не забудьте скачать SQLite и SQLite Viewer(если вы не скачали на уроке P.S: Бакай я на уроке показывал обязательно посмотри запись)
# CRUD - Create, Read, Update, Delete


import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection("school.db")

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

def create_student(conn, student: tuple):
    sql = '''INSERT INTO students
    (full_name, mark, hobby, birth_date, is_passed)
    VALUES (?, ?, ?, ?, ?);'''
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()

def update_students_mark(conn, id, new_mark):
    sql = '''UPDATE students SET mark = ? WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_mark, id))
    conn.commit()

# def dop_h_w(conn):
#     sql = '''SELECT * FROM students WHERE mark > 3; '''
#     cursor = conn.cursor()
#     orders = cursor.execute(sql).fetchall()
#     for order in orders:
#         print(order)

def delete_student(conn, id: int):
    sql = '''DELETE FROM students WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()

sql_create_table = """
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (100) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_passed BOOLEAN DEFAULT FALSE
);
"""
# IF NOT EXISTS = создать таблицу если такой не существует
# AUTOINCREMENT = сам сгенерирует айди
# VARCHAR = текст с ограниченной длиной(str)
# NOT NULL = обязательное поле
# DOUBLE = float
# TEXT = текст без ограничений(str)
# DEFAULT NULL = необязательное поле

connection = create_connection("school.db")
if connection:
    print("Успешное соединение!")
    create_table(connection, sql_create_table)
    delete_student(connection, 1)
    update_students_mark(connection, 3, 80)
    # dop_h_w(connection)
    # create_student(connection, ("Bakai", 75.53, "Typing", "2009-01-01", True))
    # create_student(connection, ("Nurai", 95.00, "Voleyball", "07-01-2008", True))
