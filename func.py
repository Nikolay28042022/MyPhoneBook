import csv  # Импортируем модуль csv для работы с CSV-файлами

def create_table_date():    # Функция создает файл date.csv и создает в таблице данных заголовки.
    with open('date.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)  # Создаем объект writer для записи в CSV-файл
        writer.writerow(['Last Name', 'First Name', 'Phone number', 'Comment'])  # Записываем заголовки таблицы в файл

                        
def open_table_date():
    try:
        with open('date.csv', 'r', newline='', encoding='UTF-8') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Файл 'date.csv' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



def add_date(): # Функция добавляет новый контакт 
    date_str = input("Введите Фамилию, Имя, Номер телефона, Комментарии через пробел : ")
    date_list = date_str.split()  # Разбиваем строку на список, используя пробел в качестве разделителя

    with open('date.csv', 'a', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(date_list)



def search_date():  # Функция ищет контакт по введенному слову или номеру.
    ''' 
В первой строке тела цикла используется выражение-генератор (generator expression) в сочетании с функцией any().
Давайте разберем, что происходит:
    for field in row: Этот фрагмент перебирает все элементы в текущей строке (row) файла.

    search_word.lower() in field.lower(): Это проверяет, содержится ли введенное слово (приведенное к нижнему регистру) 
в текущем поле строки файла (также приведенном к нижнему регистру). Мы используем .lower(), чтобы сделать сравнение 
без учета регистра.

    any(...): Это встроенная функция Python, которая возвращает True, если хотя бы один элемент в переданном ей итерируемом 
объекте является истинным. В данном случае, она возвращает True, если найдено совпадение в хотя бы одном поле текущей строки.

Таким образом, если в текущей строке найдено хотя бы одно поле, содержащее введенное слово (с учетом или без учета регистра),
условие if будет истинным, и программа выведет строку с найденным контактом.
    '''
    search_word = input('Введите слово или номер для поиска контакта: ')
    
    with open('date.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Пропускаем первую строку, так как это заголовки

        # Ищем контакты в каждой строке файла
        for row in reader:
            if any(search_word.lower() in field.lower() for field in row):
                print(', '.join(row))  # Выводим найденный контакт в виде строки




# def open_table_date():
#     try:
#         with open('date.csv', 'r', newline='', encoding='UTF-8') as file:
#             for line in file:
#                 print(line)
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")


