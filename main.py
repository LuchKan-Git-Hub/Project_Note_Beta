# import time
import time
# the note
notes = dict()


# function add new note
def add_note(description, key):
    global notes
    notes[description] = key
    print(f"note added {description}: {key}!")


# function show all notes
def show_notes():
    if len(notes) == 0:
        print("there is no notes yet.")
        time.sleep(1)
    else:
        for number_loop, (title, text) in enumerate(notes.items(), start=1):  # `enumerate` with a starting index of 1
            print(f"{number_loop}. {title}: {text}")
            time.sleep(3)


# function delete notes
def delete_note(title):
    global notes
    if title in notes:
        del notes[title]
        print("note deleted!")
    else:
        print("note not found!")


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
        print("4. quit (deletes all notes data!)")
        choice = input("Choose an option: ")

        # if chose add note
        if choice == "1":
            note_title = input("Name of the note: ")
            note_text = input("Name of the keyword: ")
            add_note(note_title, note_text)
            time.sleep(1)

        # if chose show notes
        elif choice == "2":
            show_notes()

        # if chose delete note
        elif choice == "3":
            input_title = input("Name of the note: ")
            delete_note(input_title)
            time.sleep(1)

        # if chose to quit exit
        elif choice == "4":
            break

        # if invalid choice
        else:
            print("try again no option like that.")
            time.sleep(1)


# starting the main function
main()
exit(319)
