# Python Assignments
# Author: Adithya V
# Date: 29/09/2026


# 1. Print All Prime Numbers Between Input Range
~~~

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")

for number in range(start, end + 1):
    if number > 1:
        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(number, end=" ")

print()
~~~


# 2. Factorial Using Recursion
~~~

def find_factorial(value):
    if value <= 1:
        return 1

    return value * find_factorial(value - 1)


num = int(input("\nEnter a number for factorial: "))

result = find_factorial(num)

print("Factorial:", result)
~~~


# 3. Square of Numbers Using Lambda
~~~

numbers = [1, 2, 3, 4, 5]

find_square = lambda num: num ** 2

squares = list(map(find_square, numbers))

print("\nNumbers:", numbers)
print("Squares:", squares)
~~~


# 4. Find the Second Largest Element in a List
~~~

numbers = [10, 25, 7, 45, 32, 18]

values = sorted(set(numbers), reverse=True)

second_largest = values[1]

print("\nList:", numbers)
print("Second largest element:", second_largest)
~~~


# 5. Count Frequency of Characters in a String
~~~

text = input("\nEnter a string: ")

frequency = {}

for letter in text:
    frequency[letter] = frequency.get(letter, 0) + 1

print("Character frequency:")

for letter in frequency:
    print(letter, ":", frequency[letter])
~~~


# 6. Calculate Area of a Circle Using Math Library
~~~

import math

radius = float(input("\nEnter radius of the circle: "))

circle_area = math.pi * (radius ** 2)

print("Area of the circle:", circle_area)
~~~


# 7. Reverse a String Without Using Built-in Reverse
~~~

text = input("\nEnter a string to reverse: ")

result = ""

for index in range(len(text) - 1, -1, -1):
    result += text[index]

print("Original string:", text)
print("Reversed string:", result)
~~~


# 8. Remove Duplicates from a List
~~~

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = []

for value in numbers:
    if value not in result:
        result.append(value)

print("\nOriginal list:", numbers)
print("List after removing duplicates:", result)
~~~


# 9. Merge Two Dictionaries
~~~

dict1 = {
    "name": "Adithya",
    "age": 21
}

dict2 = {
    "department": "CSE",
    "college": "Engineering College"
}

merged = dict1.copy()
merged.update(dict2)

print("\nFirst dictionary:", dict1)
print("Second dictionary:", dict2)
print("Merged dictionary:", merged)

~~~


# 10. Fibonacci Series Using Recursion
~~~

def fibonacci(term):
    if term == 0:
        return 0
    elif term == 1:
        return 1
    else:
        return fibonacci(term - 1) + fibonacci(term - 2)


terms = int(input("\nEnter number of Fibonacci terms: "))

print("Fibonacci series:")

for term in range(terms):
    print(fibonacci(term), end=" ")

print()
~~~
