def count_vowels(input_string):
    vowels = set("aeiou")
    count = sum(1 for char in input_string if char in vowels)
    return count

input_str = "hello world"
result = count_vowels(input_str)
print(result)
