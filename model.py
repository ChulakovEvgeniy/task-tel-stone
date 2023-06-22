class Contact:
    count_id = 1
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment
        self.uid = Contact.count_id
        Contact.count_id += 1

    def __str__(self):
        return f'{self.uid:>3}. {self.name:<20} {self.phone:<20} {self.comment:<20}'

    def for_search(self):
        return f'{self.name} {self.phone} {self.comment}'.lower()


class PhoneBook:

    def __init__(self, path: str):
        self.contacts: list[Contact] = []
        self.path = path

    def  open_file(self):
        if len(self.contacts) == 0:
            with open(self.path, 'r', encoding='UTF-8') as file:
                data = file.readlines()
            for contact in data:
                _, name, phone, comment, *_ = contact.strip().split(':')
                self.contacts.append(Contact(name,phone,comment))

    def add_contact(self,new: Contact):
        self.contacts.append(new)

    def search(self,word: str) -> list[Contact]:
        result = []
        for contact in self.contacts:
            if word.lower() in contact.for_search().lower():
                result.append(contact)
                break
        return result


    def change(self,index: int, new: dict[str, str]):
        for contact in self.contacts:
            if index == contact.uid:
                contact.name = new.get('name') if not new.get('name') else contact.name
                contact.phone = new.get('phone') if not new.get('phone') else contact.phone
                contact.comment = new.get('comment') if not new.get('comment') else contact.comment

        # for key, field in new.items():
        #     if field != '':
        #         self.contacts[index - 1][key] = field

    def deleted(self,index: int):
        contact = self.contacts.pop(index-1)
        return contact.name

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            for contact in self.contacts:
                file.write(f"{contact.uid}:{contact.name}:{contact.phone}:{contact.comment}\n")
