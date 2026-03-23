def solve(n):
    def valid(current,o_count,c_count):
        if len(current)==2*n:
            ans.append(current)
            return
        if o_count<n:
            valid(current+'(',o_count+1,c_count)
        if c_count<o_count:
            valid(current+')',o_count,c_count+1)
    ans=[]
    valid('',0,0)
    print(ans)
solve(3)