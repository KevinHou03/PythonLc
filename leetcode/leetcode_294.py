def canWin(currentState):
    """
    :type currentState: str
    :rtype: bool
    """
    memo = {} #记录当前状态下 我 能不能赢
    def backtrack(cur_state):
        if "++" not in "".join(cur_state):
            print("sjd")
            return False
        if cur_state in memo:
            return memo[cur_state]
        for i in range(0, len(currentState) - 1):
            if cur_state[i] == '+' and cur_state[i + 1] == '+':
                new_state = cur_state[:i] + "--" + cur_state[i + 2:]

                if not backtrack(new_state):#backtrack(new_state)代表是对手先手了，因为之前我已经flip完了，所以backtrack(new_state)返回false才代表对手输，我赢
                    memo[cur_state] = True
                    return True
        # exhaust所有可能性了，依旧没有return true，那这个情况下我只能输
        # 如果所有行动后，对手都能赢 => 我必输。
        memo[cur_state] = False
        return False

    return backtrack(currentState)

'''
能找到一次行动，使对手处于必输态 => 我能赢；
如果所有行动后，对手都能赢 => 我必输。
'''

s = "++++"
canWin(s)