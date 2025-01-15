def getRow(row_index):
    res = [1]
    for i in range(row_index): #一行一行create直到你要的那一行
        temp = [0] * (len(res) + 1)
        for j in range(len(res)):
            temp[j] += res[j]
            temp[j + 1] += res[j]
        res = temp
        print(res)

    return res

print(getRow(1))

