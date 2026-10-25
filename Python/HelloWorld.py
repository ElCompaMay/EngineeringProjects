print("Hello, World!")


# 1. Variables and basic data types
name = "Ada"              # str: text
age = 12                  # int: whole number
height = 1.5              # float: decimal number
is_learning = True        # bool: True or False
nothing = None            # None: no value

print(f"\n{name} is {age} years old.")
print(f"Next year, they will be {age + 1}.")


# 2. Type conversion
number_text = "42"
number = int(number_text)
print(f"{number} + 8 = {number + 8}")

# Try converting between types with int(), float(), and str().
# user_age = int(input("How old are you? "))


# 3. Operators
first_number = 10
second_number = 3
print(first_number + second_number)  # addition
print(first_number / second_number)  # division
print(first_number // second_number) # whole-number division
print(first_number % second_number)  # remainder
print(first_number ** second_number) # exponent
print(first_number > second_number)  # comparison
print(is_learning and age < 18)      # logical operators: and, or, not


# 4. Strings
greeting = "  Hello, Python!  "
print(greeting.strip())
print(greeting.upper())
print(greeting.replace("Python", "world"))
print(f"{name} says: {greeting.strip()}")


# 5. Decisions
if age < 13:
    life_stage = "child"
elif age < 20:
    life_stage = "teenager"
else:
    life_stage = "adult"
print(f"{name} is a {life_stage}.")


# 6. Loops
for number in range(1, 4):
    print(f"Counting: {number}")

countdown = 2
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1


# 7. Collections
fruits = ["apple", "banana", "cherry"]  # list: ordered and changeable
fruits.append("orange")
print(fruits[0])                         # indexes start at 0
print(fruits)

coordinates = (4, 7)                     # tuple: ordered, not changeable
unique_numbers = {1, 2, 2, 3}            # set: unique values
person = {"name": name, "age": age}      # dict: key-value pairs
print(coordinates, unique_numbers, person["name"])

for fruit in fruits:
    print(f"I like {fruit}.")


# 8. Functions
def describe_person(person_name: str, person_age: int) -> str:
    """Return a short description of a person."""
    return f"{person_name} is {person_age} years old."


print(describe_person(name, age))


# 9. Errors and exceptions
try:
    division_result = first_number / second_number
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print(f"Division result: {division_result}")


# 10. Classes and objects
class Dog:
    """A class describes the data and behavior shared by its objects."""

    def __init__(self, dog_name: str, breed: str) -> None:
        self.name = dog_name       # instance attributes
        self.breed = breed

    def bark(self) -> str:          # instance method
        return f"{self.name} says woof!"


my_dog = Dog("Milo", "terrier")    # create an object (instance)
print(f"{my_dog.name} is a {my_dog.breed}.")
print(my_dog.bark())


# This condition is true when this file is run directly.
if __name__ == "__main__":
    print("\nTemplate finished. Try changing the values and examples!")