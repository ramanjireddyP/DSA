class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # to set low and high
        low=0
        high=len(nums)-1
        # condition to stop
        while low<=high:
            # mid value to compare with target 
            mid=low+(high-low)//2
            #check with target 
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
    