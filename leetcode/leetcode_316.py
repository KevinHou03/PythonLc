class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []  # 栈，用于存放结果字符
        in_stack = set()  # 记录栈中是否已有某字符，防止重复加入

        for i, char in enumerate(s):
            # 如果当前字符已经在栈中，直接跳过
            if char in in_stack:
                continue

            # 如果栈顶字符比当前字符大，并且栈顶字符在后续还能出现，则弹出栈顶字符
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)  # 从集合中移除弹出的字符

            # 将当前字符加入栈并记录
            stack.append(char)
            in_stack.add(char)

        # 栈中的字符按顺序拼接成结果
        return ''.join(stack)

