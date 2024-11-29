# 0 1 1 2 3 5 ..

# def fibo_series(N):
#     first_ele = 0
#     second_ele = 1

#     output_array = [0,1]

#     for i in range (1,N-1):
#         next_ele = output_array[i]+output_array[i-1]
#         output_array.append(next_ele)

#     return output_array

# output = fibo_series(8) #[0, 1, 1, 2, 3, 5, 8, 13]
# print(output)

def fibo_series_recursion(N):
    first_ele = 0
    second_ele = 1

    output_array = [0,1]

    while i<N:
        next_ele = output_array[i]+output_array[i-1]
        output_array.append(next_ele)

    return output_array

output = fibo_series_recursion(8) #[0, 1, 1, 2, 3, 5, 8, 13]
print(output)
