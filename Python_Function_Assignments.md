# Python Function Assignments

# 1. Calculator Function
~~~

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print(calculate(num1, num2, op))
~~~


# 2. Sum of Numbers Using *args
~~~

def sum_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


print(sum_numbers(10, 20, 30, 40))
~~~


# 3. Employee Information Using **kwargs
~~~

def employee(**args):
    for key, value in args.items():
        print(key, ":", value)


employee(
    name="Adithya",
    ID=101,
    department="CSE",
    salary=30000
)
~~~


# 4. Remove Duplicates from a List
~~~

def remove_duplicates(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)

    return unique


numbers = [10, 20, 10, 30, 20, 40, 30]

print(remove_duplicates(numbers))
~~~


# 5. Sort List of Tuples Using Lambda
~~~

data = [(1, 5), (2, 3), (4, 1)]

sorted_data = sorted(data, key=lambda item: item[1])

print(sorted_data)
~~~
