#Functions
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

greet("Abdullah")
result = add(10, 5)
print(result)

#Dictionaries
student = {
    "name": "Abdullah",
    "age": 18,
    "city": "Lahore"
}

print(student["name"])
print(student["age"])

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

#Nested Dictionaries
students = {
    "student1": {"name": "Abdullah", "grade": "A"},
    "student2": {"name": "Ali", "grade": "B"}
}

for student_id, info in students.items():
    print(f"{student_id} -> Name: {info['name']}, Grade: {info['grade']}")

#F-strings
name = "Abdullah"
age = 18
city = "Lahore"

print(f"My name is {name}, I am {age} years old and I live in {city}.")
print(f"Next year I'll be {age + 1}.")


#Functions Calling Functions
def get_full_name(first, last):
    return f"{first} {last}"

def introduce(first, last, age):
    full_name = get_full_name(first, last)
    print(f"Hi! My name is {full_name} and I am {age} years old.")

introduce("Muhammad", "Abdullah", 18)


#Project: Student Report Card
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    return sum(scores) / len(scores)

def print_report(student):
    name = student["name"]
    scores = student["scores"]
    average = calculate_average(scores)
    grade = get_grade(average)

    print(f"\n--- Report Card for {name} ---")
    for subject, score in scores.items():
        print(f"  {subject}: {score}")
    print(f"  Average: {average:.1f}")
    print(f"  Final Grade: {grade}")

# Data
students = {
    "student1": {
        "name": "Abdullah",
        "scores": {"Math": 92, "English": 85, "Science": 78}
    },
    "student2": {
        "name": "Ali",
        "scores": {"Math": 70, "English": 65, "Science": 80}
    }
}

# Run report for all students
for key, student in students.items():
    print_report(student)