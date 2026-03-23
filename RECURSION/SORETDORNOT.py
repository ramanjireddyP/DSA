def solve(nums):
    def check(index):
        if index==len(nums)-1:
            return True
        if nums[index]>nums[index+1]:
            return False
        return check(index+1)
        
        
    print(check(0))
solve([1,2,3,4])