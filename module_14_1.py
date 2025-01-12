# Загрузка библиотек
import sqlite3
import random

# Создадим базу
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,n
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполним базу согласно задания
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?) ",
#                    (f'user{i}', f'examle{i}@gmail.com', i * 10, 1000))

# установим баланс каждой второй записи в 500
# cursor.execute("UPDATE Users SET balance = 500 WHERE id%2 != 0")

# Удалим каждую третью запись начиная с первой
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# Сделаем выборку всех записей (id не включать) возраст 60 исключим
cursor.execute("SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.commit()
connection.close()
