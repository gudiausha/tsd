#bruteforce - 2/4 test cases passed
#finds the count to alternate 0's and 1's but not
#the min count

def makeBeautiful(str):
	# Write your code here
	str_list = list(str)
	c=0
	for i in range(0,len(str)-1):
		if str_list[i]=='0':
			if str_list[i+1] !='1':
				c+=1
				str_list[i+1]='1'
		elif str_list[i]=='1':
			if str_list[i+1]!='0':
				c+=1
				str_list[i+1]='0'
		else:
			c+=0
	return c			
	# pass