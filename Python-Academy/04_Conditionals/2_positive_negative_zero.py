# Input a number
n = int(input("Enter a number: "))

# Check if positive, negative, or zero
if n > 0:
    result = "Positive"
elif n < 0:
    result = "Negative"
else:
    result = "Zero"

# Print the result
print("The number is:", result)
