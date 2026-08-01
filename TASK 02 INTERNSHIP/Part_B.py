# Q1
# with open('sample.txt','w') as f:
#     f.write('Hello')
# with open('sample.txt','a') as f:
#     f.write('\nWelcome')
# with open('sample.txt') as f:
#     print(f.read())

# Q2
# try:
#     print(10/int(input()))
# except ZeroDivisionError:
#     print('Division by zero is not allowed.')
# except ValueError:
#     print('Enter valid number.')

#Q3
# import csv
# print("Student Data from CSV File:\n")
# with open("student.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

import json
print("Student Data from JSON File:\n")
with open("student.json", "r") as file:
    data = json.load(file)
print(data)



