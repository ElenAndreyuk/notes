import model
import view


def button_click():
    while True:
        command = view.start_selection()
        notes = model.extract_csv()
        if command == 1:
            note = view.create_note()
            # note.update(['ID', str(len(notes) + 1)])
            id = len(notes)+1
            note.update({'ID': id})
            notes.append(note)
            model.write_csv(notes)
            view.confirm()
        elif command == 2:
            note = model.search_for_id(view.get_id(), notes)
            view.print_note(note)
            model.write_csv(notes)
            view.confirm()
        elif command == 3:
            start_date = view.get_date()
            stop_date = view.get_date()
            result = model.sort_for_date(start_date, stop_date, notes)
            for note in result:
                view.print_note(note)
            model.write_csv(notes)
            view.confirm()
        elif command == 4:
            id = view.get_id()
            note = model.search_for_id(id, notes)
            view.print_note(note)
            notes.pop(note)
            note = view.create_note()
            note.update(['ID', len(notes) + 1])
            notes.append(note)
            model.write_csv(notes)
            view.confirm()
        elif command == 5:
            id = view.get_id()
            model.delete_for_id(id, notes)
            model.write_csv(notes)
            view.confirm()
        elif command == 6:
            for note in notes:
                view.print_note(note)
            model.write_csv(notes)
            view.confirm()
        else:
            return

