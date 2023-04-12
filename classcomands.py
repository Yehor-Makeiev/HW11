from collections import  UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __str__(self) -> str:
        return str(self.value)


class Phone(Field):
    def __str__(self) -> str:
        return str(self.value)
    
class Birthday(Field):
    def __str__(self) -> str:
        return str(self.value)



class Record:

    def __init__(self, name: Name, phone: Phone = None, birthday:Birthday = None):
        self.name = name
        self.phones = [phone] if phone else [] 
        self.birthday = birthday 
        
    def add_phone(self, phone: Phone):
        self.phones.append(phone)
    
    def add_birthday(self, birthday):
        self.birthday.append(birthday)
        
    def change_phone(self, old_phone:Phone, new_phone:Phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone
                return f'Phone {old_phone} change to {new_phone}'
        return f'Contact has no phone {old_phone}'
         
    def delete_phone(self, phone:Phone):
        for i, p in enumerate(self.phones):
            if p.value == phone.value:
                self.phones.pop(i)
                return f'Phone {phone} deleted'

    def days_to_birthday(self):
        day_now = datetime.today()
        next_birthday_year = day_now.year
        if day_now.month > self.birthday.month or (day_now.month == self.birthday.month and day_now.day > self.birthday.day):
            next_birthday_year += 1
        next_birthday = datetime(next_birthday_year, self.birthday.month, self.birthday.day)
        days_to_birthday = (next_birthday - day_now).days
        return f"{days_to_birthday} days to {self.name} birthday"
        
        
    
    def __str__(self) -> str:
        phones = ", ".join([str(phone) for phone in self.phones])
        if self.birthday:
            return f"{phones}, Birthday: {self.birthday}"
        return f"{phones}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record


    # def __iter__(self):
    #     return self.generator()
    
    # def generator(self, n=1):
    #     """
    #     Generates representations for N records at a time.
    #     :param n: number of records to generate a representation for.
    #     """
    #     items = self.data.items()
    #     i = 0
    #     while i < len(items):
    #         yield [str(v) for k, v in items[i:i+n]]
    #         i += n 