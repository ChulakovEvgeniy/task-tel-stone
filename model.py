phone_book = []
path = 'phones.txt'


def open_file():
    if len(phone_book) == 0:
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            user_id, name, phone, comment, *_ = contact.strip().split(':')
            phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}


def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field

def deleted(index: int):
    contact = phone_book.pop(index-1)
    return contact.get('name')

def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        for contact in phone_book:
            file.write(f"{contact.get('id')}:{contact.get('name')}:{contact.get('phone')}:{contact.get('comment')}\n")
