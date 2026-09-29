# NUMPY ASSIGNMENT

# Question 1 -- Student Marks Array

**Problem:**
The marks obtained by five students are `[78, 65, 89, 56, 92]`. Create a
NumPy array and display the array along with its basic properties.

``` python
import numpy as np

marks = np.array([78, 65, 89, 56, 92])

print(marks)
print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Data type:", marks.dtype)
```


# Question 2 -- Student Marks Access

**Problem:**\
The marks of five students are `[72, 85, 64, 90, 76]`. Access and
display specific student marks using indexing and slicing.

``` python
import numpy as np

marks = np.array([72, 85, 64, 90, 76])

print("First:", marks[0])
print("Third:", marks[2])
print("Last:", marks[-1])
print("First 3:", marks[:3])
print("Last 2:", marks[-2:])
print("2nd to 4th:", marks[1:4])
```



# Question 3 -- Subject-wise Marks

**Problem:**\
Create an array for five students and three subjects and reshape it into
a `5 × 3` matrix.

``` python
import numpy as np

marks = np.array([
    78, 85, 90,
    65, 72, 80,
    88, 91, 84,
    56, 62, 70,
    95, 89, 92
])

student_marks = marks.reshape(5, 3)

print(student_marks)
print("Shape:", student_marks.shape)
```


# Question 4 -- Internal and External Marks

**Problem:**\
Calculate final marks using internal and external marks.

``` python
import numpy as np

internal = np.array([20, 18, 22, 19, 21])
external = np.array([65, 70, 60, 68, 72])

total = np.add(internal, external)

print("Internal:", internal)
print("External:", external)
print("Final:", total)
```


# Question 5 -- Pass Percentage Analysis

**Problem:**\
Identify students who scored 50 marks or above using Boolean masking.

``` python
import numpy as np

marks = np.array([45, 78, 56, 32, 91])

condition = marks >= 50

print(marks[condition])
```

------------------------------------------------------------------------

# Question 6 -- Average Marks

**Problem:**\
Calculate the average marks of each student in three subjects.

``` python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

avg = np.mean(marks, axis=1)

print(avg)
```

------------------------------------------------------------------------

# Question 7 -- Class Performance Statistics

**Problem:**\
Calculate total, average, highest, lowest, and standard deviation.

``` python
import numpy as np

marks = np.array([67, 82, 91, 74, 58])

total = np.sum(marks)
average = np.average(marks)
highest = np.amax(marks)
lowest = np.amin(marks)
std = np.std(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Standard Deviation:", std)
```

------------------------------------------------------------------------

# Question 8 -- Subject-wise Performance

**Problem:**\
Calculate the total marks obtained in each subject using an axis
operation.

``` python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

subject_total = marks.sum(axis=0)

print(subject_total)
```

------------------------------------------------------------------------

# Question 9 -- Student-wise Performance

**Problem:**\
Calculate the total marks obtained by each student using an axis
operation.

``` python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

student_total = marks.sum(axis=1)

print(student_total)
```

------------------------------------------------------------------------

# Question 10 -- Student Ranking

**Problem:**\
Arrange total marks in order and determine the ranking of students.

``` python
import numpy as np

marks = np.array([245, 278, 219, 290, 256])

order = np.argsort(marks)[::-1]

for rank in range(5):
    student = order[rank]
    print("Rank", rank + 1, "Student", student + 1, marks[student])
```

------------------------------------------------------------------------

# Question 11 -- Duplicate Marks Analysis

**Problem:**\
Identify unique marks from `[85, 92, 85, 76, 92]`.

``` python
import numpy as np

marks = np.array([85, 92, 85, 76, 92])

different_marks = np.unique(marks)

print(different_marks)
```

------------------------------------------------------------------------

# Question 12 -- Missing Marks

**Problem:**\
Calculate the average without considering the missing value represented
by `np.nan`.

``` python
import numpy as np

marks = np.array([78, 85, np.nan, 92, 67])

avg = np.nanmean(marks)

print(avg)
```

------------------------------------------------------------------------

# Question 13 -- Grade Classification

**Problem:**\
Classify students according to their marks.

``` python
import numpy as np

marks = np.array([95, 82, 74, 61, 45])

grades = np.select(
    [marks >= 90, marks >= 80, marks >= 70, marks >= 60],
    ["A", "B", "C", "D"],
    default="F"
)

print(grades)
```

------------------------------------------------------------------------

# Question 14 -- Random Marks Generation

**Problem:**\
Generate marks for five students using NumPy random number generation
and perform statistical analysis.

``` python
import numpy as np

np.random.seed(10)

marks = np.random.randint(0, 101, size=5)

print(marks)
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Standard Deviation:", marks.std())
```

------------------------------------------------------------------------

# Question 15 -- Student Performance Analysis

**Problem:**\
Perform a complete performance analysis using the marks of five students
in three subjects.

``` python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

total = marks.sum(axis=1)
average = marks.mean(axis=1)
highest = marks.max(axis=1)
lowest = marks.min(axis=1)

class_avg = total.mean()

above_average = np.where(total > class_avg)[0] + 1

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Class Average:", class_avg)
print("Above Class Average:", above_average)
```

------------------------------------------------------------------------
