def digit_root(n): 
    return (n - 1) % 9 + 1 if n else 0

input = 1111
result = digit_root(input)
print(result)