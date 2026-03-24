class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)-1
        col=len(matrix[0])-1
        low=0
        high=row
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid][0]<=target<=matrix[mid][col]:
                ans= mid
                break
            elif matrix[mid][col]<target:
                low=mid+1
            else:
                high=mid-1
        low=0
        high=col
        if ans==-1:
            return False
        while low<=high:
            mid=(low+high)//2
            if matrix[ans][mid]==target:
                return True
            elif matrix[ans][mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False
    

        
        