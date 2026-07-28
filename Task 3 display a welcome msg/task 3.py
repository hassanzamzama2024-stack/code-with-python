Python_Students = set(input("Enter Python students separated by commas: ").split(","))

Ai_Students = set(input("Enter AI students separated by commas: ").split(","))

print("\nPython Course Students:", Python_Students)
print("AI Course Students:", Ai_Students)

print("\nStudents enrolled in either course:")
print(Python_Students | Ai_Students)

print("\nStudents enrolled in both courses:")
print(Python_Students & Ai_Students)

print("\nStudents enrolled only in Python:")
print(Python_Students - Ai_Students)

print("\nStudents enrolled only in AI:")
print(Ai_Students - Python_Students)

print("\nTotal students in Python:", len(Python_Students))
print("Total students in AI:", len(Ai_Students))

Unique_Students = Python_Students | Ai_Students
print("Total Unique Students:", len(Unique_Students))

print("\n===== FINAL ANALYSIS REPORT =====")
print("Python Students:", Python_Students)
print("AI Students:", Ai_Students)
print("Either Course:", Unique_Students)
print("Both Courses:", Python_Students & Ai_Students)
print("Only Python:", Python_Students - Ai_Students)
print("Only AI:", Ai_Students - Python_Students)
print("Total Python Students:", len(Python_Students))
print("Total AI Students:", len(Ai_Students))
print("Total Unique Students:", len(Unique_Students))