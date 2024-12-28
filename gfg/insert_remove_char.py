# https://www.geeksforgeeks.org/how-to-insert-characters-in-a-string-at-a-certain-position/

# Input: str = “geeksforgeeks”, chars = [1, 5, 7, 9]
# Output: g*eeks*fo*rg*eeks
# Explanation: The indices 1, 5, 7, and 9 correspond to the bold characters in “geeksforgeeks”.


# Input: str = “spacing”, chars = [0, 1, 2, 3, 4, 5, 6]
# Output: “*s*p*a*c*i*n*g”

def insert_char(input_str,char_positions):
    char_positions = set(char_positions)# Convert to set for O(1) lookups
    output_str = ''
    for ind,val in enumerate(input_str):
        if ind in char_positions:
            output_str+='*'
        output_str+=val
    return output_str

output = insert_char("spacing",[0, 1, 2, 3, 4, 5, 6])
print(output)

# https://www.geeksforgeeks.org/remove-all-occurrences-of-a-character-in-a-string/
# Input : s = “geeksforgeeks”
#         c = ‘e’
# Output : s = “gksforgks”

# Input : s = “geeksforgeeks”
#         c = ‘g’
# Output : s = “eeksforeeks”

# Input : s = “geeksforgeeks”
#         c = ‘k’
# Output : s = “geesforgees”

def remove_char(input_str,char):
    output = input_str.replace(char,'')
    print(output)

remove_char("geeksforgeeks",'e')
