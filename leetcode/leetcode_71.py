def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    path = path[:-1]
    delete = []
    result = []
    for i in range(2, len(path)):
        if (path[i] == "." and path[i - 1] == ".") or path[i] == ".":
            delete.append(i)
            delete.append(i - 1)
        if path[i] == "/" and path[i - 1] == "/":
            delete.append(i)
    for i in range(len(path)):
        if i in delete:
            continue
        else:
            result.append(path[i])
    if path[-1] == ".":
        return "".join(result[:-1])
    return "".join(result)


print(simplifyPath("/a/./b/../../c/"))
s = "/a/./b/../../c/"
print(s.split("/"))
