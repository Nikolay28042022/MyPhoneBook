import func
import csv

while True:
    action = input('''
        Какое действие Вы хотите произвести?
        Введите соответствующую цифру.
        1 - Просмотр контактов
        2 - Поиск контакта
        3 - Добавление контакта
        4 - Изменение контакта
        5 - Удаление контакта
        6 - Выход
    ''')

    try:
        action = int(action)
    except ValueError:
        print("Введите корректное число.")
        continue

    if action == 1:
        func.open_table_date()
        break
    elif action == 2:
        func.search_date()
        break
    elif action == 3:
        func.add_date()
        break
    elif action == 6:
        print("Выход из программы.")
        break
    else:
        print("Введите корректное число из списка.")







