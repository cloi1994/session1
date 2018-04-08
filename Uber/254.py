def getFactors(n):
    res = []
    dfs(2,n,[],res)
    return res

def dfs(start,target,tmp,res):
    if target == 1:
        if len(tmp) > 1:
            res.append(tmp[:])
        return

    if target < 1:
        return

    for i in range(start,target+1):
        if target % i == 0:
            tmp.append(i)
            dfs(i,target/i,tmp,res)
            tmp.pop()


print getFactors(1)
print getFactors(37)
print getFactors(12)
print getFactors(32)
print getFactors(8)
