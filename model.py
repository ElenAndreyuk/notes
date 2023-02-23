import csv
from pathlib import Path


def write_csv(notes):
    path = 'notes.csv'
    with open('notes.csv', 'a', encoding='utf-8') as data:
    # with open(path, 'a') as data:
        for note in notes:
            for line in note:
                data.write(line + ',')
            data.write('\n')
    data.close()
def extract_csv():
    path = 'notes.csv'
    notes = []
    with open(Path.cwd() / path, 'r', encoding='utf-8') as fin:
    # with open(Path.cwd() / path, 'r') as fin:
        csv_reader = csv.reader(fin)
        id = 0
        try:
            for row in csv_reader:
                temp = {"id": row[0], "title": row[1], "data": row[2], "date": row[3]}
                notes.append(temp)
        except:
            print("----")
    return notes


def search_for_id(id, notes):
    for note in notes:
        if id == note.get('ID'):
            return note
    return None


def delete_for_id(id, notes):
    for note in notes:
        if id == note.get('ID'):
            notes.pop(note)
    return notes


def sort_for_date(start_date, stop_date, notes):
    for note in notes:
        result = []
        date = note.get('date')
        if start_date <= date <= stop_date:
            result.append(note)
    return result



