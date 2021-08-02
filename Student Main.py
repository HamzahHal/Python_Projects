# Importing Student Class from Student File
from Student import Student

# Creating objects with stored values inside
student1 = Student('Hamzah', 22, 'Computer Science', 'First Class', False)
student2 = Student('Galvin', 22, 'Computer Science', 'First Class', True)
student3 = Student('Shiza', float(19), 'Psychology', 'First Class', True)
student4 = Student('Rav', int(22), 'Computer Science with teaching', 'First Class', True)

# Printing Object values as a sentence
print(student2.name, 'is', student2.age, 'and is studying', student2.major)

# First print of student 4
print(student4.name, student4.age, student4.is_studying)


# Searching and replacing string characters withing a name
for i in range(3):
    for letters in student3.name:
        student3.name = student3.name.replace('a', 'S')

    print(student3.name)

# Second print of student 4 - Changing Boolean Values within an object & replacing object name
if student4.is_studying == True:
    student4.is_studying = False
    student4.name = 'Raviolio'

print(student4.name, student4.age, student4.is_studying)


