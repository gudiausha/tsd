#Question.: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter_list = []
        for num in nums:
            typecasting_num = str(num)
            if len(typecasting_num)%2==0:
                counter_list.append(num)
        return(len(counter_list))
        
        