class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        ans=[]
        found=False
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                high=mid-1
                found=True
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if not found:
            return[-1,-1]
        ans.append(low)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        ans.append(high)
        return ans 
