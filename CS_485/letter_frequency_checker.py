
# compute the relative frequency
def check(s):
    letter_dict = {}
    s = "".join(s.split())
    s = s.lower()
    str_len = len(s)
    for index, letter in enumerate(s):
        if letter not in letter_dict.keys():
            letter_dict[letter] = 0
        else:
            letter_dict[letter] += 1
    print("the occurence of each word:", letter_dict)
    for key, value in letter_dict.items():
        letter_dict[key] = value / str_len

    return sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)



s1 = "Wsgeaeiqof ol q rtetfzkqsomtr qfr rolzkowxztr rouozqs strutkzteifgsgun ziqz tfqwstl ltexkt, zkqflhqktfz, " \
    "qfr zqdhtkktlolzqfz ktegkr atthofu gy zkqflqezogfl qekgll q ftzvgka gyegdhxztkl Oz ltkctl ql zit xfrtksnofu " \
    "zteifgsgun ygk cqkogxleknhzgexkktfeotl vozi Wozegof wtofu zit yoklz qfr dglz vtss-afgvf qhhsoeqzogf Igvtctk, " \
    "zit hgztfzoqs qhhsoeqzogfl gywsgeaeiqof tbztfr yqk wtngfr eknhzgexkktfeotl odhqezofucqkogxl ofrxlzkotl"

print(check(s1))