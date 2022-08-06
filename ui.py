from logger import delete_data, input_data, search_data, print_data

def interface():
    print('Доброго времени суток! Вы попали на специальную программу.\n'
          '1. Записать данные\n'
          '2. Удалить данные\n'
          '3. Поиск данных\n'
          '4. Вывести данные\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print('Неверное значение, повторите')
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        search_data()
    else:
        print_data()

interface()
