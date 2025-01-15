def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    y = str(x)
    for i in range(0, len(str(y)) // 2):  # i = 012 -(i+1) = -1-2-3
        print('y[i]', y[i])
        print('y[-1+1', y[-(i + 1)])
        if y[i] != y[-(i + 1)]:
            return False
    return True


print(isPalindrome(8))

a = '123'
b = 123
print(len(a))
print(a[0])
print(a[1])
print(a[2])

print(a[-1])
print(a[-2])

print(a[-1::-1])

s = "Wsgeaeiqofolqrtetfzkqsomtrqfrrolzkowxztrrouozqsstrutkzteifgsgunziqztfqwstlltexkt,zkqflhqktfz,qfrzqdhtkktlolzqfzktegkratthofugyzkqflqezogflqekgllqftzvgkagyegdhxztklOzltkctlqlzitxfrtksnofuzteifgsgunygkcqkogxleknhzgexkktfeotlvoziWozegofwtofuzityoklzqfrdglzvtss-afgvfqhhsoeqzogfIgvtctk,zithgztfzoqsqhhsoeqzogflgywsgeaeiqoftbztfryqkwtngfreknhzgexkktfeotlodhqezofucqkogxlofrxlzkotl"

print(len(s))


# blockchain is
# a decentralized and
# distributed digital
# ledger technology that
# enables secure, transparent
# , and tamper resistant record keeping
# of transactions across a network of computers
# it serves as the underlying

def trans(s):
    dict1 = {"q": "a", "f": "n", "r": "d", "l": "s", "o": "i", "z": "t", "i": "h", "t": "e", "b": "x", "v": "w",
            "u": "g", "s": "l", "w": "b", "g": "o", "y": "f", "k": "r", "e": "c", "a": "k", "m": "z", "x": "u",
            "n": "y", "h": "p", "d": "m", "c": "v"," ":" "}
    result = []
    for i in range(0, len(s)):
        if s[i] in dict1.keys():
            result.append(dict1[s[i]])

    return "".join(result)

print(trans("Wsgeaeiqof ol q rtetfzkqsomtr qfr rolzkowxztr rouozqs strutk zteifgsgun ziqz tfqwstl ltexkt, zkqflhqktfz, qfr zqdhtk ktlolzqfz ktegkr atthofu gy zkqflqezogfl qekgll q ftzvgka gy egdhxztkl Oz ltkctl ql zit xfrtksnofu zteifgsgun ygk cqkogxl eknhzgexkktfeotl vozi Wozegof wtofu zit yoklz qfr dglz vtss- afgvf qhhsoeqzogf Igvtctk, zit hgztfzoqs qhhsoeqzogfl gy ws eaeiqof tbztfr yqk wtngfr eknhzgexkktfeotl odhqezofu cqkogxl ofrxlzkotl"))
