class Person:
 
    def __init__(self, name, phone_num):
        self.name = name
        self.phone_num = phone_num

    def get_name(self):
        return self.name
    
    def get_phone_num(self):
        return self.phone_num
    
class PhoneBook:

    def __init__(self):
        self.phone_book = {}

    def add_contact(self, person):
        self.phone_book[person.get_name()] = person.get_phone_num()

    def get_contact(self, name):
        if name in self.phone_book.keys():
            return self.phone_book[name]
        else:
            return None
    
    def update_contact(self, name, phone_num):
        if name in self.phone_book.keys():
            self.phone_book[name] = phone_num
        else:
            return None
        
    def delete_contact(self, name):
        if name in self.phone_book.keys():
            self.phone_book.pop(name)
        else:
            return None
        
phonebook = PhoneBook()
person = Person("John Doe", "123-456-7890")
person2 = Person("Alice Bob", "0987654321")
phonebook.add_contact(person)
print(phonebook.phone_book)
phonebook.update_contact("John Doe", "987-654-3210")
print(phonebook.phone_book)
