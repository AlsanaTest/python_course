def total_sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s
 
print(total_sum(7, 3))
print(total_sum(1, 3, 5, 14, 6))