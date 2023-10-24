#Prob Link.: https://www.codingninjas.com/studio/problems/second-largest-element-in-the-array_873375?leftPanelTab=1

#Brute Force Approach
#TC.: O(n) (ignoring the inbuilt sort method)
#SC.: O(1)
def findSecondLargest(sequenceOfNumbers):
    #var initialization
    largest_index=0
    second_largest_index=0
    is_compared=0

    #inplace array sort
    sequenceOfNumbers.sort()

    #loop thro' to compare the values and store the respective indexes
    for i in range(0,len(sequenceOfNumbers)-1):
        if sequenceOfNumbers[i]<sequenceOfNumbers[i+1]:
            is_compared+=1
            largest_index = i+1
            second_largest_index = i
    
    #for duplicate values --> [9,9,9] / [-1,-1,-1]
    if is_compared==0:
        return -1
    return sequenceOfNumbers[second_largest_index]
    

#Best Approach
#TC.: O(1) --> ignoring the inbuilt sort method
#SC.: O(1)
def findSecondLargest(sequenceOfNumbers):
    #remove the duplicates
    arr = list(set(sequenceOfNumbers))
    
    #sort using the inbuilt method
    arr.sort()
    
    #len(arr) will be less than 2 if dupes are present
    #as we are performing set operation
    #and only one element will be available
    if len(arr)<2:
        return -1
    #return second largest element
    return a[-2]