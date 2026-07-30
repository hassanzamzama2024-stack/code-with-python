

print("        STUDENT RECORDS ENTRY SYSTEM")

total_students = int(input("How many students do you want to enter? "))


all_students_list = []

count = 1
while count <= total_students:
    print(f"\n Enter Details for Student {count} ")
    

    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ").title() 
    physics_marks = float(input("Enter Physics Marks: "))
    chemistry_marks = float(input("Enter Chemistry Marks: "))
    mathematics_marks = float(input("Enter Mathematics Marks: "))


    marks_list = [physics_marks, chemistry_marks, mathematics_marks] 
    total_marks = sum(marks_list)
    average_marks = total_marks / 3
    percentage = (total_marks / 300) * 100

    student_dict = {
        "Student ID": student_id,
        "Student Name": student_name,
        "Physics": physics_marks,
        "Chemistry": chemistry_marks,
        "Mathematics": mathematics_marks,
        "Total Marks": total_marks,
        "Average Marks": round(average_marks, 2),
        "Percentage": round(percentage, 2)
    }

    all_students_list.append(student_dict)
    
    count = count + 1 



print("         ALL STUDENTS RECORD")

print(all_students_list) 


print(f"\nTotal Number of Students Entered: {len(all_students_list)}")
