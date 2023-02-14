import csv
from pathlib import Path
import main


def extract_cvs():
    path = main.path
    notes = []
    # with open(Path.cwd() / path, 'r', encoding='utf-8') as fin:
    with open(Path.cwd() / path, 'r') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {"id": row.index() + 1, "title": row[1], "data": row[2], "date": row[3]}
            notes.append(temp)
    return notes


def search_for_id(id, notes):
    for note in notes:
        if id == note.get('ID'):
            return note
    return


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


def write_csv(notes):
    # with open('notes.csv', 'a', encoding='utf-8') as data:
    with open(path, 'a') as data:
        for line in notes:
            data.write(line + '\n')
    # data = open('phones.txt', 'a', encoding='utf-8')
    # data.write('\n line 2\n')
    data.close()
