# return all permutation of set
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used=[False]*len(nums)
        ans=[]
        def solve(current):
            if len(current)==len(nums):
                ans.append(current[:])
                return 
            for j ,val in enumerate(nums):
                if not used[j]:
                    print(current)
                    used[j]=True
                    solve(current+[nums[j]])
                    used[j]=False
        solve([])
        return ans