def solve(nums):
    def maximum(nums):
        if len(nums)==1:
            return nums[0]
        return max(nums[0],maximum(nums[1:]))
    print(maximum(nums))
print(solve([1,2,5,3,8,5,9,0]))
