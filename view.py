from datetime import datetime
import emoji


def start_selection():
    print("\n" + "=" * 30)
    print(emoji.emojize('Python is :thumbs_up:'))
    print('выберите пункт меню')
    print('1 - создать заметку;')
    print('2 - поиск заметки по ID;')
    print('3 - фильтровать по дате;')
    print('4 - редактировать заметку по ID;')
    print('5 - удалить заметку по ID;')
    print('6 - показать все заметки.')
    print('7 - выход.')
    command = int(input(": "))
    if 0 < command < 7:
        return command
    elif command == 7:
        return False
    else:
        print('ошибка ввода')


def confirm():
    print("успешно выполнено ")


def create_note():
    title = input('введите заголовок: ')
    data = input('введите данные: ')
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    # note = {'title': title, 'data': data, 'date': date}
    note = {title: 'title', data: 'data', date: 'date'}
    return note


# def print_note(note):
#     try:
#         print('+++++++++++')
#         print(note.get['title'])
#         print(note.get['ID'])
#         print(note.get['data'])
#         print(note.get['date'])
#     except:
#         print('error')


def print_note(note):
    print(note.values())

def get_id():
    id = int(input('введите ID: '))
    return id


def get_date():
    date = input('Введите дату в формате dd.mm.yyyy: ')
    return date

# def show_all(x):
#     x = [i.rstrip() for i in x]
#     for i in x:
#         if (x.index(i) + 1) % 4 == 0:
#             print(i, )
#         else:
#             print(i, end=' ')
#
#

#
#
# def search_surname(b):
#     y = input('введите фамилию: ')
#     for i in range(0, len(b), 4):
#         if y in b[i]:
#             print(b[i], b[i + 1], b[i + 2], b[i + 3])
#             break
#     else:
#         print('не найдено')
#
#
# def search_number(d):
#     list_cont = d
#     z = input('введите номер телефона: ')
#     for i in range(len(list_cont)):
#         if z in list_cont[i]:
#             print(list_cont[i], list_cont[i - 1], list_cont[i - 2], list_cont[i + 1])
#             break
#     else:
#         print('не найдено')
#
#
