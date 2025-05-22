################ YASİN ASLAN ################
################ Python Exercises ################

###############################################
# TASK 1: Examine the data types of the given variables.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4, "String", 3.2, False]
type(l)

d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)




###############################################
# TASK 2: Convert all characters in the given string to uppercase.
# Replace commas and periods with spaces, and then split the string into words.
###############################################

text = "The goal is to turn data into information, and information into insight."


new_text = text.upper()
new_text = new_text.replace(",", " ")
new_text = new_text.replace(".", " ")
new_text.split()
words = new_text.split()
print(words)


###############################################
#TASK 3: Perform the following operations for the given list.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Check the number of elements in the given list.
# Step 2: Call the elements at the zeroeth and tenth index.
# Step 3: Create a new list ["D", "A", "T", "A"] from the given list.
# Step 4: Delete the element at the eighth index.
# Step 5: Add a new element.
# Step 6: Add the element "N" back to the eighth index.

# Step 1
len(lst)

# Step 2
lst[0]
lst[10]

# Step 3
data_list = lst[0:4]  # Slice from index 0 up to (but not including) index 4.
data_list

# Step 4
lst.pop(8)
lst

# Step 5
lst.append(101)
lst

# Step 6
lst.insert(8, "N")
lst

###############################################
# TASK 4: Apply the following steps to the given dictionary structure.
###############################################
d = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
# Step 1: Access the key values.
# Step 2: Access the values.
# Step 3: Update the value 12 for the 'Daisy' key to 13.
# Step 4: Add a new key-value pair where the key is 'Ahmet' and the value is [Turkey, 24].
# Step 5: Delete 'Antonio' from the dictionary.

# Step 1
d.keys()

# Step 2
d.values()

# Step 3
d["Daisy"][1] = 13
d

# Step 4
d["Ahmet"] = ["Turkey", 24]
d

# Step 5
d.pop("Antonio")
d

###############################################
# TASK 5: Write a function that takes a list as an argument, separates odd and even numbers into separate lists, and returns these lists.
###############################################

l = [2, 13, 18, 93, 22]

def func(lst):
    cift_list = []
    tek_list = []
    for i in lst:
        if i % 2 == 0:
            cift_list.append(i)
        else:
            tek_list.append(i)

    return cift_list, tek_list
func(l)

# TASK 6: The list below contains the names of students who graduated with honors from engineering and medicine faculties.
# The first three students represent the ranking of the Faculty of Engineering, while the last three students belong to the ranking of the Faculty of Medicine.
# Using enumerate, print the student rankings specific to each faculty.

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

# General enumerate example
print("--- General Student List ---")
for index, student_name in enumerate(students):
    print(f"Index: {index}, Student Name: {student_name}")

# Faculty-specific ranking
print("\n--- Student Rankings by Faculty ---")
for index, student_name in enumerate(students):
    if index < 3:
        rank = index + 1
        print(f"Engineering Faculty {rank}. student: {student_name}")
    else:
        rank = index - 2
        print(f"Medicine Faculty {rank}. student: {student_name}")

# TASK 7: Three lists are given below. The lists contain course codes, credits, and capacity information, respectively. Print the course information using zip.
# This task highlights the zip() function, which is excellent for combining elements from multiple iterables (like lists) into single tuples, element by element.

course_codes = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credits = [3, 4, 2, 4]
capacity = [30, 75, 150, 25]


for code, credit, cap in zip(course_codes, credits, capacity):
    print(f"Course: {code}, Credit: {credit}, Capacity: {cap}")

# TASK 8: Two sets are given below. You are expected to define a function that prints the common elements if the first set covers the second set, and if not, prints the difference of the second set from the first set.
# This task delves into set operations like issuperset() (checking if one set contains all elements of another), intersection() (finding common elements), and difference() (finding elements unique to one set).



set1 = {"data", "python"}
set2 = {"data", "function", "qcut", "lambda", "python", "miuul"}

def compare_sets(s1, s2):
    if s1.issuperset(s2):
        print("Common elements:", s1.intersection(s2))
    else:
        print("Different elements:", s2.difference(s1))

compare_sets(set1, set2)

