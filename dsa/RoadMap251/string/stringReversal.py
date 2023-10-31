def reverseStringWordWise(string):
    output_list = string.split()
    reversed_string = (' ').join(output_list[::-1])
    return reversed_string

string = input()
ans = reverseStringWordWise(string)
print(ans)
        
