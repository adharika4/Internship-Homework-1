# QUESTION 18
def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
string1 = "listen"
string2 = "silent"
if check_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")