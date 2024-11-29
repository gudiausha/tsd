int_list = [2,0,20,-5,7,-9]
target = 22
#20,7,2,0
#[0,2] or []

# a+b = c
# b = c-a

for i in range (0,len(int_list)):
    for j in range (i+1,len(int_list)):
        if int_list[i]+int_list[j] == target:
            print([i,j])
print([])
        
def third_largest(int_list):

    output_list = []

    max_ele = int_list[0]

    for i in range (0,len(int_list)):
        if int_list[i]>max_ele:
            max_ele = int_list[i]
            output_list.append(max_ele)

arr = [[1,2,3],[4,5,6],[7,8,9]]

'''
1 2 3
4 5 6
7 8 9
'''

'''
1 4 7
2 5 8
3 6 9
'''

