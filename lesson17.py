# Имя и фамилия и зп из файла (попробовать из бд)


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"



class Employee(Human):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self.salary = salary

    def get_paid(self):
        return f'{self.salary}'


class Manager(Employee):
    def __init__(self, name, surname, salary, muliplication_k):
        super().__init__(name, surname, salary)
        self.muliplication_k = muliplication_k

    def get_paid(self):
        return f'{self.salary * self.muliplication_k}'


class Programmer(Employee):
    def __init__(self, name, surname, salary, launguage, bonus):
        super().__init__(name, surname, salary)
        self.bonus = bonus
        self.launguage = launguage

    def get_paid(self):
        return f'{self.salary + self.bonus}'


employees = [Programmer('Anton', 'Martynov', 1000, 'python', 100),
             Manager('Kyrylo', 'Kozhemyaka', 2000, 1.2),
             Employee('Sam', 'Smith', 800)]

for e in employees:
    print(f"{e} have to be paid: {e.get_paid()}")
