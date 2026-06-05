#Classes & Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! I'm {self.name} and I'm {self.age} years old.")

person1 = Person("Abdullah", 18)
person2 = Person("Ali", 20)

person1.introduce()
person2.introduce()

#Methods & Attributes
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

account = BankAccount("Abdullah", 1000)
account.deposit(500)
account.withdraw(200)
account.show_balance()


#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Bruno")
cat = Cat("Whiskers")

dog.speak()
cat.speak()


#__str__ Method
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name} | Grade: {self.grade}"

s1 = Student("Abdullah", "A")
print(s1)  



#Class with Error Handling
class Calculator:
    def __init__(self, name):
        self.name = name

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Can't divide by zero!"

    def __str__(self):
        return f"Calculator: {self.name}"

calc = Calculator("Abdullah's Calc")
print(calc)
print(calc.divide(10, 2))
print(calc.divide(10, 0))


#Project: Student Management System
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject, score):
        self.grades[subject] = score
        print(f"Added {subject}: {score} for {self.name}")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

    def __str__(self):
        return f"{self.name} (Age: {self.age}) | Average: {self.get_average():.1f} | Grade: {self.get_letter_grade()}"


class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} added to {self.class_name}")

    def show_all(self):
        print(f"\n--- {self.class_name} Report ---")
        if not self.students:
            print("No students yet.")
        for student in self.students:
            print(student)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average())

classroom = Classroom("AI Batch 2025")

s1 = Student("Abdullah", 18)
s1.add_grade("Math", 95)
s1.add_grade("English", 88)
s1.add_grade("Science", 92)

s2 = Student("Ali", 19)
s2.add_grade("Math", 70)
s2.add_grade("English", 65)
s2.add_grade("Science", 75)

s3 = Student("Sara", 18)
s3.add_grade("Math", 85)
s3.add_grade("English", 90)
s3.add_grade("Science", 88)

classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

classroom.show_all()

top = classroom.top_student()
print(f"\nTop Student: {top.name} with average {top.get_average():.1f}")