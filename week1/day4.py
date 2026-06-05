#File Handling (Write & Read)
# Writing to a file
with open("notes.txt", "w") as file:
    file.write("My name is Abdullah\n")
    file.write("I am learning Python\n")
    file.write("Day 4 is going well!\n")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)


#Appending to a File
with open("notes.txt", "a") as file:
    file.write("I added this line later!\n")

# Read again to confirm
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())



#Modules
import math
import random
import datetime

print(math.sqrt(144))
print(math.pi)

print(random.randint(1, 100))

today = datetime.date.today()
print(f"Today is: {today}")


#Error Handling (try/except)
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: You can't divide by zero!")

try:
    number = int("abc")
except ValueError:
    print("Error: That's not a valid number!")



#Multiple Except Blocks

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Can't divide by zero!"
    except TypeError:
        return "Please use numbers only!"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "x"))


#Project: Personal Diary App
import datetime

def get_today():
    return str(datetime.date.today())

def write_entry(entry):
    try:
        with open("diary.txt", "a") as file:
            date = get_today()
            file.write(f"\n[{date}]\n{entry}\n")
        print("Entry saved!")
    except Exception as e:
        print(f"Something went wrong: {e}")

def read_diary():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("Your diary is empty.")
            else:
                print("\n--- Your Diary ---")
                print(content)
    except FileNotFoundError:
        print("No diary found yet. Write your first entry!")

def main():
    while True:
        print("\n1. Write entry")
        print("2. Read diary")
        print("3. Quit")

        choice = input("Choose: ")

        if choice == "1":
            entry = input("Write your entry: ")
            write_entry(entry)
        elif choice == "2":
            read_diary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()




