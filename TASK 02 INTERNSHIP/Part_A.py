# QUESTION 01 -- DEMONSTATE DIFFERENT DATA TYPES --
# age=21
# gpa=3.85
# is_passed=True
# name='Ali Raza'
# subjects=['Python','AI','ML']
# coordinates=(33.6844,73.0479)
# student={'name':name,'age':age,'gpa':gpa}
# unique_skills={'Python','SQL','Git'}
# print(name)
# print(age)
# print(gpa)
# print(is_passed)
# print(subjects)
# print(coordinates)
# print(student)
# print(unique_skills)


# QUESTION 02 -- USER-DEFINED FUNCTIONS --

# def calculate_average(marks):
#     return sum(marks)/len(marks)
# marks=[88,92,79,95]
# print("Average marks : ",calculate_average(marks))


# Function to calculate the area of a rectangle

# def calculate_area(length, width):
#     area = length * width
#     return area

# length = 8
# width = 5

# print("Area =", calculate_area(length, width))

#QUESTION 03 -- COMPREHENSION
# numbers=range(1,11)
# even_squares=[n**2 for n in numbers if n%2==0]
# print("-----LIST COMPREHENSION----")
# print(even_squares)
# print("****************************************")
# squares_dict={n:n**2 for n in range(1,6)}
# print("-----DICTIORNARY COMPREHENSION----")
# print(squares_dict)

# QUESTION 04 -- OOPS -- 
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#         return f"Hi, I'm {self.name}"
# class Student(Person):
#     def __init__(self,name,age,roll,program):
#         super().__init__(name,age)
#         self.program=program
#         self.roll = roll
#     def introduce(self):
#         return f" I'm  a student of {self.program} with roll number {self.roll}"
# p=Person('Bilal',20)
# print(p.introduce())
# s=Student("Bilal",20,131,"BSCS")
# print(s.introduce())


