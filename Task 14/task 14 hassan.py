
students = {

    "S101": {
        "Registration Number": "S101",
        "Name": "Umer",
        "Department": "Computer Science",
        "Semester": 3,
        "CGPA": 3.42
    },
    "S102": {
        "Registration Number": "S102",
        "Name": "Ayesha",
        "Department": "Software Engineering",
        "Semester": 4,
        "CGPA": 3.78
    },
    "S103": {
        "Registration Number": "S103",
        "Name": "Bilal",
        "Department": "Information Technology",
        "Semester": 2,
        "CGPA": 3.15
    },
    "S104": {
        "Registration Number": "S104",
        "Name": "Zainab",
        "Department": "Data Science",
        "Semester": 5,
        "CGPA": 3.90
    },
    "S105": {
        "Registration Number": "S105",
        "Name": "Ahmed",
        "Department": "Artificial Intelligence",
        "Semester": 1,
        "CGPA": 3.60
    }
}


print("3. Complete Nested Dictionary:")
print(students)


print("\n4. Complete Information of First Student:")
print(students["S101"])


print("\n5. Name of Second Student:")
print(students["S102"]["Name"])

print("\n6. Department of Third Student:")
print(students["S103"]["Department"])

print("\n7. Semester of Fourth Student:")
print(students["S104"]["Semester"])


print("\n8. CGPA of Fifth Student:")
print(students["S105"]["CGPA"])


students["S103"]["CGPA"] = 3.50
print("\n9. Updated CGPA of S103:", students["S103"]["CGPA"])


students["S102"]["University"] = "NUST"
print("\n10. After Adding University to S102:")
print(students["S102"])

del students["S102"]["University"]
print("\n11. After Removing University from S102:")
print(students["S102"])


print("\n12. Keys of First Student:", students["S101"].keys())
print("    Values of First Student:", students["S101"].values())

print("\n13. Final Updated Nested Dictionary:")
print(students)