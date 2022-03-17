#Take marks as input and print grades of the student

marks = int(input("marks:"))

if marks >= 80:
    print("Grade = 'A'")
elif marks >= 60:
    print("Grade = 'B'")
elif marks >= 40:
    print("Grade = 'C'")
else:
    print("Fail")
