#Lists
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])   
print(fruits[2])   
fruits.append("grapes")
print(fruits)
fruits.remove("banana")
print(fruits)
print(len(fruits))
 

#for loop
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)   

for i in range(1, 6):
    print(i) 

#If/Else
age = 18

if age >= 18:
    print("You can vote!")
elif age == 17:
    print("Almost there!")
else:
    print("Too young to vote.")

# With a list
marks = [55, 80, 40, 90]

for mark in marks:
    if mark >= 60:
        print(mark, "→ Pass")
    else:
        print(mark, "→ Fail")  

#While Loops

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

number = 1

while True:
    print(number)
    number += 1
    if number > 5:
        break


#my project
students = [
    ["Abdullah", 85],
    ["Ali", 45],
    ["Sara", 70],
    ["Usman", 33]
]

print("RESULTS")
for student in students:
    name = student[0]
    score = student[1]
    if score >= 60:
        print(name, " PASS ")
    else:
        print(name, " FAIL ")