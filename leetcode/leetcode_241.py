def diffWaysToCompute(expression):
    """
    :type expression: str
    :rtype: List[int]
    """

    calculations = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
    }
    def backtrack(left, right):
        res = []
        for i in range(left, right + 1):
            stuff = expression[i]
            if stuff in calculations:
                num_left = backtrack(left, i - 1)
                num_right = backtrack(i + 1, right)
                for num1 in num_left:
                    for num2 in num_right:
                        res.append(calculations[stuff](num1, num2))

        if res == []:
            res.append(int(expression[left:right + 1]))

        return res

    return backtrack(0, len(expression) - 1)



expression = "2-1-1"
print(diffWaysToCompute(expression))