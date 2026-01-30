# Problem 76: Calculate string similarity (common characters)
# Find and fix the error
def string_similarity(str1, str2):
    str2_list = list(str2)  # convert to list to mark used characters
    common = 0
    for char in str1:
        if char in str2_list:
            common += 1
            str2_list.remove(char)  # remove matched character
    return common

s1 = "hello"
s2 = "world"
print(f"Common characters: {string_similarity(s1, s2)}")
