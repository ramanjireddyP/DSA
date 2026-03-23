# to return all subsets of a set 
def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def solution(index,current):
            if index==len(nums):
                ans.append(current[:])
                return None
            solution(index+1,current+[nums[index]])
            solution(index+1,current)
        ans=[]
        solution(0,[])
        return ans