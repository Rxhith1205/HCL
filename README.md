# hcl-test
# python program

## 1. Student Attendance Analysis

```python
arr = list(map(int, input().split()))

max_len = 0

for i in range(len(arr)):
    unique = []

    for j in range(i, len(arr)):
        if arr[j] in unique:
            break

        unique.append(arr[j])

    if len(unique) > max_len:
        max_len = len(unique)

print(max_len)
```

---

## 2. Online Shopping Price Analysis

```python
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
```

---

## 3. Rainwater Collection System

```python
height = list(map(int, input().split()))

water = 0

for i in range(1, len(height) - 1):

    left = max(height[:i])
    right = max(height[i + 1:])

    if left < right:
        level = left
    else:
        level = right

    if level > height[i]:
        water = water + level - height[i]

print(water)
```

---

## 4. Employee Performance Analysis

```python
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
```

---

## 5. Product Sales Analysis

```python
arr = list(map(int, input().split()))

max_product = arr[0]
min_product = arr[0]
answer = arr[0]

for i in range(1, len(arr)):

    if arr[i] < 0:
        max_product, min_product = min_product, max_product

    max_product = max(arr[i], max_product * arr[i])
    min_product = min(arr[i], min_product * arr[i])

    answer = max(answer, max_product)

print(answer)
```

---

## 6. Customer Purchase History

```python
arr = list(map(int, input().split()))

max_len = 0

for i in range(len(arr)):
    unique = []

    for j in range(i, len(arr)):
        if arr[j] in unique:
            break

        unique.append(arr[j])

    if len(unique) > max_len:
        max_len = len(unique)

print(max_len)
```

---

## 7. Bank Transaction Analysis

```python
arr = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total = total + arr[j]

        if total == target:
            count = count + 1

print(count)
```

---

## 8. Employee Skill Grouping

```python
arr = input().split()

groups = {}

for word in arr:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))
```

---

## 9. Network Packet Analysis

```python
arr = list(map(int, input().split()))

numbers = set(arr)
max_len = 0

for num in numbers:

    if num - 1 not in numbers:

        length = 1
        current = num

        while current + 1 in numbers:
            current = current + 1
            length = length + 1

        if length > max_len:
            max_len = length

print(max_len)
```

---

## 10. Hospital Appointment Scheduling

```python
n = int(input())

arr = []

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort()

result = []

for interval in arr:

    if not result or interval[0] > result[-1][1]:
        result.append(interval)

    else:
        result[-1][1] = max(result[-1][1], interval[1])

for interval in result:
    print(interval[0], interval[1])
```









# python programming

# program 1
```
a = input().split(",")
b = []
for i in a:
    n = int(i, 2)
    if n % 5 == 0:
        b.append(i)
print(",".join(b))
```

# program 2
```
a=input()
letters=0
digits=0
for i in a:
  if i.isalpha():
    letters=letters+1
  elif i.isdigit():
    digits=digits+1
print("LETTERS:",letters)
print("DIGITS:",digits)
```

# program 3
```
n=int(input())
fact = 1
for i in range(1,n+1):
  fact=fact*i
print (fact)
```

