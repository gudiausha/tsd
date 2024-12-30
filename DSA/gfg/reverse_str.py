# https://www.geeksforgeeks.org/reverse-a-string/
# [::-1]

def reverse_str(input_str):
    left_ptr = 0
    right_ptr = len(input_str)-1

    input_str_list = list(input_str)
    while left_ptr<right_ptr:
        input_str_list[left_ptr],input_str_list[right_ptr] = input_str_list[right_ptr],input_str_list[left_ptr]
        left_ptr+=1
        right_ptr-=1
    
    return ''.join(input_str_list)

output = reverse_str("abdcfe")
print(output)