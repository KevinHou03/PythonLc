def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """

    def backtrack(count,cur_pos,path):
        if count == 4:
            if cur_pos == len(s):
                res.append(".".join(path))
            return

        for i in range(1, 4):
            if cur_pos + i > len(s):
                break

            part = s[cur_pos:cur_pos + i]
            if (part[0] == "0" and len(part) > 1) or int(part) > 255:
                continue

            backtrack(count + 1, cur_pos + i, path + [part])

    res = []
    backtrack(0,0,[])
    return res

s1 = "25525511135"
print(restoreIpAddresses(s1))


