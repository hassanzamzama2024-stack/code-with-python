


print("        STUDENT RESULT CARD SYSTEM")


student_name = input("Enter Student Name: ")
reg_no = input("Enter Registration Number: ")
physics_marks = float(input("Enter Physics Marks: "))
chemistry_marks = float(input("Enter Chemistry Marks: "))
mathematics_marks = float(input("Enter Mathematics Marks: "))


marks_list = [physics_marks, chemistry_marks, mathematics_marks]


total_marks = sum(marks_list)
average_marks = total_marks / 3
percentage = (total_marks / 300) * 100


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


name_upper = student_name.upper()
name_lower = student_name.lower()
name_title = student_name.title()
name_length = len(student_name)

print("\n String Operations on Name ")
print(f"UPPERCASE : {name_upper}")
print(f"lowercase : {name_lower}")
print(f"Title Case: {name_title}")
print(f"Name Length: {name_length} characters")

student_record = {
    "Registration Number": reg_no,
    "Student Name": student_name,
    "Subject Marks": {
        "Physics": physics_marks,
        "Chemistry": chemistry_marks,
        "Mathematics": mathematics_marks
    },
    "Total Marks": total_marks,
    "Average Marks": round(average_marks, 2),
    "Percentage": round(percentage, 2),
    "Grade": grade
}



print("           OFFICIAL RESULT CARD")

print(f"Registration Number : {student_record['Registration Number']}")
print(f"Student Name        : {student_record['Student Name']}")

print("Subject Marks:")
print(f"  Physics     : {student_record['Subject Marks']['Physics']}")
print(f"  Chemistry   : {student_record['Subject Marks']['Chemistry']}")
print(f"  Mathematics : {student_record['Subject Marks']['Mathematics']}")

print(f"Total Marks   : {student_record['Total Marks']} / 300")
print(f"Average Marks : {student_record['Average Marks']}")
print(f"Percentage    : {student_record['Percentage']}%")
print(f"Grade         : {student_record['Grade']}")


print("        STUDENT RESULT CARD SYSTEM")


student_name = input("Enter Student Name: ")
reg_no = input("Enter Registration Number: ")
physics_marks = float(input("Enter Physics Marks: "))
chemistry_marks = float(input("Enter Chemistry Marks: "))
mathematics_marks = float(input("Enter Mathematics Marks: "))


marks_list = [physics_marks, chemistry_marks, mathematics_marks]


total_marks = sum(marks_list)
average_marks = total_marks / 3
percentage = (total_marks / 300) * 100


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


name_upper = student_name.upper()
name_lower = student_name.lower()
name_title = student_name.title()
name_length = len(student_name)

print("\n--- String Operations on Name ---")
print(f"UPPERCASE : {name_upper}")
print(f"lowercase : {name_lower}")
print(f"Title Case: {name_title}")
print(f"Name Length: {name_length} characters")


student_record = {
    "Registration Number": reg_no,
    "Student Name": student_name,
    "Subject Marks": {
        "Physics": physics_marks,
        "Chemistry": chemistry_marks,
        "Mathematics": mathematics_marks
    },
    "Total Marks": total_marks,
    "Average Marks": round(average_marks, 2),
    "Percentage": round(percentage, 2),
    "Grade": grade
}



print("           OFFICIAL RESULT CARD")

print(f"Registration Number : {student_record['Registration Number']}")
print(f"Student Name        : {student_record['Student Name']}")

print("Subject Marks:")
print(f"  Physics     : {student_record['Subject Marks']['Physics']}")
print(f"  Chemistry   : {student_record['Subject Marks']['Chemistry']}")
print(f"  Mathematics : {student_record['Subject Marks']['Mathematics']}")

print(f"Total Marks   : {student_record['Total Marks']} / 300")
print(f"Average Marks : {student_record['Average Marks']}")
print(f"Percentage    : {student_record['Percentage']}%")
print(f"Grade         : {student_record['Grade']}")

