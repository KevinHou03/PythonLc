def cross(li):
    pos, neg, result = [], [], []
    for i in range(len(li)):
        neg.append(li[i]) if li[i] < 0 else pos.append(li[i])

    for j in range(len(li)):
        if len(pos) == 0:
            result.extend(neg)
            return result
        if len(neg) == 0:
            result.extend(pos)
            return result
        if j % 2 == 0:
            result.append(pos[-1])
            pos.pop()
        else:
            result.append(neg[-1])
            neg.pop()
    return result


print(cross( [9, -3, 5, -2, -8, -6, 1, 3, -1, -3, -9]))

def cross2(li):
    pos = 0
    neg = 1

    while True:
        while pos < len(li) and li[pos] >= 0 :
            pos += 2
        while neg < len(li) and li[neg] < 0  :
            neg += 2

        if pos < len(li) and neg < len(li):
            li[pos], li[neg] = li[neg], li[pos]

        else:
            break
    return li

print(cross2( [9, -3, 5, -2, -8, -6, 1, 3, -1, -3, -9]))
