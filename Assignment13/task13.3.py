class Student:
    def __init__(self, name, age, mark1, mark2, mark3):
        """
        Represents a student with basic details and marks.
        """
        self.name = name
        self.age = age
        self.marks = [mark1, mark2, mark3]

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def total(self):
        return sum(self.marks)


name = input("Enter student name: ")
age = int(input("Enter age: "))
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

s = Student(name, age, m1, m2, m3)
s.details()
print("Total Marks:", s.total())