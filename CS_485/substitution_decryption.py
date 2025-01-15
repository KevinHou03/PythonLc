# decryption, with the help of the frequency we are indeed able to get a few letters correctly, like "e" and "z" but not
#perfectly, we still need some other analysis to get everything right.
def trans(s):
    s = s.lower()
    dict1 = {"q": "a", "f": "n", "r": "d", "l": "s", "o": "i", "z": "t", "i": "h", "t": "e", "b": "x", "v": "w",
             "u": "g", "s": "l", "w": "b", "g": "o", "y": "f", "k": "r", "e": "c", "a": "k", "m": "z", "x": "u",
             "n": "y", "h": "p", "d": "m", "c": "v", " ": " ", "W": "B"}

    result = []
    for i in range(0, len(s)):
        if s[i] in dict1.keys():
            result.append(dict1[s[i]])

    return "".join(result)


print(trans(
    "Wsgeaeiqof ol q rtetfzkqsomtr qfr rolzkowxztr rouozqs strutk zteifgsgun ziqz tfqwstl ltexkt, zkqflhqktfz, "
    "qfr zqdhtk ktlolzqfz ktegkr atthofu gy zkqflqezogfl qekgll q ftzvgka gy egdhxztkl Oz ltkctl ql zit xfrtksnofu "
    "zteifgsgun ygk cqkogxl eknhzgexkktfeotl vozi Wozegof wtofu zit yoklz qfr dglz vtss- afgvf qhhsoeqzogf Igvtctk, "
    "zit hgztfzoqs qhhsoeqzogfl gy wsgeaeiqof tbztfr yqk wtngfr eknhzgexkktfeotl odhqezofu cqkogxl ofrxlzkotl"))


# answer:blockchain is a decentralized and distributed digital ledger
# technology that enables secure transparent and tamper resistant record
# keeping of transactions across a network of computers it serves as the
# underlying technology for various cryptocurrencies with bitcoin being the
# first and most well known application however the potential applications of
# blockchain extend far beyond cryptocurrencies impacting various industries
