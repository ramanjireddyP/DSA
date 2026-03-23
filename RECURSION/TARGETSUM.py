def solution(nums,target):
   # nums = [2, 3, 6, 7]
    #target = 7
    '''Return all combinations where:
    You can use the same number multiple times
    Sum = target'''
    res=[]
    def targetSum(index,current,targetsum):
        #base case is to return when you find targetsum==0
        if targetsum==0:
            return res.append(current[:])
        if targetsum<0 or index==len(nums):
            return None
        # include function to include the number 
        solve=targetSum(index,current+[nums[index]],targetsum-nums[index])

        # to return when you find solution rather than exploring all
        #if solve:
            #return solve
        
        #exclude the number and check another number in array
        return targetSum(index+1,current,targetsum)

    #function calling 

    (targetSum(0,[],target))
    print(res)
nums=[2,3,6,7]
target=7

solution(nums,target)

