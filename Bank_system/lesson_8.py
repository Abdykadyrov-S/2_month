import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
               id INTEGER PRIMARY KEY,
               name VARCHAR(100) NOT NULL,
               surname VARCHAR(100) NOT NULL,
               age INTEGER NOT NULL,
               email TEXT NOT NULL,
               balance DOUBLE (8,2) DEFAULT 0.0,
               props VARCHAR (20) NOT NULL,
               is_active BOOLEAN DEFAULT FALSE
);
""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.email = None
        self.balance = 0
        self.props = None
        self.is_active = False

    def register(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        cursor.execute(f"""INSERT INTO clients (name, surname, age, email, balance, props, is_active)
                       VALUES ('{name}', '{surname}', '{age}', '{email}', 0, 7777777, True);""")
        
        connect.commit()

    def deposit(self, amount):
        cursor.execute(f"""UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance += amount

    def minus(self, amount):
        cursor.execute(f"""UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance -= amount
    
    def __str__(self):
        return f"Ваш текущий баланс: {self.balance} сом"
        
    def main(self):
        while True:
            print("Выберите действие:")
            print("1-Регистрация, 2-Полнить баланс, 3-Вывести деньги, 4-Выйти")
            command = int(input("Введите цифру: "))
            if command == 1:
                name = input("Введите ваше имя:")
                surname = input("Введите вашу фамилию:")
                age = int(input("Введите ваш возраст: "))
                email = input("Введите вашу почту: ")
                self.register(name, surname, age, email)
            elif command == 2:
                if self.email:

                    amount = int(input("Введите сумму: "))
                    self.deposit(amount)
                else:
                    print("Пройдите регистрацию!")
            elif command == 3:
                if self.email:
                    amount = int(input("Введите сумму: "))
                    self.minus(amount)
                else:
                    print("Пройдите регистрацию!")
            elif command == 4:
                break
            else:
                print("Выберите действие:")
                print("1-Регистрация, 2-Полнить баланс, 3-Вывести деньги, 4-Выйти")

if __name__ == "__main__":
    bank = Bank()
    bank.main()