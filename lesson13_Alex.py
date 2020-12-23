import os
from random import randint


class EmailGenerator:

    def __init__(self, file_domains, file_names):
        self.file_domains = file_domains
        self.file_names = file_names
        self.get_domains()
        self.get_names()


    def get_domains(self):
        with open(self.file_domains, 'r') as file:
            data = []
            self.domains = []
            for line in file.readlines():
                data.append(line.strip())
            for element in data:
                new_element = element.replace(".", "")
                self.domains.append(new_element)
        print(self.domains)
        print(f"len domains = {len(self.domains)}")
        return self.domains


    def get_names(self):
        with open(self.file_names, 'r') as file:
            self.names = []
            for line in file.readlines():
                self.names.append(line.split()[1])
        print(self.names)
        print(f"len names = {len(self.names)}")
        return self.names


    def generate_email(self):
        my_symbol = ""
        rand_surname = randint(0, len(self.names) - 1)
        rand_number = randint(100, 999)
        for symbol in range(randint(5, 7)):
            rand_symbol = chr(randint(97, 122))
            my_symbol += rand_symbol
        rand_domain = randint(0, len(self.domains) - 1)
        my_email = f"{self.names[rand_surname]}.{rand_number}@{my_symbol}.{self.domains[rand_domain]}"
        print(my_email)
        return my_email


email_generator = EmailGenerator("domains.txt", "names.txt")
email = email_generator.generate_email()