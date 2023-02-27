import csv
from pathlib import Path


def write_csv(notes):
    path = 'notes.csv'
    with open(path, 'w', encoding='utf-8') as csv_file:
        # with open(path, 'a') as data:
        for note in notes:
            csv_file.write(note['title'] + ';' + note['data'] + ';' + note['date'])
            # csv_file.write('\n')
    csv_file.close()


def extract_csv():
    path = 'notes.csv'
    data = open(path, 'r', encoding='utf-8')
    notes = []
    id = 0
    try:
        for row in data:
            id = id + 1
            line = row.strip('\n').split(';')
            note = {'title': line[0], 'data': line[1], 'date': line[2], 'ID': id}
            notes.append(note)
    except:
        print('заметок нет')
    data.close()
    return notes


def search_for_id(id, notes):
    for note in notes:
        if id == str(note['ID']):
            return note
    return


def delete_for_id(id, notes):
    for note in notes:
        if id == str(note['ID']):
            notes.pop(note)
    return notes


def sort_for_date(start_date, stop_date, notes):
    for note in notes:
        result = []
        date = note['date']
        if start_date <= date <= stop_date:
            result.append(note)
    return result

    # def save(self, notepad):
    #     data = pd.DataFrame([note.py.__dict__ for note.py in notepad])
    #     data.to_csv(self.file_name, index=False)
