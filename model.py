import csv
from pathlib import Path


def write_csv(notes):
    path = 'notes.csv'
    with open(path, 'w', encoding='utf-8') as csv_file:
        # with open(path, 'a') as data:
        for note in notes:
            for line in note:
                csv_file.write(line + ';')
            csv_file.write('\n')
    csv_file.close()


# def write_csv(notes):
#     with open('eggs.csv', 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=' ',
#                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#         spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# def extract_csv():
#     path = 'notes.csv'
#     notes = []
#     try:
#         with open(Path.cwd() / path, 'r', encoding='utf-8') as fin:
#             csv_reader = csv.reader(fin)
#             id = 0
#             for row in csv_reader:
#                 temp = {row[0]: 'title', row[1]: 'data', row[2]: 'date', id+1 : 'ID"'}
#                 # temp = {"id": id + 1, "title": row[0], "data": row[1], "date": row[3]}
#                 notes.append(temp)
#     except:
#         print("----")
#     return notes


def extract_csv():
    try:
        notes = []
        file = open("notes.csv", "r", encoding='utf-8')
        temp = file.read().strip().split("\n")
        for i in temp:
            split_n = i.split(';')
            note = {split_n[0]: 'title', split_n[1]: 'data', split_n[2] : 'date', split_n[3]: 'ID'}
            notes.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
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

    # def save(self, notepad):
    #     data = pd.DataFrame([note.__dict__ for note in notepad])
    #     data.to_csv(self.file_name, index=False)
