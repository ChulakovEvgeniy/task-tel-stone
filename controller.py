from view import menu, show_contacts, print_message, input_contact, input_return
import model
from view import text


def start():
    pb = model.PhoneBook('phones.txt')
    while True:
        choice = menu()
        match choice:
            case 1:
                pb.open_file()
                print_message(text.open_successful)
            case 2:
                pb.save_file()
                print_message(text.save_file)
            case 3:
                show_contacts(pb)
            case 4:
                new = input_contact(text.input_new_contact)
                pb.add_contact(new)
                print_message(text.contact_saved(new.name))
            case 5:
                word = input_return(text.search_word)
                result = pb.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = pb.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                pb.change(int(index), new)
                old_name = pb.contacts[int(index) - 1]
                print_message(text.contact_changed(new.name if new.name else old_name))

            case 7:
                word = input_return(text.search_word)
                result = pb.search(word)
                show_contacts(result)
                index = input_return(text.input_index_deleted)
                contact = pb.deleted(int(index))
                print_message(text.contact_deleted(contact))

            case 8:
                print()
                return print(text.exit_programm)
