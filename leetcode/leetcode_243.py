def shortestDistance(wordsDict, word1, word2):
    """
    :type wordsDict: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    # min_val = float("inf")
    # A = float("-inf")
    # B = float("inf")
    # for i in range(len(wordsDict)):
    #     if wordsDict[i] == word1:
    #         A = i
    #     min_val = min(min_val, abs(A - B))
    #     if wordsDict[i] == word2:
    #         B = i
    #     print(A,B,min_val)
    #     min_val = min(min_val, abs(A - B))
    # return min_val

    A = wordsDict.index(word1)
    B = wordsDict.index(word2)
    print(A,B)

wordsDict = ["a", "a", "a", "b", "b"]
word1 = "a"
word2 = "b"




print(shortestDistance(wordsDict, word1, word2))