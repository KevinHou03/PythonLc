def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                dp[i] = dp[i + len(word)]
                # dp[i] = True ; 依赖后续状态：此方法的逻辑是：即使 s[i : i + len(word)] 是 wordDict 中的一个单词，但如果从 i + len(word) 到结尾不能被组合成 wordDict 中的单词组合，那么 dp[i] 也不能设置为 True。
                # 这种方法更加严格，因为它确保了从位置 i + len(word) 开始的子串可以通过 wordDict 中的单词组合而成，才会将 dp[i] 设置为 True。因此，它可以更准确地表示是否可以从 i 开始分割字符串 s
            if dp[i]:
                break
    return dp[0]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s,wordDict))

def wordBreak2(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if dp[j] and (s[j:i] in wordDict):
                dp[i] = True
    return dp[len(s)]

print(wordBreak2(s,wordDict))
