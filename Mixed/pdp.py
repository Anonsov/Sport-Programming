# #
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width
# #
# #     def calculate_area(self):
# #         return self.length * self.width
# #
# #
# #     def calculate_perimeter(self):
# #         return 2 * (self.length + self.width)
# #
# #
# # rectangle1 = Rectangle(1, 3)
# # area_rect = rectangle1.calculate_area()
# # perimetr_rect = rectangle1.calculate_perimeter()
# # print(f"area {area_rect}: perimetr {perimetr_rect}")
# #
# #
# #
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         return "Woof!"
#
#     def get_age_in_human_years(self):
#         return f"{self.age * 7} years in human years"
#
#
# dog1 = Dog("Buddy", 3)
# print(dog1.bark())
# print(dog1.get_age_in_human_years())
#
#
# class Car:
#     def __init__(self, make, model, year, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#
#     def drive(self, distance):
#         self.mileage += distance
#
#
#     def get_info(self):
#         return f"make: {self.make}, model: {self.model}, year: {self.year}, distance: {self.mileage}"
#
#
# car = Car("Toyota", "Camry", 2020, 15000)
# car.drive(2000)
# print(car.get_info())
#
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def introduce(self):
#         return f"Hello, my name is {self.first_name} {self.last_name}. I am {self.age} years old."
#
#
# person = Person('Akobir', 'Salomov', 17)
# print(person.introduce())
#
#
# class Account:
#     def __init__(self, balance, account_holder):
#         self.balance = balance
#         self.account_holder = account_holder
#
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#
#     def get_balance(self):
#         return self.balance
#
# my_account = Account(10000, 'Jasur')
# my_account.deposit(5000)
# my_account.withdraw(3000)
# print(my_account.get_balance())
#
#
#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def make_sound(self):
#         return "Animal makes a sound"
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__("Cat", "Felis catus")
#
#     def make_sound(self):
#         return "Meow!"
#
#     def purr(self):
#         return "Purr"
#
#
# animal = Animal("Masya", "Cat")
# cat = Cat()
# print(animal.make_sound())
# print(cat.make_sound())
#
#
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#     def get_info(self):
#         return f"name: {self.name}, age: {self.age}, grades: {self.grades}, average grade: {self.average_grade()}"
#
#
# student = Student("Jasur", 18, [3, 2, 5])
# student.add_grade(4)
# print(student.average_grade())
# print(student.get_info())
#
#
# class Library:
#     def __init__(self, name, books):
#         self.name = name
#         self.books = books
#
#
#     def add_book(self, book):
#         self.books.append(book)
#
#
#     def remove_book(self, book):
#         self.books.remove(book)
#
#
#     def list_books(self):
#         return self.books
#
#
# books = Library("Akobir", ['Progs', 'Some'])
# books.add_book('Python')
# books.remove_book('Some')
# print(books.list_books())
#
#
# class Bank:
#     def __init__(self, bank_name, accounts):
#         self.bank_name = bank_name
#         self.accounts = accounts
#
#     def create_account(self, account_holder):
#         account = Account(0, account_holder)
#         self.accounts.append(account)
#
#     def get_account(self, account_holder):
#         for account in self.accounts:
#             if account.account_holder == account_holder:
#                 return account
#             else:
#                 return "It's not your account"
#
#
#     def transfer_funds(self, from_account, to_account, amount):
#         if from_account.balance >= amount:
#             from_account.withdraw(amount)
#             to_account.deposit(amount)
#             return "Transfer successful"
#         else:
#             return "Funds are not available"
#
#
#
# bank = Bank("Akobir", [])
# bank.create_account('Jasur')
# account1 = bank.get_account('Jasur')
# print(bank.transfer_funds(account1, account1, 500))
#
#
#
#

#
# class School:
#     def __init__(self, name):
#         self.name = name
#         self.teachers = []
#         self.students = []
#
#     def add_teacher(self, teacher_name):
#         self.teachers.append(teacher_name)
#
#     def add_student(self, student_name):
#         self.students.append(student_name)
#
#     def list_all(self):
#         print(f"School Name: {self.name}")
#         print("Teachers:")
#         for teacher in self.teachers:
#             print(f"- {teacher}")
#         print("Students:")
#         for student in self.students:
#             print(f"- {student}")
#
# school = School("PDP")
# school.add_student("Albert")
# school.add_student("Jasur")
# school.add_student('Akobir')
#
# school.list_all()
#
#
# class Course:
#     def __init__(self, name, instructor):
#         self.name = name
#         self.instructor = instructor
#         self.students = []
#
#
#     def add_students(self, student):
#         self.students.append(student)
#
#
#     def remove_student(self, student):
#         self.students.remove(student)
#
#
#     def list_students(self):
#         return self.students
#
# course = Course('Who', 'Who')
#
# print(course.add_students('Akobir'))
# print(course.remove_student('Akobir'))
#
# print(course.list_students())
#
#
# class Movie:
#     def __init__(self, title, director, year, rating):
#         self.title = title
#         self.director = director
#         self.year = year
#         self.rating = rating
#
#     def update_rating(self, new_rating):
#         self.rating = new_rating
#
#     def get_summary(self):
#         return f"{self.title}, directed by {self.director}, was released in {self.year} with a rating of {self.rating}."
#
#
# movie = Movie('Avatar 2', 'Camron', 2023, 8.6)
#
# print(movie.get_summary())
# print(movie.update_rating(5.4))
# print(movie.get_summary())
#
# class ShoppingCart:
#     def __init__(self):
#         self.item = {}
#
#
#     def add_item(self,name,price):
#         self.item[name] = price
#
#
#     def remove_item(self, name):
#         self.item.pop(name)
#
#
#     def calculate_total(self):
#         return self.item
#
# shop = ShoppingCart()
# shop.add_item('tomato', 3.4)
# shop.remove_item('tomato')
# print(shop.calculate_total())
#
#
# class Game:
#     def __init__(self, name, max_players):
#         self.name = name
#         self.max_players = max_players
#         self.players = []
#
#
#     def add_player(self, player_name):
#         if len(self.players) < self.max_players:
#             self.players.append(player_name)
#         else:
#             return 'limited users'
#
#
#     def remove_player(self, player_name):
#         self.players.remove(player_name)
#
#
#     def start_game(self):
#         if len(self.players) < 3:
#             return "Insufficient players"
#         else:
#             return f"Game: {self.name} started {self.players}, max: {self.max_players} "
#
#
# game = Game('Mario', 10)
# game.add_player('Albert')
# game.add_player('Akobir')
# print(game.start_game())
#
# class House:
#     def __init__(self, adress, rooms, price):
#         self.adress = adress
#         self.rooms = rooms
#         self.price = price
#     def describe(self):
#         return f'This house at {self.adress} has {self.rooms} rooms and costs ${self.price}.'
#     def apply_discount(self, discount_percentage):
#         self.price = self.price - (self.price * discount_percentage/100)
#
# house = House('Taj 8', 4, 250000)
# house.apply_discount(20)
# print(house.describe())
#
#
# class Robot:
#     def __init__(self, name, battery_level=100):
#         self.name = name
#         self.battery_level = battery_level
#
#     def charge(self):
#         self.battery_level = 100
#
#     def work(self, hours):
#         if self.battery_level >= hours * 10:
#             self.battery_level -= hours * 10
#             return f"{self.name} is working for {hours} hours. The battery level is {self.battery_level}"
#         else:
#             return f"{self.name} has run out of battery"
#
#
# robot1 = Robot("Me")
# print(robot1.work(2))
#
#
# class Trip:
#     def __init__(self, destination, distance, duration):
#         self.destination = destination
#         self.distance = distance
#         self.duration = duration
#
#     def get_speed(self):
#         return self.distance / self.duration
#
#     def update_duration(self, new_duration):
#         self.duration = new_duration
#         return f"New duration is {self.duration}"
#
#
#
# trip1 = Trip("Tsahkent", 1000, 2)
# print(trip1.get_speed())
# print(trip1.update_duration(3))
#
#
# class University:
#     def __init__(self, name, departments, students):
#         self.name = name
#         self.departments = departments
#         self.students = students
#
#     def add_department(self, department_name):
#         self.departments.append(department_name)
#
#     def enroll_students(self, students_name):
#         self.students.append(students_name)
#
#     def list_all_info(self):
#         for department in self.departments:
#             print(f" - {department}")
#         print(f"Students:")
#         for student in self.students:
#             print(f" - {student}")
#
#
# university = University("PDP", "PDP", ['Rakhim'])
# university.add_department("Computer Science")
# university.add_department("Electrical Engineering")
# university.enroll_students("Akobir")
# university.enroll_students("Jasur")
#
# class Restaurant:
#     def __init__(self, name, menu: dict):
#         self.name = name
#         self.menu = menu
#
#     def add_item(self, item, price):
#         self.menu[item] = price
#
#     def remove_item(self, item):
#         del self.menu[item]
#
#     def get_menu(self):
#         """in readable format"""
#         for item in self.menu:
#            print(f"Item: {item}, Price: {self.menu[item]}")
#
#
#
# restaurant1 = Restaurant("KFC", {"Chicken": 500, "Pizza": 800})
#
#
# restaurant1.add_item("Salad", 400)
# restaurant1.remove_item("Pizza")
# restaurant1.get_menu()



# # a = input()
# # b = input()
# # res = 'YES' if a[::-1] == b else 'NO'
# # print(res)
#
#
# # n = int(input())
# # chesses = input()
# # count_d = 0
# # count_a = 0
# # for i in chesses:
# #     if i == 'D':
# #         count_d += 1
# #     if i == 'A':
# #         count_a += 1
# #
# # if count_a > count_d:
# #     print('Anton')
# # elif count_d > count_a:
# #     print('Danik')
# # else:
# #     print('Friendship')
# #
#
# # matrix = []
# # xo, yo = 3 ,3
# # for y in range(5):
# #     el_matrix = list(map(int, input().split(' ')))
# #     matrix.append(el_matrix)
# #     for x in range(5):
# #         if el_matrix[x] == 1:
# #             res = [abs(x+1 - xo), abs(y+1 - yo)]
# #
# #
# #
# # print(sum(res))
#
# # a = input()
# # a = sorted(list(map(int, a.split('+'))))
# #
# # print('+'.join(list(map(str, a))))
#
#
# # a = 'xiaodao'
# # if len(set(a)) % 2 == 0:
# #     print('CHAT WITH HER!')
# # else:
# #     print('IGNORE HIM!')
# #
#
#
# # n = int(input())
# # i = 0
# # total = 0
#
# #
# # while i <= n:
# #     total += i
# #     i+=1
# # print(total)
#
# # n = 60
# # flag = None
# # while flag != n:
# #     a = int(input())
# #     if a == n:
# #         print('Вы угадали')
# #         break
# #     else:
# #         print('Нет')
#
# #
# # count = 0
# # while True:
# #     a = int(input())
# #     if a == 0:
# #         break
# #     if a % 2 == 0:
# #         count+=1
# #
# # print(count)
#
# #
# # a = int(input())
# # while a > 0:
# #     print(a)
# #     a -= 1
#
# #
# # a = int(input())
# # sum_digits = 0
# # while a > 0:
# #     sum_digits = sum_digits + a % 10
# #     a = a // 10
# # print(sum_digits)
# #
# # a = int(input())
# # [*res] = list(map(int, input().split(' ')))
# #
# # if 1 in res:
# #     print('HARD')
# # else:
# #     print('EASY')
# #
# # numbers = [1, 6, 8]
# # print(*numbers)
#
# # count = 0
# # a = int(input())
# # for _ in range(a):
# #     n, t = int(input()), int(input())
# #     if abs(n) - t >= 2:
# #         count+=1
# #
# # print(count)
#
# # n = int(input())
# # count_odd = 0
# # count_even = 0
# # for i in range(1, n+1, 2):
# #     count_odd += -i
# # for j in range(2, n+1, 2):
# #     count_even += j
# #
# # print(count_odd + count_even)
#
# # b = 0
# # n = int(input())
# # for i in range(1, n+1, 2):
# #     for j in range(2, n+1, 2):
# #         print(i)
#
# # arr = [1, 4, 6, 1, 1, 6]
# # arr = sorted(arr)
# # cur_cnt = 0
# # ans = 0
# # val = -1
# # for i in range(0, len(arr)):
# #     if i == 0 or arr[i] != arr[i - 1]:
# #         cur_cnt = 0
# #
# #     cur_cnt += 1
# #
# #     if(cur_cnt > ans):
# #         ans = cur_cnt
# #         val = arr[i]
# #
# #
# # print(val, ans)
#
# """
# 1. Task: Create a ProjectManagement System
# Create a Project class with:
# •  Attributes:
# o  name (string)
# o  deadline (datetime object)
# o  tasks (list of Task objects)
# •  Methods:
# o  add_task(task): Adds a Task object to the project.
# o  remove_task(task_name): Removes a task by its name.
# o  get_progress(): Returns the percentage of completed tasks.
# Create a Task class with:
# •  Attributes:
# o  name (string)
# o  status (boolean, default False for incomplete)
# •  Methods:
# o  mark_complete(): Marks the task as complete.
# Objective: Practice class relationships (composition) and calculating progress dynamically.
# """
# #
# #
# # class Task:
# #     def __init__(self, name):
# #         self.name = name
# #         self.status = False
# #
# #     def mark_complete(self):
# #         self.status = True
# #
# #
# #
# # class Project:
# #     def __init__(self, name, deadline):
# #         self.name = name
# #         self.deadline = deadline
# #         self.tasks = []
# #
# #     def add_task(self, task):
# #         self.tasks.append(task)
# #
# #     def remove_task(self, task_name):
# #         for task in self.tasks:
# #             self.tasks.remove(task)
# #             break
# #
# #     def get_progress(self):
# #         completed_tasks = 0
# #         for task in self.tasks:
# #             if task.status:
# #                 completed_tasks += 1
# #         total_tasks = len(self.tasks)
# #         progress = (completed_tasks / total_tasks) * 100
# #         return progress
# #
# #
# #
# # project = Project("Qadam", "24.10")
# # task1 = Task("1")
# # task2 = Task("2")
# # task3 = Task("3")
# #
# # project.add_task(task1)
# # project.add_task(task2)
# # project.add_task(task3)
# #
# # task1.mark_complete()
# # print(project.get_progress())
# #
# #
#
#
# """2. Task: Create a BankSystem with Multiple Account Types
# Create a BankAccount class with:
# •  Attributes:
# o  account_number (string)
# o  balance (float)
# o  account_type (string, choices: "Savings", "Current")
# •  Methods:
# o  deposit(amount): Adds the amount to the balance.
# o  withdraw(amount): Withdraws the amount if the balance is sufficient.
# o  apply_interest(): Applies interest (different rates for savings and current accounts).
# Objective: Implement conditional logic based on the account type.
# """
#
# # class BankAccount:
# #     def __init__(self, account_number: str, balance: float, account_type: str):
# #         self.account_number = account_number
# #         self.balance = balance
# #         self.account_type = account_type
# #
# #     def deposit(self, amount):
# #         self.balance += amount
# #         return self.balance
# #
# #     def withdraw(self, amount):
# #         self.balance -= amount
# #         return self.balance
# #
# #     def apply_interest(self):
# #         if self.account_type == "Savings":
# #             self.balance *= 1
# #         elif self.account_type == "Current":
# #             self.balance *= 2
# #
# #
# #
# # savings_account = BankAccount("938724269", 1000, "Savings")
# # savings_account.deposit(500)
# # savings_account.apply_interest()
# # print(savings_account.balance)
# #
#
# """3. Task: Create a Chess Game
# Create a ChessPiece class with:
# •  Attributes:
# o  name (string, e.g., "Pawn", "Queen", etc.)
# o  position (tuple, e.g., (1, 1) for a1 on a chessboard)
# •  Methods:
# o  move(new_position): Updates the position, but only if the move is valid for the piece.
# Create a ChessGame class with:
# •  Attributes:
# o  pieces (list of ChessPiece objects)
# •  Methods:
# o  add_piece(piece): Adds a new piece to the board.
# o  is_checkmate(): Returns True if the king is in checkmate (simplified logic).
# Objective: Implement rules and constraints for moving chess pieces.
# """
#
#
#
# # class ChessPiece:
# #     def __init__(self, name, position):
# #         self.name = name
# #         self.position = position
# #
# #     def move(self, new_position):
# #         self.position = new_position
# #
# # class ChessGame:
# #     def __init__(self):
# #         self.pieces = []
# #
# #     def add_pieces(self, piece):
# #         self.pieces.append(piece)
#
# #
# # a = int(input())
# # if a % 2 == 0:
# #     print(a//2)
# # else:
# #     print((a // 2)-a)
#
#
#
# # def is_simple(x):
# #     divisor = 2
# #     while divisor < x:
# #         if x % divisor == 0:
# #             return False
# #         divisor += 1
# #     return True
# # print(is_simple(9))
# #
#
#
# # a = [1,2,3,4,5,6]
# # for k in range(5):
# #
# """### 2. Product Class
# Create a Product class that has private attributes for the product name, price, and quantity.
# - Implement methods to get and set each attribute.
# - Add a method to apply a discount to the price (should not allow negative prices or quantities)."""
# # class Product:
# #     def __init__(self, name, price, quantity):
# #         self.__name = name
# #         self.__price = price
# #         self.__quantity = quantity
# #
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def set_name(self, name):
# #         self.__name = name
# #
# #     def get_price(self):
# #         return self.__price
# #
# #     def set_price(self, price):
# #         if price >= 0:
# #             self.__price = price
# #         else:
# #             print("Price cannot be negative.")
# #
# #
# #     def get_quantity(self):
# #         return self.__quantity
# #
# #     def set_quantity(self, quantity):
# #         self.__quantity = quantity
# #
# #     def apply_discount(self, discount):
# #         if 0 < discount <= 1:
# #             self.__price *= (1 - discount)
# #         else:
# #             print("Invalid discount. Discount must be between 0 and 1.")
# #
# #
# # product1 = Product(name='Product', price=10, quantity=30)
# #
# # product1.apply_discount(1)
# # print(product1.get_price())
# #
# #
#
# # a = 0
# # def is_prime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, int(n**0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True
#
# """1. Create a Book Class
# Define a class Book with a constructor that initializes title and author.
# Add a method describe() that prints the book title and author.
# Create two instances of Book and call the describe() method."""
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def describe(self):
#         print(f"Title: {self.title}, Author: {self.author}")
#
#
#
# book1 = Book("Some", "Some")
# book2 = Book("Some1", "Some1")
# book1.describe()
# book2.describe()
#
#
#
# """2. Design a Student Class
# Define a class Student with a constructor to initialize name and grade.
# Add a method greet() that prints a greeting with the student’s name.
# Add another method is_passing() that checks if the grade is greater than or equal to 50."""
#
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def greet(self):
#         print(f"Hello, {self.name}!")
#
#     def is_passing(self):
#         return self.grade >= 50
#
#
#
# student1 = Student("Akobir", 85)
# student1.greet()
# print(student1.is_passing())
#
#
# """3. Create a Circle Class
# Define a class Circle with a constructor that initializes radius.
# Add a method area() to calculate and return the circle’s area (use 3.14 * radius * radius).
# Add another method circumference() to calculate the circumference (2 * 3.14 * radius)."""
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def circumference(self):
#         return 2 * 3.14 * self.radius
#
# circle1 = Circle(8)
# print(circle1.area())
# print(circle1.circumference())
#
#
# """4. Build a Car Class
# Define a class Car with a constructor to initialize brand and mileage.
# Add a method display_info() that prints the brand and mileage.
# Add another method drive() that increases the mileage by a specified amount."""
#
# class Car:
#     def __init__(self, brand, mileage):
#         self.brand = brand
#         self.mileage = mileage
#
#     def display_info(self):
#         print(f"brand: {self.brand}, mileage: {self.mileage}")
#
#     def drive(self, amount):
#         self.mileage += amount
#         print(f"drove {amount} miles. new mileage: {self.mileage}")
#
#
# car1 = Car("toyota", 30)
# car1.display_info()
# car1.drive(50)
#
# """5. Design a Pet Class
# Define a class Pet with a constructor to initialize name and species.
# Add a method introduce() that says "I am a [species] and my name is [name]."
# Create multiple pet objects and call their introduce() method."""
#
# class Pet:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def introduce(self):
#         print(f"I am a {self.species} and my name is {self.name}.")
#
#
# dog1 = Pet("Some1", "Some1")
# dog1.introduce()
# cat1 = Pet("Whiskers", "Cat")
# cat1.introduce()
#
#
# """6. Create a TemperatureConverter Class
# Define a class TemperatureConverter with no attributes.
# Add a method celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit (celsius * 9/5 + 32).
# Add another method fahrenheit_to_celsius(fahrenheit) that converts Fahrenheit to Celsius."""
#
# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         return f"{celsius * 9/5 + 32} celsius"
#
#     def fahrenheit_to_celsius(self, fahrenheit):
#         return f"{(fahrenheit - 32) * 5/9} farenheit"
#
#
# converter = TemperatureConverter()
# print(converter.celsius_to_fahrenheit(25))
# print(converter.fahrenheit_to_celsius(77))
#
# """7. Build a Person Class
# Define a class Person with a constructor to initialize name and age.
# Add a method birthday() that increments the age by 1.
# Add another method introduce() to print "Hi, I am [name] and I am [age] years old."""
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def birthday(self):
#         self.age += 1
#
#     def introduce(self):
#         print(f"Hi, I am {self.name} and I am {self.age} years old.")
#
#
# person1 = Person("Akobir", 17)
# person1.introduce()
# person1.birthday()
# person1.introduce()
#
#
# """8. Create a Rectangle Class
# Define a class Rectangle with a constructor to initialize width and height.
# Add a method area() to calculate the area (width * height).
# Add another method scale(factor) to multiply both width and height by a scaling factor."""
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def scale(self, factor):
#         self.width *= factor
#         self.height *= factor
#         return f"{self.width} is width and height is {self.height}"
#
# rectangle1 = Rectangle(10, 20)
# print(rectangle1.area())
# print(rectangle1.scale(2))
#
#
#
# """9. Design a ShoppingCart Class
# Define a class ShoppingCart with an empty list as an attribute to hold items.
# Add a method add_item(item) to add an item to the list.
# Add another method view_cart() to print all items in the shopping cart."""
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def view_cart(self):
#         print("Items in the cart:")
#         for item in self.items:
#             print(item)
#
# shop_cart1 = ShoppingCart()
# shop_cart1.add_item("Apple")
# shop_cart1.add_item("Banana")
# shop_cart1.view_cart()
#
#
# """10. Create a BankAccount Class
# Define a class BankAccount with a constructor to initialize account_holder and balance (default to 0).
# Add a method deposit(amount) to increase the balance by amount.
# Add another method withdraw(amount) to decrease the balance by amount.
# Add a method check_balance() to display the current balance."""
#
#
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def check_balance(self):
#         print(f"Balance: {self.balance}")
#
#
# holder_bank = BankAccount("Akobir", 90)
# holder_bank.deposit(50)
# holder_bank.withdraw(20)
# holder_bank.check_balance()
#
#

#
#
# import random
# print(random.randint(1, 25))


# def insert_sort(A: list):
#     for i in range(1, len(A)):
#         while i > 0 and A[i-1] > A[i]:
#             A[i-1], A[i] = A[i], A[i-1]
#             i -= 1
#
#     return A
# print(insert_sort([5, 3, 9, 8, 4]))
# #
#
# """APM functions: change password and withdrawing cashses"""
# class APM:
#     def __init__(self, password):
#         self.__password = password
#         self.__cash = 500
#
#     def withdraw(self, cash_withdraw):
#         if self.__cash >= cash_withdraw:
#             self.__cash -= cash_withdraw
#             return f"your cash is now ${self.__cash}"
#         else:
#             return "Insufficient funds"
#
#     def change_password(self, old_password, new_password):
#         if old_password == self.__password:
#             self.__password = new_password
#             return "Password changed successfully"
#         else:
#             return "Incorrect password"
#
#
# apm = APM("123456")
# print(apm.withdraw(300))
# print(apm.change_password("123456", "654321"))
# print(apm.withdraw(300))
#
# cash = 500
# def withdraw(cash_withdraw):
#
# a = "1010111"
# for i in range(0, len(a)):
#     res = 2 * int(a[i])




#
# """"""
#
# class Library:
#     def __init__(self, title, author, publication_year):


# ATM in terminal
# def_cash = 500
# print("Create Your Account")
# balance = 0
# def create_account(password, confirm_password):
#     if password != confirm_password:
#         return "Password do not match"
#     else:
#         return "Password matches, successfully created account"
#
#
# password = input("Enter your password")
# confirm_password = input("Enter your password")
# create_account(password, confirm_password)
# print("Account created successfully")
# print("ATM Menu:")
# print("1. Check Balance")
# print("2. Deposit Cash")
# print("3. Withdraw Cash")
# print("4. Change Password")
# print("5. Exit")
# print("6. Delete account")
#
# while True:
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print(f"Your current balance is: ${def_cash}")
#         continue
#     if choice == "2":
#         amount = float(input("Enter the amount to deposit: "))
#         def_cash += amount
#         print(f"Deposit successful. New balance: ${def_cash}")
#         continue
#     if choice == "3":
#         amount = float(input("Enter the amount to withdraw: "))
#         if amount > def_cash:
#             print("Money are less that you will withdraw")
#         else:
#             def_cash -= amount
#             print(f"Withdrawal successful. New balance: ${def_cash}")
#         continue
#     if choice == "4":
#         old_password = input("Enter your current password: ")
#         if old_password == password:
#             new_password = input("Enter a new password: ")
#             confirm_password = input("Confirm the new password: ")
#             if new_password == confirm_password:
#                 print("Password changed successfully")
#             else:
#                 print("Passwords do not match")
#         else:
#             print("Incorrect password")
#         continue
#     if choice == "5":
#         print("Thank you for using our ATM. Goodbye!")
#         break
#
#     if choice == "6":
#         password = input("Enter your password to delete your account: ")
#         if password == password:
#             print("Account deleted successfully")
#             break
#         else:
#             print("Incorrect password")
#             continue
#
#     else:
#         print("Invalid choice. Please try again.")
#
# a = "1010111"
# a = a[::-1]
# b = list(range(0, len(a)))
# x = []
# res = 0
# for i in range(len(a)):
#     if a[i] == '0':
#         x.append(i)
# for i in x:
#     b.remove(i)
# res = 0
# for i in range(0, len(b)):
#     res += 2 ** b[i]
# print(res)




#
# class Library:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.books = []
#
#     def display_books(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Publication Year: {self.publication_year}")
#         print("Available Books:")
#
#
#     def add_book(self, book):
#         """Add a book with all details to the list of books"""
#         self.books.append(book)
#
#
#     def remove_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 return "Book removed successfully"
#         return "Book not found"
#
# book1 = Library("Book1", "Book1", 2020)
# book2 = Library("Book2", "Book2", 2021)
# book3 = Library("Book3", "Book3", 2022)
# book1.add_book(book1)
# book2.add_book(book2)
# book3.add_book(book3)
# print(book1.display_books())
# print(book2.display_books())
# print(book3.display_books())
# a = [1, 4, 4, 5, 5, 8, 8, 9, 9]
# unique_max = -1
# for num in a:
#     if a.count(num) == 1 and num > unique_max:
#         unique_max = num
# print(unique_max)
#
# """Student Grades Tracker
# Create a Student class with attributes for name, age, and a list of grades. Include methods to add grades, calculate the average grade, and display student details."""
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grades = []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def calculate_average_grade(self):
#         return sum(self.grades) / len(self.grades) if self.grades else 0
#
#     def display_student_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print("Grades:")
#         for grade in self.grades:
#             print(grade)
#         print(f"Average Grade: {self.calculate_average_grade()}")
#
#
# student1 = Student("John Doe", 18)
# student1.add_grade(85)
# student1.add_grade(90)
# student1.add_grade(78)
# student1.display_student_details()
#
# """Car Rental System
# Create a Car class with attributes like make, model, and availability status. Include methods to rent a car (which changes its status to unavailable) and return it (making it available again). You can also add a rental price per day attribute and calculate the total rental cost.
# """
#
#
# class Car:
#     def __init__(self, make, model, rental_price_per_day):
#         self.make = make
#         self.model = model
#         self.availability_status = False
#         self.rental_price_per_day = rental_price_per_day
#         self.rental_days = None
#     def rent_a_car(self, rental_days):
#         self.rental_days = rental_days
#         self.availability_status = True
#         return f"Car {self.make} rented successfully, per day {self.rental_price_per_day}"
#     def return_car(self):
#         self.availability_status = False
#         return f"Car {self.make} returned successfully, total cost: {self.rental_days*self.rental_price_per_day}"
#
#
# car1 = Car("Toyota", "Camry", 30)
# print(car1.rent_a_car(5))
# print(car1.return_car())
#
#
# """Inventory Management
# Create an Item class with attributes for name, quantity, and price. Implement methods to update the quantity when items are added or sold and calculate the total value of the items in inventory."""
#
#
# class Item:
#     def __init__(self, name, quantity, price):
#         self.name = name
#         self.quantity = quantity
#         self.price = price
#         self.total_value = self.quantity * self.price
#         self.inventory = []
#     def add_item(self, name, quantity, price):
#         self.quantity += quantity
#         self.price = price
#         self.total_value = self.quantity * self.price
#         self.inventory.append([name, quantity, price])
#         return f"{name} added successfully, new quantity: {self.quantity}"
#     def update_quantity(self, quantity):
#         self.quantity = quantity
#         self.total_value = self.quantity * self.price
#         return f"Quantity updated successfully, new quantity: {self.quantity}"
#     def sell_item(self, quantity):
#         if quantity <= self.quantity:
#             self.quantity -= quantity
#             self.total_value = self.quantity * self.price
#             return f"{quantity} {self.name}(s) sold successfully, new quantity: {self.quantity}"
#         else:
#             return "Not enough items in inventory"
#
#
# item1 = Item("Apple", 10, 1.5)
# print(item1.add_item("Banana", 5, 0.75))
# print(item1.update_quantity(15))
# print(item1.sell_item(8))
# print(item1.sell_item(12))
#
#
# """Employee Management System
# Design an Employee class with attributes for name, job title, and salary. Include methods for giving a raise and displaying employee details."""
#
#
# class Employee:
#     def __init__(self, name, job_title, salary):
#         self.name = name
#         self.job_title = job_title
#         self.salary = salary
#         self.employees = []
#     def give_raise(self, name):
#         for employee in self.employees:
#             if employee.name == name:
#                 employee.salary += 500
#                 return f"{employee.name}'s salary raised by 500"
#         return "Employee not found"
#     def display_employee_details(self):
#         print(f"Name: {self.name}")
#         print(f"Job Title: {self.job_title}")
#         print(f"Salary: {self.salary}")
#
#
# employee1 = Employee("John Doe", "Software Engineer", 50000)
# employee2 = Employee("Jane Smith", "Project Manager", 60000)
# employee1.employees.append(employee1)
# employee2.employees.append(employee2)
# print(employee1.give_raise("John Doe"))
# employee1.display_employee_details()
#
# """Shopping Cart
# Create a Product class with attributes for name, price, and quantity. Then create a ShoppingCart class that can add products, remove products, and calculate the total price of items in the cart.
# """
#
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def update_quantity(self, quantity):
#         self.quantity = quantity
#         return f"Quantity updated successfully, new quantity: {self.quantity}"
#
#     def sell_item(self, quantity):
#         if quantity <= self.quantity:
#             self.quantity -= quantity
#             return f"{quantity} {self.name}(s) sold successfully, new quantity: {self.quantity}"
#         else:
#             return "Not enough items in stock"
#
#     def calculate_total_price(self):
#         return self.price * self.quantity
#
#
# class ShoppingCart:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         return f"{product.name} added successfully to the cart"
#
#     def remove_product(self, product_name):
#         for product in self.products:
#             if product.name == product_name:
#                 self.products.remove(product)
#                 return f"{product_name} removed successfully from the cart"
#         return "Product not found in the cart"
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products:
#             total_price += product.calculate_total_price()
#         return total_price
#
#
# product1 = Product("Apple", 1.5, 10)
# product2 = Product("Banana", 0.75, 5)
# cart = ShoppingCart()
# print(cart.add_product(product1))
# print(cart.add_product(product2))
# print(cart.calculate_total_price())
# print(cart.remove_product("Banana"))
# print(cart.calculate_total_price())
#
# """Ticket Booking System
# Create a MovieTicket class with attributes for movie title, showtime, and price. Include a method to print the ticket details. Then, create a Booking class that manages the number of tickets available and handles bookings (ensuring no overbooking).
# """
#
#
# class MovieTicket:
#     def __init__(self, movie_title, showtime, price):
#         self.movie_title = movie_title
#         self.showtime = showtime
#         self.price = price
#         self.remaining_tickets = 10
#         self.bookings = []
#
#     def print_ticket_details(self):
#         print(f"Movie Title: {self.movie_title}")
#         print(f"Showtime: {self.showtime}")
#         print(f"Price: ${self.price}")
#         print(f"Remaining Tickets: {self.remaining_tickets}")
#
#
# class Booking:
#     def __init__(self, movie_ticket):
#         self.movie_ticket = movie_ticket
#         self.total_price = self.movie_ticket.price * self.movie_ticket.remaining_tickets
#         self.bookings = []
#
#     def book_ticket(self, num_tickets):
#         if num_tickets <= self.movie_ticket.remaining_tickets:
#             self.movie_ticket.remaining_tickets -= num_tickets
#             self.total_price -= self.movie_ticket.price * num_tickets
#             self.bookings.append(num_tickets)
#             return f"Ticket booked successfully, {num_tickets} ticket(s) remaining"
#         else:
#             return "Not enough remaining tickets"
#
#
# movie_ticket = MovieTicket("Inception", "10:00 PM", 15.00)
# booking = Booking(movie_ticket)
# print(booking.book_ticket(5))
# print(booking.book_ticket(7))
# movie_ticket.print_ticket_details()
#
# """Bank Loan System
# Create a Loan class with attributes for loan amount, interest rate, and loan duration. Include methods to calculate the total repayment amount, interest, and monthly payment.
# """
#
#
# class Loan:
#     def __init__(self, loan_amount, interest_rate, loan_duration):
#         self.loan_amount = loan_amount
#         self.interest_rate = interest_rate
#         self.loan_duration = loan_duration
#
#     def calculate_total_repayment_amount(self):
#         return self.loan_amount + (self.loan_amount * self.interest_rate * self.loan_duration)
#
#     def calculate_interest(self):
#         return self.loan_amount * self.interest_rate * self.loan_duration
#
#     def calculate_monthly_payment(self):
#         monthly_interest = self.loan_amount * self.interest_rate / 12
#         monthly_payment = self.loan_amount / (self.loan_duration * 12) + monthly_interest
#         return monthly_payment
#
#
#
# loan = Loan(10000, 0.05, 5)
# print(f"Total Repayment Amount: ${loan.calculate_total_repayment_amount()}")
# print(f"Interest: ${loan.calculate_interest()}")
# print(f"Monthly Payment: ${loan.calculate_monthly_payment()}")
#
#
# """Room Reservation System
# Design a Room class with attributes like room number, type (single/double), and price per night. Create a Reservation class that books rooms and calculates the total cost for the reservation."""
# import datetime
# class Room:
#     def __init__(self, room_number, room_type, price_per_night):
#         self.room_number = room_number
#         self.room_type = room_type
#         self.price_per_night = price_per_night
#
#     def get_room_details(self):
#         return f"Room Number: {self.room_number}, Room Type: {self.room_type}, Price per Night: ${self.price_per_night}"
#
# class Reservation:
#     def __init__(self, room):
#         self.room = room
#         self.start_date = None
#         self.end_date = None
#         self.total_cost = None
#
#     def book_room(self, start_date, end_date):
#         self.start_date = start_date
#         self.end_date = end_date
#         self.total_cost = self.room.price_per_night * (end_date - start_date).days
#         return f"Room Booked successfully, Total Cost: ${self.total_cost}"
#
#     def cancel_reservation(self):
#         self.start_date = None
#         self.end_date = None
#         self.total_cost = None
#         return "Reservation Cancelled"
#
#     def get_reservation_details(self):
#         return f"Room Details: {self.room.get_room_details()}, Start Date: {self.start_date}, End Date: {self.end_date}, Total Cost: ${self.total_cost}"
#
#
# room = Room(101, "Single", 150)
# reservation = Reservation(room)
# print(reservation.book_room(datetime.date(2022, 1, 1), datetime.date(2022, 1, 7)))
# print(reservation.get_reservation_details())


# a = [1, 9, 9, 8, 8, 4, 1]
# unique_max = -1
#
# for num in a:
#     if a.count(num) == 1:
#         unique_max = num
# print(unique_max)

#


#
# """1. Public Variable: Rectangle Area
# Task: Create a class Rectangle with public variables length and width. Write a method to calculate and display the area of the rectangle. Allow direct modification of the dimensions and observe the behavior."""
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
#     def modify_dimensions(self, new_length, new_width):
#         self.length = new_length
#         self.width = new_width
#         print(f"New: Length = {self.length}, Width = {self.width}")
#
# rectangle1 = Rectangle(10, 20)
# print(rectangle1.calculate_area())
# rectangle1.modify_dimensions(5, 15)
# print(rectangle1.calculate_area())
#
#
# """2. Private Variable: Safe Deposit Box
# Task: Create a class SafeBox with a private variable __pin_code. Add methods to:
# Set the pin code.
# Validate a user-entered pin code."""
#
# class SafeBox:
#     def __init__(self):
#         self.__pin_code = None
#
#     def set_pin_code(self, pin_code):
#         self.__pin_code = pin_code
#
#     def validate_pin_code(self, entered_pin_code):
#         return self.__pin_code == entered_pin_code
#
#
# safe_box = SafeBox()
# safe_box.set_pin_code(1234)
# print(safe_box.validate_pin_code(1234))
# print(safe_box.validate_pin_code(5678))
#
#
# """3. Encapsulation: Movie Ratings
# Task: Create a class Movie with:
# Public variables title and genre.
# A private variable __rating.
# Add methods to:
# Set a valid rating between 0 and 10.
# Display movie details, including the rating"""
#
#
# class Movie:
#     def __init__(self, title, genre):
#         self.title = title
#         self.genre = genre
#         self.__rating = 0
#
#     def set_rating(self, new_rating):
#         if 0 <= new_rating <= 10:
#             self.__rating = new_rating
#         else:
#             print("Invalid rating. Rating should be between 0 and 10.")
#
#     def display_movie_details(self):
#         print(f"Title: {self.title}")
#         print(f"Genre: {self.genre}")
#         print(f"Rating: {self.__rating}")
#
#
# movie1 = Movie('Interstellar', 'some1')
# movie1.set_rating(4)
# movie1.display_movie_details()
#

# """4. Public and Private: Temperature Converter
# Task: Create a class Temperature with:
# Public variables celsius and fahrenheit.
# Methods to:
# # Convert Celsius to Fahrenheit and display the result.
# # Convert Fahrenheit to Celsius and display the result.
# # Ensure direct modification of variables affects the conversions."""
#
#
# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         return f"{celsius * 9/5 + 32} celsius"
#
#     def fahrenheit_to_celsius(self, fahrenheit):
#         return f"{(fahrenheit - 32) * 5/9} farenheit"
#
#
# converter = TemperatureConverter()
# print(converter.celsius_to_fahrenheit(25))
# print(converter.fahrenheit_to_celsius(77))

#
# """5. Private Variable: Gym Membership
# Task: Create a class GymMembership with a private variable __member_id and public variables name and age. Add methods to:
# Set and display the member ID.
# Ensure the age is at least 18 during initialization or modification."""
#
# class GymMembership:
#     def __init__(self, name, age, member_id):
#         self.__member_id = member_id
#         self.name = name
#         self.age = age
#
#     def set_member_id(self, new_member_id):
#         self.__member_id = new_member_id
#
#     def check_age(self):
#         if self.age >= 18:
#             return True
#         else:
#             return False
#
#     def display_member_details(self):
#         print(f"Member ID: {self.__member_id}")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#
# gymmember = GymMembership('some', 18, '98699')
# gymmember.set_member_id('7957')
# print(gymmember.check_age())
# gymmember.display_member_details()
#
# """6. Public Variables: Circle Properties
# Task: Create a class Circle with public variables radius and color. Add a method to calculate and display the circle’s area. Allow the radius to be directly modified and observe the effect."""
#
#
# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def calculate_area(self):
#         return 3.14 * (self.radius ** 2)
#
#     def modify_radius(self, new_radius):
#         self.radius = new_radius
#         print(f"New Radius: {self.radius}")
#         print(f"New Area: {self.calculate_area()}")
#
#
# circle1 = Circle(10, "Red")
# print(circle1.calculate_area())
# circle1.modify_radius(5)
#
# """7. Encapsulation: Bank Interest Rate
# Task: Create a class BankAccount with:
# Public variable account_number.
# A private variable __interest_rate.
# Add methods to:
# Set a valid interest rate (0-100).
# Calculate and display interest based on a given balance."""
#
#
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.__interest_rate = 0
#         self.balance = balance
#
#     def set_interest_rate(self, new_interest_rate):
#         if 0 <= new_interest_rate <= 100:
#             self.__interest_rate = new_interest_rate
#         else:
#             print("Invalid interest rate. Interest rate should be between 0 and 100.")
#
#     def calculate_interest(self):
#         return self.balance * self.__interest_rate / 100
#
#     def display_interest(self):
#         print(f"Interest for Account Number {self.account_number}: ${self.calculate_interest()}")
#
#
# account1 = BankAccount("12345", 1000)
# account1.set_interest_rate(5)
# account1.display_interest()
#
#
# """8. Public and Private: Inventory Stock
# Task: Create a class Product with:
# Public variables name and price.
# A private variable __stock.
# Add methods to:
# Increase or decrease the stock.
# Prevent stock from going below zero."""
#
#
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.__stock = 0
#
#     def increase_stock(self, quantity):
#         self.__stock += quantity
#         if self.__stock < 0:
#             self.__stock = 0
#             print(f"Stock cannot be increased. Stock level has reached zero.")
#         print(f"{self.name} stock increased by {quantity}. New stock: {self.__stock}")
#
#     def decrease_stock(self, quantity):
#         if self.__stock >= quantity:
#             self.__stock -= quantity
#             print(f"{self.name} stock decreased by {quantity}. New stock: {self.__stock}")
#         else:
#             print(f"Stock cannot be decreased. Only {self.__stock} units available.")
#
# product1 = Product('some', 90)
# product1.increase_stock(5)
# product1.decrease_stock(3)
# product1.decrease_stock(3)
#
#
# """9. Encapsulation with Validation: Marks Calculator
# Task: Create a class Student with:
# Public variables name and roll_number.
# Private variables __math_marks, __science_marks, and __english_marks.
# Add methods to:
# Set marks for each subject (validate: 0-100).
# Calculate and display the total and average marks."""
#
#
# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
#         self.__math_marks = 0
#         self.__science_marks = 0
#         self.__english_marks = 0
#
#     def set_marks(self, subject, marks):
#         if 0 <= marks <= 100:
#             if subject == "Math":
#                 self.__math_marks = marks
#             elif subject == "Science":
#                 self.__science_marks = marks
#             elif subject == "English":
#                 self.__english_marks = marks
#             else:
#                 print("no subject")
#         else:
#             print("max 0-100")
#
#     def calculate_total_marks(self):
#         return self.__math_marks + self.__science_marks + self.__english_marks
#
#     def calculate_average_marks(self):
#         total_marks = self.calculate_total_marks()
#         if total_marks > 0:
#             return total_marks / 3
#         else:
#             return 0
#
#
# student1 = Student("some", 123)
# student1.set_marks("Math", 80)
# student1.set_marks("Science", 90)
# student1.set_marks("English", 85)
# print(f"Total Marks: {student1.calculate_total_marks()}")
# print(f"Average Marks: {student1.calculate_average_marks()}")
#
#
# """10. Public Variables: Laptop Specifications
# Task: Create a class Laptop with public variables brand, model, and price. Write methods to:
# Display laptop details.
# Allow direct modifications of variables and observe the results."""
#
# class LaptopSpecifications:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def display_laptop_details(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Price: {self.price}")
#
#     def direct_modifications(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         print(f"New Brand: {self.brand}")
#         print(f"New Model: {self.model}")
#         print(f"New Price: {self.price}")
#
#
# laptop1 = LaptopSpecifications("some", "some", 1500)
# laptop1.display_laptop_details()
# laptop1.direct_modifications("some1", "some1", 1800)


# def quick_sort(x:list):
#     if len(x) <= 1:
#         return x
#     else:
#         pivot = x.pop()
#     items_grower = []
#     items_lower = []
#     for item in x:
#         if item > pivot:
#             items_grower.append(item)
#         else:
#             items_lower.append(item)
#
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_grower)
#
# print(quick_sort([5,6,3,32,6,62,46]))


# def bubble_sort(x):
#     flag = True
#     while flag:
#         flag = False
#         for i in range(len(x)-1):
#             if x[i] > x[i+1]:
#                 flag = True
#                 x[i], x[i+1] = x[i+1], x[i]
#                 print(x)
#
#     return x
#
# print(bubble_sort([1,6,62,8,2,1,6,9,0]))

#
# def selection_sort(x:list):
#     for i in range(0, len(x)-1):
#         cur_min = i
#         for j in range(i+1, len(x)):
#             if x[j] < x[cur_min]:
#                 cur_min = j
#         x[i], x[cur_min] = x[cur_min], x[i]
#     return x
#
# print(selection_sort([5,8,1,2,3,90,3,2]))


# def merge_split(a1, a2):
#     c = []
#     i = 0
#     j = 0
#     while i < len(a1) and j < len(a2):
#         if a1[i] < a2[j]:
#             c.append(a1[i])
#             i += 1
#         else:
#             c.append(a2[j])
#             j += 1
#     c += a1[i:] + a2[j:]
#     return c
#
#
# def split_into_halfes(a:list):
#     n = len(a) // 2
#     a1 = a[:n]
#     a2 = a[n:]
#     if len(a1) > 1:
#         a1 = split_into_halfes(a1)
#     if len(a2) > 1:
#         a2 = split_into_halfes(a2)
#
#     return merge_split(a1, a2)
#
#
#
# a = [-3, 4, 7, 1, 9, 5]
# print(split_into_halfes(a))

#

#
# input_str = "1 5"
#
# clean_input = ""
# for char in input_str:
#     if char != " ":
#         clean_input += char
#
# print(clean_input)
# start = int(clean_input[0])в
# end = int(clean_input[1])
# output_str = ""
# i = start
# while i <= end:
#     output_str += str(i) + " "
#     i += 1
#
# print(output_str[:-1])

# def binary_search(arr, target):
#
#   start = 0
#   end = len(arr) - 1
#
#   while start <= end:
#
#     mid = (start + end) // 2
#
#     if arr[mid] == target:
#       return mid
#
#     elif arr[mid] < target:
#       start = mid + 1
#
#     else:
#
#       end = mid - 1
#
#   return -1
#
#
# arr = [1,5,1000, 144,23,111, 500]
# target = 1000
#
# result = binary_search(arr, target)
# print(result)
#
# if result != -1:
#   print("Element found at index", result)
# else:
#   print("Element not found")

# a = [1, 6, 8, -1, 5]
# print(sorted(a))

# with open('text.txt', "r") as f:
#     text = f.read()
#
# res = text.split()[-2:]
# for i in res:
#     print(i, end=" ")
#
# print()
#
# def unique_email(a):
#     res = []
#     for i in a:
#         if i not in res:
#             res.append(i)
#     return res
#
#
# print(unique_email(["john@example.com", "bob@example.com"]))
#
#

# word1 = "abc"
# word2 = "pqr"
#
# for i in range(0, len(word1), 2):
# a = [-1, 8, 7, -12, 10, 3]
# two_sum = -5
# left = 0
# right = len(a) - 1
# while left < right:
#     if a[left] + a[right] < two_sum:
#         left += 1
#     else:
#         right -= 1


# def quick_sort(x:list):
#     if len(x) <= 1:
#         return x
#     pivot = x.pop()
#     items_grower = []
#     items_lower = []
#     for item in x:
#         if item > pivot:
#             items_grower.append(item)
#         else:
#             items_lower.append(item)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_grower)


# def find_pairs(nums, target):
#     left = 0
#     right = len(nums) - 1
#     pairs = []
#     while left < right:
#         current_nums = nums[left] + nums[right]
#         if current_nums == target:
#             pairs.append((nums[left], nums[right]))
#             left += 1
#             right -= 1
#         elif current_nums < target:
#             left += 1
#         else:
#
#             right -= 1
#     return pairs

# print(find_pairs([1, 2, 3, 4, 5], 2))

# def quick_sort(x: list):
#     if len(x) <= 1:
#         return x
#     pivot = x.pop()
#     items_grower = []
#     items_lower = []
#     for item in x:
#         if item > pivot:
#             items_grower.append(item)
#         else:
#             items_lower.append(item)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_grower)
#
#
#
# def sliding_window(x, k):
#     x = quick_sort(x)
#     n = len(x)
#     window_sum = sum(x[:k])
#     max_sum = window_sum
#     for i in range(n - k):
#         window_sum = window_sum - x[i] + x[i+k]
#         max_sum = max(window_sum, max_sum)
#
#     return max_sum
#
# print(sliding_window([1, 4, 7, 8, 9, 3, 5], 2))
#
# """Task: Shapes and Areas
# Create a parent class Shape with a method area() that returns 0 (a default value).
# Create child classes Rectangle and Circle.
# Rectangle should calculate the area of a rectangle.
# Circle should calculate the area of a circle."""
#
# class Shape:
#     def area(self):
#         return 0
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
#
# rectangle = Rectangle(5, 10)
# circle = Circle(3)
#
# print(rectangle.area())
# print(circle.area())
#
# """2. Task: VehiclesCreate a parent class Vehicle with attributes like make and model, and a method describe().
# Create child classes Car and Motorcycle, each adding unique methods like play_music() or pop_wheelie()."""
#
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def describe(self):
#         return f"This vehicle is a {self.make} {self.model}."
#
# class Car(Vehicle):
#     def __init__(self, make, model, color):
#         super().__init__(make, model)
#         self.color = color
#
#     def play_music(self):
#         return "Car cna play music."
#
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year):
#         super().__init__(make, model)
#         self.year = year
#
#     def pop_wheelie(self):
#         return "Motorcycle can pop a wheelie."
#
#
# car = Car("Toyota", "Camry", "Red")
# motorcycle = Motorcycle("Harley-Davidson", "SVT-R", 2015)
#
# print(car.describe())
# print(car.play_music())
#
# print(motorcycle.describe())
# print(motorcycle.pop_wheelie())
#
#
# """3. Task: Animals and SoundsCreate a parent class Animal with a method sound() that prints a generic sound.
# Create child classes Dog, Cat, and Cow that override the sound() method to print specific sounds (e.g., "Woof", "Meow", "Moo")."""
#
# class Animal:
#     def sound(self):
#         print("Generic sound.")
#
# class Dog(Animal):
#     def sound(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow!")
#
# class Cow(Animal):
#     def sound(self):
#         print("Moo!")
#
#
# dog = Dog()
# cat = Cat()
# cow = Cow()
#
# dog.sound()
# cat.sound()
# cow.sound()
#
#
# """4 .Task: Library SystemCreate a parent class LibraryItem with attributes like title and author.
# Create child classes Book and DVD that add unique attributes such as pages for books and runtime for DVDs.
# Add a method details() to display information about the item."""
#
# class LibraryItem:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
# class Book(LibraryItem):
#     def __init__(self, title, author, pages):
#         super().__init__(title, author)
#         self.pages = pages
#
#     def details(self):
#         return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
#
# class DVD(LibraryItem):
#     def __init__(self, title, author, runtime):
#         super().__init__(title, author)
#         self.runtime = runtime
#
#     def details(self):
#         return f"Title: {self.title}, Author: {self.author}, Runtime: {self.runtime} minutes"
#
#
# book = Book("some", "some", 280)
# dvd = DVD("some", "soome", 152)
#
# print(book.details())
# print(dvd.details())
#
# """5. Task: Online StoreCreate a parent class Product with attributes like name and price.
# Create child classes Clothing and Electronics.
# Clothing should have a size attribute.
# Electronics should have a warranty attribute.
# Add a method to display the details of each product."""
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Clothing(Product):
#     def __init__(self, name, price, size):
#         super().__init__(name, price)
#         self.size = size
#
#     def display_details(self):
#         return f"Name: {self.name}, Price: {self.price}, Size: {self.size}"
#
# class Electronics(Product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty
#
#     def display_details(self):
#         return f"Name: {self.name}, Price: {self.price}, Warranty: {self.warranty}"
#
#
# clothing = Clothing("Shirt", 19.99, "M")
# electronics = Electronics("iPhone", 999.99, "3 years")
#
# print(clothing.display_details())
# print(electronics.display_details())
#
#
# """Task: Employee Hierarchy
# Create a parent class Employee with attributes like name and salary, and a method work().
# Create child classes Manager and Developer.
# Manager should have a method hold_meeting().
# Developer should have a method write_code()."""
#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def method_work(self):
#         return "Employee is working."
#     def display_details(self):
#         return f"Name: {self.name}, Salary: {self.salary}"
#
# class Manager(Employee):
#     def hold_meeting(self):
#         return "Manager is holding a meeting."
#
# class Developer(Employee):
#     def write_code(self):
#         return "Developer is writing code."
#
#
# employee = Employee("John Doe", 50000)
# manager = Manager("Jane Smith", 80000)
# developer = Developer("Bob Johnson", 60000)
#
# print(employee.method_work())
# print(manager.hold_meeting())
# print(developer.write_code())
#
#
# """7. Task: Banking SystemCreate a parent class BankAccount with methods for deposit() and withdraw().
# Create child classes SavingsAccount and CheckingAccount.
# SavingsAccount should add a method add_interest().
# CheckingAccount should have a method write_check()."""
#
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#     def deposit(self, deposit):
#         self.balance += deposit
#     def withdraw(self, amount):
#         self.balance -= amount
#
# class SavingAccount(BankAccount):
#     def add_interest(self, interest_rate):
#         self.balance += self.balance * interest_rate
#
#     def display_details(self):
#         return f"Account Number: {self.account_number}, Balance: {self.balance}"
#
# class CheckingAccount(BankAccount):
#     def write_check(self, amount, payee):
#         self.balance -= amount
#         return f"Check written to {payee}, new balance: {self.balance}"
#
#
# savings_account = SavingAccount("12345", 1000)
# checking_account = CheckingAccount("67890", 500)
#
# savings_account.deposit(500)
# savings_account.withdraw(200)
# savings_account.add_interest(0.05)
#
# print(savings_account.display_details())
#
# print(checking_account.write_check(100, "Someone"))
#
# """9. Task: School ManagementCreate a parent class Person with attributes like name and age.
# Create child classes Student and Teacher.
# Student should have a method study().
# Teacher should have a method teach().
# Create another class Principal that inherits from Teacher and adds a method manage_school()."""
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.grade = grade
#     def study(self):
#         return f"Student is studying. and his grade is {self.grade}"
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#     def teach(self):
#         return "Teacher is teaching."
#
#
# student = Student("John Doe", 18, 12)
# teacher = Teacher("Jane Smith", 35, "Math")
#
#
# print(student.study())
# print(teacher.teach())
#
# """10. Task: Zoo SimulationCreate a parent class Animal with attributes like name and species.
# Create child classes Carnivore and Herbivore.
# Carnivore should add a method hunt().
# Herbivore should add a method graze().
# Create subclasses of Carnivore (like Lion) and Herbivore (like Deer) with their unique behaviors."""
#
#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
# class Carnivore(Animal):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#
#     def hunt(self):
#         return f"{self.name} is hunting."
#
# class Herbivore(Animal):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#     def graze(self):
#         return f"{self.name} is grazing."
#
#
# lion = Carnivore("Simba", "Lion")
# deer = Herbivore("Buddy", "Deer")
#
# print(lion.hunt())
# print(deer.graze())
# animals = ['cat', 'dog', 'fish']
#
# for first_animal in animals:
#     for second_animal in animals:
#         print("Yesterday I bought a %s. Today I bought a %s." % (first_animal, second_animal))

# for i in zip(range(5), range(5, 10), range(10, 15)):
#     print(i)


# total = 0
# number = 0
#
# while total < 200:
#     number += 1
#     total += number**2
#
# print("Total: %d" % total)
# print("Last number: %d" % number)
#

# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))


# class Person:
#     def __init__(self, name, surname, number):
#         self.name = name
#         self.surname = surname
#         self.number = number
#
#
# class LearnerMixin:
#     def __init__(self):
#         self.classes = []
#
#     def enrol(self, course):
#         self.classes.append(course)
#
#
# class TeacherMixin:
#     def __init__(self):
#         self.courses_taught = []
#
#     def assign_teaching(self, course):
#         self.courses_taught.append(course)
#
#
# class Tutor(Person, LearnerMixin, TeacherMixin):
#     def __init__(self, *args, **kwargs):
#         super(Tutor, self).__init__(*args, **kwargs)
#
# jane = Tutor("Jane", "Smith", "SMTJNX045")
# jane.enrol('somethbb')
# jane.assign_teaching()
#
#
# class Parent1:
#     def func(self):
#         print("Parent1 function")
#
# class Parent1:
#     def func(self):
#         print("Parent1 function")
#
# class Child:
#     def func(self):
#         print("Parent1 function")

"""Task 1: Library Management System
Create a LibraryItem base class with:

Attributes:
title (string)
author (string)
publication_year (int)
Methods:
display_info(): Prints the item's details.
Create subclasses for Book and Magazine:

Book:
Additional attribute: genre (string)
Override display_info() to include genre.
Magazine:
Additional attribute: issue_number (int)
Override display_info() to include issue number.
Objective: Practice creating subclasses and overriding methods.
"""

# class LibrarySystem:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}")
#
# class Book(LibrarySystem):
#     def __init__(self, title, author, publication_year, genre):
#         super().__init__(title, author, publication_year)
#         self.genre = genre
#
#     def display_info(self):
#         super().display_info()
#         print(f"Genre: {self.genre}")
#
# class Magazine(LibrarySystem):
#     def __init__(self, title, author, publication_year, issue_number):
#         super().__init__(title, author, publication_year)
#         self.issue_number = issue_number
#     def display_info(self):
#         super().display_info()
#         print(f"Issue Number: {self.issue_number}")
#
#
# book = Book("some1", "some1", 1960, "some1")
# book.display_info()
#
# magazine = Magazine("some2", "some2", 1941, 100)
# magazine.display_info()


"""Task 2: Vehicle Rental System
Create a Vehicle base class with:

Attributes:
make (string)
model (string)
rental_rate (float)
Methods:
display_vehicle_info(): Prints the vehicle details.
Create subclasses for Car and Motorcycle:

Car:
Additional attribute: num_seats (int)
Override display_vehicle_info() to include the number of seats.
Motorcycle:
Additional attribute: engine_capacity (cc, int)
Override display_vehicle_info() to include engine capacity.
Add a RentalService class with:

Attributes:
vehicles (list of Vehicle objects)
Methods:
add_vehicle(vehicle): Adds a vehicle to the list.
get_all_vehicle_info(): Prints details of all vehicles.
Objective: Practice inheritance, composition, and method overriding.
"""
#
#
# class Vehicle:
#     def __init__(self, make, model, rental_rate):
#         self.make = make
#         self.model = model
#         self.rental_rate = rental_rate
#     def display_vehicle_info(self):
#         print(f"Make: {self.make}, Model: {self.model}, Rental Rate: {self.rental_rate}")
#
# class Car(Vehicle):
#     def __init__(self, make, model, rental_rate, num_seats):
#         super().__init__(make, model, rental_rate)
#         self.num_seats = num_seats
#     def display_vehicle_info(self):
#         super().display_vehicle_info()
#         print(f"Number of Seats: {self.num_seats}")
#
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, rental_rate, engine_capacity):
#         super().__init__(make, model, rental_rate)
#         self.engine_capacity = engine_capacity
#     def display_vehicle_info(self):
#         super().display_vehicle_info()
#         print(f"Engine Capacity: {self.engine_capacity} cc")
#
# class VehicleRentalService(Vehicle):
#     def __init__(self, make, model, rental_rate):
#         super().__init__(make, model, rental_rate)
#         self.vehicles = []
#
#     def add_vehicle(self, vehicle):
#         self.vehicles.append(vehicle)
#
#     def get_all_vehicle_info(self):
#         for vehicle in self.vehicles:
#             vehicle.display_vehicle_info()
#
#
# car = Car("Toyota", "Camry", 30, 5)
# motorcycle = Motorcycle("Honda", "Civic", 20, 125)
#
# rental_service = VehicleRentalService("General Motors", "Rental Service", 25)
# rental_service.add_vehicle(car)
# rental_service.add_vehicle(motorcycle)
# rental_service.get_all_vehicle_info()
#
# """Task 3: Employee Hierarchy
# Create an Employee base class with:
#
# Attributes:
# name (string)
# salary (float)
# Methods:
# display_info(): Prints employee name and salary.
# Create subclasses for Manager and Developer:
#
# Manager:
# Additional attribute: department (string)
# Override display_info() to include department.
# Developer:
# Additional attribute: programming_languages (list of strings)
# Override display_info() to include programming languages.
# Create an EmployeeSystem class with:
#
# Attributes:
# employees (list of Employee objects)
# Methods:
# add_employee(employee): Adds an employee to the system.
# get_all_employees_info(): Prints details of all employees.
# Objective: Understand hierarchical relationships in classes and how to manage collections of subclass objects.
# """
#
#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def display_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")
#
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#     def display_info(self):
#         super().display_info()
#         print(f"Department: {self.department}")
# class Developer(Employee):
#     def __init__(self, name, salary, programming_languages):
#         super().__init__(name, salary)
#         self.programming_languages = programming_languages
#     def display_info(self):
#         super().display_info()
#         print(f"Programming Languages: {', '.join(self.programming_languages)}")
#
#
# class EmployeeSystem:
#     def __init__(self):
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#
#     def get_all_employees_info(self):
#         for employee in self.employees:
#             employee.display_info()
#
#
# manager = Manager("John Doe", 50000, "Sales")
# developer = Developer("Jane Smith", 60000, ["Python", "JavaScript", "C++"])
# employee_system = EmployeeSystem()
# employee_system.add_employee(manager)
# employee_system.add_employee(developer)
# employee_system.get_all_employees_info()
#
#
# """Task 4: Animal Kingdom Simulation
# Create an Animal base class with:
#
# Attributes:
# name (string)
# age (int)
# Methods:
# make_sound(): Prints a generic animal sound.
# Create subclasses for Dog and Cat:
#
# Dog:
# Additional attribute: breed (string)
# Override make_sound() to print "Woof!"
# Cat:
# Additional attribute: color (string)
# Override make_sound() to print "Meow!"
# Add a Zoo class with:
#
# Attributes:
# animals (list of Animal objects)
# Methods:
# add_animal(animal): Adds an animal to the zoo.
# make_all_sounds(): Calls make_sound() for every animal in the zoo.
# Objective: Practice method overriding and polymorphism.
# """
#
#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def make_sound(self):
#         print("Generic animal sound")
#
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
#     def make_sound(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#     def make_sound(self):
#         print("Meow!")
#
#
# class Zoo:
#     def __init__(self):
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#     def make_all_sounds(self):
#         for animal in self.animals:
#             animal.make_sound()
#
#
# dog = Dog("Buddy", 5, "Golden Retriever")
# cat = Cat("Whiskers", 3, "Black")
#
# zoo = Zoo()
# zoo.add_animal(dog)
# zoo.add_animal(cat)
# zoo.make_all_sounds()
#
#
# """Task 5: Online Course Platform
# Create a Course base class with:
#
# Attributes:
# title (string)
# instructor (string)
# Methods:
# get_description(): Prints course title and instructor.
# Create subclasses for ProgrammingCourse and MathCourse:
#
# ProgrammingCourse:
# Additional attribute: languages (list of programming languages)
# Override get_description() to include languages.
# MathCourse:
# Additional attribute: difficulty_level (string)
# Override get_description() to include difficulty level.
# Add a CoursePlatform class with:
#
# Attributes:
# courses (list of Course objects)
# Methods:
# add_course(course): Adds a course to the platform.
# list_all_courses(): Prints details of all courses.
# Objective: Train students to work with inheritance and manage collections of objects."""
#
#

#
# """Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# """
#
#
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
# res = Solution()
# print(res.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

#
# def check_brackets(s: str):
#     a = ['(', '{', '[']
#     b = [')', '}', ']']
#     x = []
#     for i in s:
#         if i in a:
#             x.append(i)
#         elif i in b:
#             if not x or b.index(i) != a.index(x.pop()):
#                 return False
#
#     return not x
# print(check_brackets('(){}'))
#
#
# """Write a function to find the longest common prefix string amongst an array of strings.
#
# do it without any builtin fuctions, no functions, without min() and any functions
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# """
#



# class Student:
#     count = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#
#     @classmethod
#     def calculate_something(cls):
#         return f"Quantity of students: {cls.count}"
#
#
# student1 = Student("some1", 4)
# student1 = Student("some2", 3)
# student1 = Student("some3", 2)
#
# print(Student.calculate_something())
#
#
# arr = [1, 4, 45, 6, 0, 19]
#
# def min_subarray(arr: list):
#     a = []
#     for i in range(len(a))
#
#
# def alg(value, last = 1, data = [ ]):
#     for i in range(last + 1, value + 1):
#         res = value - i * i
#         if res > 0:
#             alg(res, i, data + [i])
#         elif res == 0:
#             print(' + '.join(f'{j} * {j}' for j in data + [i]), '=', sum(j * j for j in data + [i]))
#
# alg(1256)
#
#
# def twoSum(nums, target):
#     nums.sort()
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         currentSum = nums[left] + nums[right]
#
#         if currentSum == target:
#             return [left, right]
#         elif currentSum < target:
#             left += 1
#         elif currentSum > target:
#             right -= 1
#     return []
# nums = [2,7,11,15]
# target = 9
#
# print(twoSum(nums, target))



# def sortedSquares(nums):
#     start = 0
#     end = len(nums) - 1
#     res = [0] * len(nums)
#     i = len(res) - 1
#     while (start <= end and i >= 0):
#         if abs(nums[start]) <= abs(nums[end]):
#             res[i] = nums[end] ** 2
#             end -= 1
#         else:
#             res[i] = nums[start] ** 2
#             start += 1
#
#         i -= 1
#     return res
#
# nums = [-7,-3,2,3,11]
# print(sortedSquares(nums))


#
# i = 0
# while True:
#     if i == 5:
#         break
#     print("Hello", i)
#
#



# def transpose(matrix: list):
#     result = []
#     for i in range(len(matrix[0])):
#         newRow = []
#         for j in range(len(matrix)):
#             newRow.append(matrix[j][i])
#         result.append(newRow)
#     return result
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(transpose(matrix))
#
#
# def discriminant(a,b,c):
#     res = []
#     d = b**2 - 4*a*c
#     if d > 0:
#         x1 = -b


# a = [1,5,22,8,34,2]
# maxim = a[0]
# res = 0
# while 



#check something

# def cakes(recipe, available):
#     # counter = recipe[1] // available[1]
#     minimum = []
#     for i in recipe:
#         if i in available and recipe[i] <= available[i]:
#             minimum.append(available[i] // recipe[i])
#         elif i not in available or recipe[i] >= available[i]: 
#             return 0
            
#     return sorted(minimum)[0]
            
            
#     # return counter
        
    
    

# print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000, 'apples': 15, 'oil': 20}))
# print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
# print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
# print(cakes({'cream': 1, 'flour': 3, 'sugar': 1, 'milk': 1, 'oil': 1, 'eggs': 1}, {'sugar': 1, 'eggs': 1, 'flour': 3, 'cream': 1, 'oil': 1, 'milk': 1}))
# def erotosphen(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#     p = 2
#     while p*p < n:
#         for i in range(p*p, n+1, p):
#             primes[i] = False
#         p+=1
#     # for i in primes:
#     #     if primes[i]:
#     #         return i
#     return [i for i in range(len(primes)) if primes[i]]
# print(erotosphen(31))

# def summation_of_primes(primes):
#     primes_list = [True] * (primes + 1)
#     primes_list[0] = primes_list[1] = False
#     p = 2
#     while p * p < primes:
#         for i in range(p*p, primes + 1, p):
#             primes_list[i] = False
    
#         p+=1
#     res = []
#     for i in range(len(primes_list)):
#         if primes_list[i]:
#             res.append(i)
    
    
#     return sum(res)
            
# print(summation_of_primes(200))

# inputs = list(map(int, input().split()))


# import asyncio, random
# meals = {'steak': 7, 'pasta': 5, 'soup': 3}
# salads = {'caesar': 4, 'greek': 2, 'olivier': 6}
# desserts = {'cake': 5, 'icecream': 2}


# res = asyncio.Event()

# async def prepare_dish(dish_name, base_time, dish_type):
#     rand = random.randint(-2, 2)
#     cooking_time = base_time + rand
#     print(f"{dish_name} готовится {cooking_time}")
#     await asyncio.sleep(cooking_time)
    
#     if dish_type == "main":
#         print(f"{dish_name} готов")
#         res.set()
#         print(f"Подаем {dish_name} и ожидающие салаты")
        
#     elif dish_type == "salad":
#         print(f"{dish_name} готов, ждет основное блюдо")
#         await res.wait()
#         print(f"Подаем {dish_name}")
#     elif dish_type == "dessert":
#         print(f"{dish_name} готов, но ждет основное блюдо...")
#         await res.wait()
#         print(f"Подаем {dish_name}")
        
# async def main():
#     res.clear()
#     meal_choice = input("Выберите основное блюдо (steak/pasta/soup): ")
#     salad_choice = input("Выберите салат (caesar/greek/olivier): ")
#     dessert_choice = input("Выберите десерт (cake/icecream): ")
    
#     main_task = asyncio.create_task(
#         prepare_dish(meal_choice, meals[meal_choice], "main")
#     )
#     salad_task = asyncio.create_task(
#         prepare_dish(salad_choice, salads[salad_choice], "salad")
#     )
#     dessert_task = asyncio.create_task(
#         prepare_dish(dessert_choice, desserts[dessert_choice], "dessert")
#     )
#     await asyncio.gather(main_task, salad_task, dessert_task)
#     print("Все блюда поданы!")

# asyncio.run(main())




