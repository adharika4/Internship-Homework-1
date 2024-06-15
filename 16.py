# QUESTION 16
input_string = "hello world"
frequency = {}

for char in input_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)