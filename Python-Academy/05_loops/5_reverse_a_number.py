# Input a number
n = int(input("Enter a number: "))

# Use loop to reverse the digits of the number
reverse_num = 0
temp = n

while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp = temp // 10

# Print the reversed number
print("Reversed number:", reverse_num)
