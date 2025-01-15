class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.word_dict = {}
        for i, word in enumerate(wordsDict):
            if word not in self.word_dict:
                self.word_dict[word] = []
            self.word_dict[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = self.word_dict[word1]
        index2 = self.word_dict[word2]

        i, j = 0, 0
        shortest = float('inf')

        while i < len(index1) and j < len(index2):
            shortest = min(shortest, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1

        return shortest


