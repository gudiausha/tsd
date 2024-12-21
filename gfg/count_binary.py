# https://www.geeksforgeeks.org/check-for-binary-string/
# Input: s = "01010101010"
# Output: true

# Input: s = "geeks101"
# Output: false 

# Input: s = "1234101"
# Output: false

def check_binary_str(input_str):
    for char in input_str:
        # print(char,type(char))
        if char not in ['0','1']: #if char != '0' and char != '1':  # Check if the character is neither '0' nor '1'
            return False
    return True

output = check_binary_str("01010101010")
print(output)