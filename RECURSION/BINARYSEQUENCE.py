# to generante n binary seqence where two ones not to gether 
def solution(n):
    def binary(index,current):
        if index==n:
            ans.append(current)
            return 
        binary(index+1,current+'0')
        if not current or  current[-1]!='1':
             binary(index+1,current+'1')  
    binary(0,'')
ans=[]
solution(3)
print(ans)