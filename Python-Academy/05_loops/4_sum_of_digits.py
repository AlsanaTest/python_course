# Input a number
n = int(input("Enter a number: "))

# Use loop to extract digits (using % and //)
sum_digits = 0
product_digits = 1

# Maintain sum of digits
temp = n

# Maintain product of digits
while temp > 0:
    digit = temp % 10        # Extract last digit
    sum_digits += digit      # Add to sum
    product_digits *= digit  # Multiply to product
    temp = temp // 10        # Remove last digit

# Print both values
print("Sum of digits:", sum_digits)
print("Product of digits:", product_digits)
