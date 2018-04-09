

def nextClosestTime(strs):
    s = map(int,list(strs.replace(':','')))

    hours = s[0] * 10 + s[1]
    mins = s[2] * 10 + s[3]

    now = hours*60+mins

    ans = [now]

    dfs(s,0,[],ans,now)

    h,m = ans[0] / 60 , ans[0] % 60


    return str(h) + ":" + str(m)

def dfs(strs,level,tmp,ans,time):

    if level == len(strs):
        hours = tmp[0] * 10 + tmp[1]
        mins = tmp[2] * 10 + tmp[3]
        if hours > 23 or mins > 59:
            return

        curTime = hours * 60 + mins

        diffCur = diffTime(time, curTime)
        diffBest = diffTime(time, ans[0])

        if diffCur < diffBest:
            ans[0] = curTime

        return

    for i in range(0,len(strs)):
        if len(set(tmp + [strs[i]])) > 3:
            continue
        tmp.append(strs[i])
        dfs(strs,level+1,tmp,ans,time)
        tmp.pop()

def diffTime(t1,t2):
    if t1 == t2:
        return float('inf')
    return ((t2 - t1) + 24 * 60) % (24 * 60)


print nextClosestTime("19:34")
print nextClosestTime("23:59")
