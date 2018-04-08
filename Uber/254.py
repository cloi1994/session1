def getFactors(n):
    res = []
    dfs(2,n,n,[],res)
    return res

def dfs(start,n,target,tmp,res):
    if target == 1:
        if len(tmp) > 1:
            res.append(tmp[:])
        return

    if target < 1:
        return

    for i in range(start,n):
        if n % i == 0:
            tmp.append(i)
            dfs(i,n,target/i,tmp,res)
            tmp.pop()


print getFactors(1)
print getFactors(37)
print getFactors(12)
print getFactors(32)
print getFactors(8)
