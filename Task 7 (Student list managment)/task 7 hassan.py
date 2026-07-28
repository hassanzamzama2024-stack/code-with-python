

students = ["Ali", "Sara", "Ahmed", "Fatima", "Usman"]
print("Complete list:", students)


students.append("Zainab")
print("After adding new student:", students)


students.insert(0, "Bilal")
print("After adding at beginning:", students)

students[2] = "Ayesha"
print("After changing 3rd student:", students)

students.remove("Ahmed")
print("After removing Ahmed:", students)


students.pop()
print("After removing last student:", students)


position = students.index("Fatima")
print("Position of Fatima:", position)

print("Total number of students:", len(students))

print("Final updated list:", students)