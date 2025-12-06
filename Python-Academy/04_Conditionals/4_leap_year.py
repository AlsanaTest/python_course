# Input a year
year = int(input("Enter a year: "))

# Check if divisible by 4
if year % 4 == 0:
    result = "Leap year"
else:
    result = "Not a leap year"

# Print if leap year or not
print(result)
