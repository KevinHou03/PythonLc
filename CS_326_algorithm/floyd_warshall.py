# The orginal version:
"""
FloydWarshall(w,n):
    for i = 1 to n do:
        for j = 1 to n do:
            D_0 [i, j] = w[i, j]
            pred[i, j ] = nil;

    for k = 1 to n do:
        for i = 1 to n do:
            for j = 1 to n d；
            if d_k-1 [i, k] + d_k-1 [k, j] < d_k [i, j]:
                d_k[i, j] = d_k-1 [i, k] + d_k-1 [k, j]
                pred[i, j ] = k
            else:
                d_k[i,j] = d_k-1 [i, j]
    return d_n[1..n, 1..n]
"""

'''
(a) It is O(n^3) because it looks like it creates a iterated new n x n matrix 
everytime for each k, so the space would be n x (n x n) = n^3

To fix this, we can use the same D rather than a new one during each iteration,
which means we can modify and update D in place. Also, we can modify pred by using
the same approach of updating in place rather than resetting it in each iteration. 
The pred[i][j] should only be updated when a shorter path through an intermediate 
node k is found. 

(b)
for i = 1 to n do:
    for j = 1 to n do:
        D[i, j] = w[i, j]  # w[i, j]
        if i = j:
            pred[i][j] = inf
        elif w[i,j] < inf:
            pred[i][j] = i
        else:
            pred[i, j] = nil
for k = 1 to n do: # use the same D
    for i = 1 to n do:
        for j = 1 to n do:
            if D[i, k] + D[k, j] < D[i, j]:
                D[i, j] = D[i, k] + D[k, j]
                pred[i, j] = pred[k, j] update ONLY when a shorter path is found 
'''