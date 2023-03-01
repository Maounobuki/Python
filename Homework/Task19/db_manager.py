
from copy import deepcopy

class PhoneBook():

    def __init__(self, path = 'phone_db.txt'):
        self.path = path
        self.phone_book = []
        self.new_pb = []

    def open_file(self):

        self.phone_book = []
        with open(self.path,'r',encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {}
                new_contact['name'] = new[0]
                new_contact['phone'] = new[1]
                new_contact['comment'] = new[2]
                self.phone_book.append(new_contact)
            self.new_pb = deepcopy(self.phone_book)

    def save_file(self):

        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.new_pb = deepcopy(self.phone_book)

    def get(self):
        return self.phone_book

    def add(self, new_contact: dict):
        self.phone_book.append(new_contact)

    def change_contact(self, index: int, contact: dict):

        for key, value in contact.items():
            if value == '':
                contact[key] = self.phone_book[index-1].get(key)
        self.phone_book.pop(index-1)
        self.phone_book.insert(index-1, contact)

    def delete_contact(self, index: int):
        self.phone_book.pop(index-1)

    def comparison(self) ->bool:

        if self.new_pb == self.phone_book:
            return False
        return True

    def file_not_opened(self) ->bool:

        if self.phone_book == []:
            return True
        return False

