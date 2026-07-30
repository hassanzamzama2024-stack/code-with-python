
name = input("Student Name: ")
m1 = float(input("Subject 1 Marks: "))
m2 = float(input("Subject 2 Marks: "))
m3 = float(input("Subject 3 Marks: "))
m4 = float(input("Subject 4 Marks: "))
m5 = float(input("Subject 5 Marks: "))


marks = [m1, m2, m3, m4, m5]


print("Marks List:", marks)


total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = total / 5  


highest = max(marks)
lowest = min(marks)



print("Name in Capital:", name.upper())
print("Name in Small:", name.lower())
print("Name Length:", len(name))


print("\nSTUDENT REPORT ")
print("Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage, "%")
print("Highest:", highest)
print("Lowest:", lowest)