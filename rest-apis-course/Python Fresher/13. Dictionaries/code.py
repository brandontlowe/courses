# friend_ages = {"Rolf": 25, "Adam": 30, "Anne": 27}
# print(friend_ages["Rolf"])

# friend_ages["Christina"] = 28
# print(friend_ages)

# friends = [
#     {"name": "James", "age": 27},
#     {"name": "Anna", "age": 28},
#     {"name": "Fred", "age": 31}
# ]

# print(friends[1]["age"])

student_attendance = {"Rolf": 96, "Jessica": 92, "Daniel": 79}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")

if "Bob" in student_attendance:
    print(f"Bob's attendance this year is {student_attendance['Rolf']}%")
else:
    print("Bob is not a student")

attendance_values = student_attendance.values()
print(f"Average student attendance is {sum(attendance_values) / len(attendance_values)}")