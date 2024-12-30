'''
Patterns - Logical Warm Up excercise
'''

def matrix_pattern(N):
    for row in range(0,N):
        for col in range(0,N):
            print("*", end='  ')
        print()

def right_angled_triangle_pattern(N):
    '''
    Different varieties by changing the second loop and print statements
    '''
    for row in range(0,N):
        for col in range(0,row+1):
            print("*",end = '  ')
        print()

    for row in range(1,N+1):
        for col in range(1,row+1):
            print(row,end = '  ')
        print()

def inverted_right_pyramid(N):
    for row in range(0,N):
        for col in range(N,row,-1):
            print("*", end = ' ')
        print()

    for row in range(1,N):
        for col in range(row,N,1):
            print(col, end = ' ')
        print()

inverted_right_pyramid(4)
