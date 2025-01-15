def is_empty(Li):
    return len(Li) == 0


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __len__(self):
        return len(self.stack)


def brace_match(s):
    match_dict = {')': '(', ']': '[', '}': '{'}
    stack_ins = Stack()
    for ch in s:
        if ch in '([{':
            stack_ins.push(ch)
        elif ch in ')]}':
            if is_empty(stack_ins):
                return False
            elif stack_ins.get_top() == match_dict[ch]:
                stack_ins.pop()
            else:
                return False
    return is_empty(stack_ins)


test1 = '{(){}[[[]]]}'

print(brace_match(test1))
