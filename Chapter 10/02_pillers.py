# 1. Encapsulation: Binding data and methods that operate on the data into a single unit (class).
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (Encapsulation)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f'{amount} deposited. New balance: {self.__balance}')
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'{amount} withdrawn. Remaining balance: {self.__balance}')
        else:
            print('Insufficient funds!')
    
    def get_balance(self):
        return self.__balance  # Encapsulated data accessed via method

# Creating object
account = BankAccount("Anekant", 10000)
account.deposit(2000)
account.withdraw(5000)
# print(account.__balance)  # Will throw an error (Private variable)


# 2. Abstraction: Hiding unnecessary details and showing only relevant information.
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")
    
# Creating object
my_car = Car()
my_car.start_engine()


# 3. Inheritance: One class acquiring properties of another.
# i. Single Inheritance
# ii. Multiple Inheritance
# iii. Multilevel Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_details(self):
        print(f'Employee: {self.name}, Salary: {self.salary}')
    
class Manager(Employee):  # Inheriting from Employee
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def show_details(self):
        print(f'Manager: {self.name}, Salary: {self.salary}, Department: {self.department}')

# Creating objects
emp = Employee("Shiv", 30000)
mgr = Manager("Anekant", 50000, "IT")
emp.show_details()
mgr.show_details()


# 4. Polymorphism: A method behaving differently for different classes.
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"
    
    # p1.__add__(p2)
    # p1.__sub__(p2)
    # p1.__mul__(p2)
    # p1.__truediv__(p2)
    # p1.__floordiv__(p2)
    
    
# Function demonstrating polymorphism
def animal_sound(animal):
    print(animal.speak())

# Creating objects
cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)
