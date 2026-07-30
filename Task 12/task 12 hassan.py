
python = {"Ali", "Ahmed", "Sara", "Fatima", "Ali"}

ai = {"Sara", "Fatima", "Usman", "Zain", "Sara"}

print("Python Students:", python)
print("AI Students:", ai)

print("\nStudents in either course:", python | ai)

print("Students in both courses:", python & ai)

print("Only in Python:", python - ai)


print("Only in AI:", ai - python)

print("\nTotal in Python:", len(python))
print("Total in AI:", len(ai))

all_students = python | ai
print("Total unique students:", len(all_students))



print("Python class:", python)
print("AI class:", ai)
print("Common students:", python & ai)
print("Only Python:", python - ai)
print("Only AI:", ai - python)
print("Total unique students:", len(all_students))
