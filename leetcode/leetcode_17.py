import itertools


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    Map = {"2": ['a', 'b', 'c'],
           "3": ['d', 'e', 'f'],
           "4": ['g', 'h', 'i'],
           "5": ['j', 'k', 'l'],
           "6": ['m', 'n', '0'],
           "7": ['p', 'q', 'r', 's'],
           "8": ['t', 'u', 'v'],
           "9": ['w','x','y','z']

           }
    total = []
    for elements in digits:
        total.append(Map[elements])
    chars = [Map[digit] for digit in digits]
    combinations = itertools.product(*chars)

    return [''.join(combination) for combination in combinations]


# combinations = [str(x) + str(y) for x in list1 for y in list2]
print(letterCombinations("23"))
strr = '23'
for element in strr:
    print(element)

Map = {"2": ['a', 'b', 'c'],
       "3": ['d', 'e', 'f'],
       "4": ['g', 'h', 'i'],
       "5": ['j', 'k', 'l'],
       "6": ['m', 'n', '0'],
       }
print(Map["2"])
