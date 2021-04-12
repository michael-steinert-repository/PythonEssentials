if __name__ == '__main__':
    print("Python is Awesome")

# Dynamically Typed
name = "Michael"
age = 27
weight = 72.1
isTrue = True

print(type(name))
print(type(age))
print(type(weight))
print(type(isTrue))

# Typed
isFalse: bool = False


def my_function() -> int:
    return 42


print(my_function())

# Strings
print(name.lower())

print(len(name))

comment = """
Long Comment
in {} Multilines
    """
print(comment.format(2))


# Indentation
def print_full_name():
    surname = "Steinert"
    print(name + " " + surname)


print_full_name()

# Control Flow
number = 42

if number > 0 and number > 10:
    print(f"Number {number} is positive and greater than 10")
elif number == 0:
    print(f"Number {number} is less than 10")
else:
    print(f"Number {number} is negative and less than 10")

# Ternary If Statement
message = "positive" if number >= 0 else "negative"
print(message)

# List
numbers = [1, 2, 3, [3.1, 3.2, 3.3]]
print(f"Length of List is {len(numbers)}")
number = 3
print(f"Is {number} in List? {number in numbers}")
print(numbers[2])
print(numbers[3])
print(numbers[3][2])
# Adding Item to List
numbers[3].append(3.4)
print(numbers[3][3])
# Removing Item at Index 3
del numbers[3]
print(numbers)
# Removing Range from Index 0 to 2
del numbers[0:2]
print(numbers)

# Sets: In Sets are Duplicates not allowed
numbers_set = {1, 1, 2, 3}
print(numbers_set)

letters_a = {"A", "B"}
letters_b = {"B", "C", "D"}
# Set Union
union = letters_a | letters_b
print(f"Union: {union}")
# Set Intersection
intersection = letters_a & letters_b
print(f"Intersection: {intersection}")
# Set Difference
difference = letters_a - letters_b
print(f"Difference: {difference}")

# Dictionaries
person = {
    "name": "Michael",
    "age": 27
}
print(f"Value of Dictionary: {person['name']} {person['age']}")

# Loops
for letter in letters_a:
    print(letter)

for key in person:
    print(f"Key: {key} Value: {person[key]}")

for key, value in person.items():
    print(f"Key: {key} Value: {value}")

result = 0
for number in numbers_set:
    result += number
print(f"Result of Adding {numbers_set} is {result}")

number = 0
while number < 4:
    print(number)
    number += 1
    if number > 2:
        continue
else:
    print("End of While Loop")


# Functions
def greet(name, age = -1):
    if age >= 0:
        print(f"Hello {name} {age} Years old")
    else:
        print(f"Hello {name}")


greet("Michael", 27)

greet("Michael")

# Modules
import calculator
print(calculator.add(1, 2))


# Classes
class Phone:
    def __init__(self, brand, phone_number):
        self.brand = brand
        self.phone_number = phone_number

    def call(self) -> None:
        print(f"Phone calling {self.phone_number}")

    def __str__(self) -> str:
        return f"Brand {self.brand} PhoneNumber {self.phone_number}"


phone = Phone("Pixel 6", "0172")

print(phone)
phone.call()

# Dates
from datetime import datetime

print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())

now = datetime.now()
print(now.strftime("%d.%m.%Y"))
print(now.strftime("%H:%M:%S"))

# Files
# w Writing - a Appending - r Reading
file = open("./data.csv", "w")
file.write("Hello World")
file.close()

file = open("./data.csv", "r")
print(file.read())

for line in file:
    print(line)

file.close()

import os.path
filename = "./data.csv"
if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"File {filename} does not exist.")

# Fetching Data
from urllib import request
import json


class Todo:
    def __init__(self, id, title, completed) -> None:
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self) -> str:
        return f"ID {self.id} Todo {self.title} Completed {completed}"


todos = []

url = "https://jsonplaceholder.typicode.com/todos/"
response = request.urlopen(url)
if response.getcode() == 200:
    json_data = json.loads(response.read())
    for data in json_data:
        id = data["id"]
        title = data["title"]
        completed = data["completed"]
        todo = Todo(id, title, completed)
        todos.append(todo)
print(len(todos))


# Installed Requests and Text-to-Speech with Pip3
import requests
import pyttsx3

response = requests.get(url)
if response.status_code == 200:
    json_data = json.loads(response.text)
    for data in json_data:
        id = data["id"]
        title = data["title"]
        completed = data["completed"]
        todo = Todo(id, title, completed)
        todos.append(todo)

for todo in todos:
    pyttsx3.speak("ID")
    pyttsx3.speak(todo.id)
    pyttsx3.speak("Title")
    pyttsx3.speak(todo.title)
    pyttsx3.speak("Completed")
    pyttsx3.speak(todo.completed)