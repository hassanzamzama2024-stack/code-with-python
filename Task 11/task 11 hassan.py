
reg = input("Registration Number: ")
name = input("Student Name: ")
dept = input("Department: ")
sem = input("Semester: ")


profile = (reg, name, dept, sem)

print("\nComplete Profile:", profile)


print("\nEach Item Separately:")
print("Reg No:", profile[0])
print("Name:", profile[1])
print("Department:", profile[2])
print("Semester:", profile[3])

print("\n Name Operations ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Length:", len(name))


print("\nTotal items in tuple:", len(profile))


print("First two:", profile[0:2])
print("Last two:", profile[2:4])