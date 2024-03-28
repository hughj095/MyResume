# name = "John"
# new_list = [letter for letter in name]
# print(new_list)

# double = [num*2 for num in range(1,5)]
# print(double)

#names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
# caps = [name.upper() for name in names if len(name) > 4]
# print(caps)

# numbers = [1,1,2,3,5,8,13,21,34,55]
# # sq_num = [number**2 for number in numbers]
# # print(sq_num)

# results = [item for item in numbers if item%2 == 0]
# print(results)
# import csv

# with open('./list_comp/file1.txt') as file1:
#     file_1_data = file1.readlines()
# with open('./list_comp/file2.txt') as file2:
#     file_2_data = file2.readlines()

# result = [int(num) for num in file_1_data if num in file_2_data]

# print(result)


#Dictionary Comprehension
# import random

# students_scores = {student:random.randint(1,100) for student in names}

# passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the airspeed velocity of an unladen swallow"

# result = {word:len(word) for word in sentence.split()}
# # print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {day:temp_c*(9/5)+32 for (day,temp_c) in weather_c.items()}
# print(weather_f)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)