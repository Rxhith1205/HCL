# hcl-test
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

