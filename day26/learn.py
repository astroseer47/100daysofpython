# List Comprehension
import random

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_n = n + 1
    new_list.append(add_n)

print(new_list)


new_list_2 = [n + 1 for n in numbers]
print(new_list_2)

name = "Angela"
print([l for l in name])

print([n * 2 for n in range(1,5)])

print([n * 2 for n in range(1,10) if n % 2 == 0])


names = ['Jane', 'Johnny', 'Jack', 'Dave', 'Freddy']

print([name.upper() for name in names if len(name) > 4])


# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}


names = ['Jane', 'Johnny', 'Jack', 'Dave', 'Freddy', 'Alice', 'Alex']
students_score = {name: random.randint(1,100) for name in names}
print(students_score)

passed_students = {key:val for (key,val) in students_score.items() if val > 80}
print(passed_students)


student_dict = {
    "student": ["Angela", "Johnny", "Jack", "Dave"],
    "score": [56, 66,78,90]
}

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

for (key,val) in student_df.items():
    print(key)
    print(val)

print("===================================")
for(index, row) in student_df.iterrows():
    print(row)