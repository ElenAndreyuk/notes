from datetime import datetime
import emoji


def start_selection():
    print("\n" + "=" * 30)
    print('выберите пункт меню')
    print('1 - создать заметку ' + emoji.emojize(':pen:') + ';')
    print('2 - поиск заметки по ID ' + emoji.emojize(':magic_wand:') + ';')
    print('3 - фильтровать по дате ' + emoji.emojize(':calendar:') + ';')
    print('4 - редактировать заметку по ID ' + emoji.emojize(':reverse_button:') + ';')
    print('5 - удалить заметку по ID ' + emoji.emojize(':toilet:') + ';')
    print('6 - показать все заметки ' + emoji.emojize(':notebook:') + ';')
    print('7 - выход ' + emoji.emojize(':hand_with_fingers_splayed:') + '.')
    command = int(input(": "))
    if 0 < command < 7:
        return command
    elif command == 7:
        return False
    else:
        print('ошибка ввода')


def confirm():
    print(emoji.emojize(':OK_hand:'))


def create_note():
    title = input('введите заголовок: ')
    data = input('введите данные: ')
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    note = {'title' : title, 'data': data, 'date': date}
    return note


def print_note(note):
    print(note['ID'])
    print(note['title'].center(20))
    print(note['data'])
    print(note['date'])
    print('-------------------')


def get_id():
    id = int(input('введите ID: '))
    return id


def get_date():
    date = input('Введите дату в формате dd.mm.yyyy: ')
    return date


def not_find():
    print('не нашлось')
