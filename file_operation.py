import pandas


def extract_csv():
    notes_data = pandas.read_csv('notes.csv')
    print('******')
    print(notes_data)
