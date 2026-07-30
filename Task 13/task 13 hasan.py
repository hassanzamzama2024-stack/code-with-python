
student_name = input("Enter Student Name: ")
physics = float(input("Enter Physics Marks: "))
chemistry = float(input("Enter Chemistry Marks: "))
maths = float(input("Enter Mathematics Marks: "))


student = {
    "Name": student_name,
    "Physics": physics,
    "Chemistry": chemistry,
    "Maths": maths
    }

print("\nComplete Dictionary:", student)


print("Student Name:", student["Name"])

print("Physics Marks:", student["Physics"])
print("Chemistry Marks:", student["Chemistry"])
print("Maths Marks:", student["Maths"])


total = student["Physics"] + student["Chemistry"] + student["Maths"]
average = total / 3
percentage = (total / 300) * 100   

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")

student["Physics"] = float(input("\nEnter new Physics Marks to update: "))
print("Updated Physics Marks:", student["Physics"])


student["Grade"] = "A"
print("After adding Grade:", student)

del student["Grade"]
print("After removing Grade:", student)

print("\nAll Keys:", student.keys())


print("All Values:", student.values())


print("\nFinal Updated Dictionary:", student)