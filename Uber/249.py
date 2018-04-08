
def groupStrings(strs):

    hm = {}
    for s in strs:

        offset = ord(s[0]) - ord('a')
        key = ""
        for c in s:
            diff = ord(c) - offset
            if diff < ord('a'):
                diff += 26
            key += str(unichr(diff))

        if key in hm:
            hm[key].append(s)
        else:
            hm[key] = [s]

    return hm.values()




print groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
