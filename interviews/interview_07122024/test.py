# Interview 07/12/2024

def longest_message_with_dict(message: str):
    # Count the occurrences of each character
    char_count = {}
    for char in message:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the maximum occurrence
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    # Print the result
    print(max_count)   # First line: Maximum length
    print(max_char * max_count)  # Second line: Longest substring

# Example usage
input1 = "abb"
longest_message_with_dict(input1)

input2 = "aabbddd"
longest_message_with_dict(input2)


'''
()[]{}
{()}[]
(]
{{[}]
[{]}
'''
def balance_items(input_item):
    items_map = {'(':')','{':'}','[':']'}
    stack = []
    for item in input_item:
        print(item)
        if item in ['(','{','[']:
            stack.append(item)
        elif item in [')','}',']']:
            ele = stack.pop() 
            if items_map[ele] != item:
                return False

    return True

output = balance_items('()[]{}')
print(output)

            




