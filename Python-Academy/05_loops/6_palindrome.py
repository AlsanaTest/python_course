# Input a number
n = int(input("Enter a number: "))

original = n      # Store original number
reverse_num = 0   # To store reversed number

# Reverse the number using loop
while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n // 10

# Check palindrome
if original == reverse_num:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")
