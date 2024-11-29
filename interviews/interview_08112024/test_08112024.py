'''
input2 =  'aaaabbtab' 
output = 'a4b2t1a1b1'
'''

def prob1(input_str):
    n = len(input_str)
    count = 0 #must have been count=1
    output_str = ''
    for char in range(0,n-1):
        if input_str[char]==input_str[char+1]:
            count+=1
        else:
            output_str+=input_str[char]+str(count)
            count=0
    return output_str

ans = prob1('aaaabbtab')
print(ans) #a3b1t0a0


