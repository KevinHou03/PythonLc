# insertion: inversion detection

def inversion(li):
    result = 0
    for i in range(len(li)):
        value = li[i]
        sub_li = sorted(li[i + 1:])
        for j in range(len(sub_li)):
            if sub_li[j] > value:
                result += len(sub_li[0:j])
                break
            if sub_li[-1] < li[i]:
                result += 1
    return result

li1 = [3,4,5,6,1,2,0]
print(inversion(li1))

'''
3 -> 1456 -> 1
4 -> 156 -> 1
5 -> 16 -> 1
6 -> 1
'''

print(li1[0:0])

'''
Merge(A,p,q,r):
n_l = q - p + 1
n_r = r - q
let L[0:n_l - 1] and R[0:n_r - 1]be new arrays
for i = 0 to n_l - 1:// copy A[p:q]into L[0 :n_l -1]
    L[i] = A[p + 1]
for j = 0 to n_r - 1: copy A[q+1:r]into L[0 :n_r -1]
    R[j] = A[q + j + 1]

i = 0 // i indexes the smallest remaining element in L
j = 0 // j indexes the smallest remaining element in R
k = p // k indexes the location in A to fill

//As long as each of the arrays L and R contains an unmerged element , copy the smallest unmerged element back in to A[p:r]

while i < n_l and j < n_r:
    if L[i] <= R[j]
        A[k] = L[i]
        i + i + 1
    else A[k] = R[j]
        j = j + 1
    k = k + 1
//having gone through one of L and R entirely, copy the remainder of the otehr to the end of A[p:r]
while i < n_l:
    A[k] = L[i]
    i = i + 1
    k = k + 1
while j < n_r:
    A[k] = R[j]
    j = j + 1
    k = k + 1
        
'''



