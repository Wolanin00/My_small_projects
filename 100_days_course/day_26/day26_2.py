import pandas as pd

students_dict = {
    "students": ["Max", "Abi", "Greta"],
    "score": [43, 23, 54]
}

students_data_frame = pd.DataFrame(students_dict)
print(students_data_frame)


# for key, value in students_data_frame.items():
#     print(key)

for index, row in students_data_frame.iterrows():
    print(row.students)
