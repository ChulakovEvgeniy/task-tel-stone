from .text import *
from model import PhoneBook,Contact


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def show_contacts(book: PhoneBook):
    if book.contacts:
        print('\n' + '=' * 67)
        for contact in book.contacts:
            print(contact)
        print('=' * 67 + '\n')
    else:
        print(book_error)


def input_contact(message: str) -> dict[str, str]:
    print(message)
    new = Contact(input(new_contact[0]),input(new_contact[1]),input(new_contact[2]))
    return new


def input_return(message: str) -> str:
    return input(message)
