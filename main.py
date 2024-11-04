# import things
import json as js
import time
# the note
notes = {}
# function with json
def save_notes():
    global notes
    with open("notes.json", "w") as file:
        js.dump(notes, file)
    print("notes saved!")

def update_notes():
    global notes
    with open("notes.json", "r") as file:
        notes = js.load(file)

# function add new note
def add_note(description, key):
    global notes
    notes[description] = key
    print(f"note added \"{description}: {key}\"")
    save_notes()
    print('-----------------------------')



# function show all notes
def show_notes():
    global notes
    update_notes()
    if len(notes) == 0:
        print("there is no notes yet.")
        time.sleep(1)
    else:
        for number_loop, (title, text) in enumerate(notes.items(), start=1):  # `enumerate` with a starting index of 1
            print(f"{number_loop}. {title}: {text}")
            time.sleep(0.5)
    print('-----------------------------')


# function delete notes
def delete_note(del_it):
    global notes
    update_notes()
    if del_it in notes:
        del notes[del_it]
        print(f"note named \"{del_it}\" deleted successfully!")
    elif len(notes) == 0:
        print("there is no notes yet.")
        time.sleep(0.2)
    else:
        print("note not found!")
        time.sleep(0.2)
    save_notes()
    print('-----------------------------')

# main function
def main():
    # loop for command
    while True:
        # asking what to do
        print("1. Add Note")
        time.sleep(0.5)
        print("2. Look at all notes")
        time.sleep(0.5)
        print("3. delete note")
        time.sleep(0.75)
        print("4. quit (update saves all notes and data!)")
        choice = input("Choose an option: ")

        # if chose add note
        if choice == '1':
            note_title = input("Name of the note: ")
            note_text = input("Name of the keyword: ")
            add_note(note_title, note_text)
            time.sleep(1)

        # if chose show notes
        elif choice == '2':
            show_notes()

        # if chose delete note
        elif choice == '3':
            input_del_note = input("Name of the note: ")
            delete_note(input_del_note)
            time.sleep(1)

        # if chose to quit exit
        elif choice == '4':
            break
        # if invalid choice
        else:
            print("try again no option like that.")
            time.sleep(1)


# starting the main function
if __name__ == "__main__":
    main()
exit(319)
