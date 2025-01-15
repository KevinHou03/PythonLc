def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # answer = []
    # for i in range(len(strs)):
    #     temp_ans = [strs[i]]
    #     for j in range(i + 1, len(strs)):
    #         flag = True
    #         if len(strs[j]) != len(strs[i]):
    #             continue
    #         for item in strs[j]:
    #             if item not in strs[i]:
    #                 flag = False
    #         if flag == True:
    #                 temp_ans.append(strs[j])
    #     answer.append(temp_ans)
    #     answer2 = []
    #     for element in answer:
    #         if len(element) != 1:
    #             answer2.append(element)
    # return answer2
    # 如果说两个words组成的单词是一样的，那么你sort他们之后，他们会是一样的
    dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))  # 把list变成str的方法
        if sorted_word in dict.keys():
            dict[sorted_word].append(word)
        else:
            dict[sorted_word] = []
            dict[sorted_word].append(word)
    return list(dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
