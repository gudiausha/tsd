# https://www.geeksforgeeks.org/program-print-substrings-given-string/
# O(n3)

def generate_substr(input_str):
    n = len(input_str)
    substring_list = []

    for i in range(0,n):
        for j in range(i,n):
            sub=input_str[i:j+1] #Instead of using slice, use incremental var --> O(n2)
            substring_list.append(sub)
    
    print(substring_list)

generate_substr("abc")
