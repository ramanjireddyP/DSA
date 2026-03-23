def solution(nums,target):
    def subsetSum(index,currentSum):
        # base case to check current sum ==0 return 
        if currentSum==0:
            return True
        if currentSum<0 or index==len(nums):
            return None
        # to include a number from nums
        res=subsetSum(index+1,currentSum-nums[index])
        
        # to early return to true
        if res :
            return res
        # to exclude a number
        return subsetSum(index+1,currentSum)
    print(subsetSum(0,target))
nums = [3, 1, 2]
target = 3
'''Return True if any subset sums to target
Otherwise return False'''
solution(nums,target)