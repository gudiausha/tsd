def is_str_palindrome(input_str):
    input_str = input_str.replace(" ","")
    # print(input_str)
    i = 0
    j = len(input_str)-1

    while i < j:
        if input_str[i] != input_str[j]:
            return False
        else:
            i +=1
            j -=1
    return True

is_palindrome = is_str_palindrome("hello world")
print(is_palindrome)

# Test Cases:
# Basic palindrome (odd length)

# Input: "madam"
# Expected Output: True
# Basic palindrome (even length)

# Input: "abba"
# Expected Output: True
# Non-palindrome string

# Input: "abcdef"
# Expected Output: False
# String with spaces (palindrome)

# Input: "nurses run"
# Expected Output: True
# String with spaces (non-palindrome)

# Input: "hello world"
# Expected Output: False
# Single character (palindrome)

# Input: "a"
# Expected Output: True
# Empty string (palindrome)

# Input: ""
# Expected Output: True
# String with mixed cases (case-sensitive test)

# Input: "Madam"
# Expected Output: False
# String with special characters (palindrome)

# Input: "A man a plan a canal Panama"
# Expected Output: False
# (This will fail because the function does not handle case-sensitivity or special characters)
# String with numbers (palindrome)

# Input: "12321"
# Expected Output: True
# String with numbers (non-palindrome)

# Input: "12345"
# Expected Output: False
# String with leading/trailing spaces

# Input: " racecar "
# Expected Output: True