print("      Welcome to Number Analyzer")

number = float(input("Enter a number: "))


square = number ** 2

 
cube = number ** 3


absolute_val = abs(number)


print("           ANALYSIS REPORT")

print(f"Entered Number : {number}")


if number > 0:
    print("Type          : Positive Number")

    half = number / 2
    double = number * 2
    print(f"Half          : {half}")
    print(f"Double        : {double}")
elif number < 0:
    print("Type          : Negative Number")
else:
    print("Type          : Zero")


print(f"Square        : {square}")


print(f"Cube          : {cube}")


print(f"Absolute Value: {absolute_val}")
