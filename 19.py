# QUESTION 19
import string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))
input_string = "Hello, World! This is a test string."
output_string = remove_punctuation(input_string)
print("Input string:", input_string)
print("String without punctuation:", output_string)