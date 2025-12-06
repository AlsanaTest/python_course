# Input marks from 0 to 100
marks = int(input("Enter marks: "))

# Use conditions to assign grade
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"

# Print the grade
print("Grade:", grade)
