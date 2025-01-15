def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    # 实际上是每一行前后补0
    res = [[1]]
    for i in range(1,numRows):
        temp = [0] + res[-1] + [0] #这里是创造一个new array 没有改变res里面的东西 记住这种方法
        new_row = []
        for j in range(len(res[-1]) + 1):
             new_row.append(temp[j] + temp[j + 1])
        res.append(new_row)
    return res



