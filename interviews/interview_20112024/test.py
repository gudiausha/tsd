# for i in range(0,100):
# 	for j in range(i+1,100):
# 		if i==j and i%j==0:
# 			break
# 		else:
# 			print(i, end=" ")

# input = pratyusha
# output = p1r1a2t1

input_str = 'pratyusha'
output = ''
# count = 0
for i in range(0,len(input_str+1)):
    count = 0
    if input_str[i] == input_str[i+1]:
        count+=1
        output += input_str[i] + str(count)
    else:
        output += input_str[i] + str(count)
print(output)