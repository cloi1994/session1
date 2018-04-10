def reverseWords(s):

    s = list(s)
    i = 0
    j = len(s) - 1

    s = s[::-1]

    start = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reverse(s,start,i-1)
            start = i+1
    reverse(s,start,len(s)-1)

    return ''.join(s)
def reverse(s,start,end):

    while start <= end:
        s[start] , s[end] = s[end] , s[start]
        start += 1
        end -= 1
