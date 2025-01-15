def findPlatform(arr, dep, n):
    '''
    Accepts two arrays with arrival and departure time
    and the size of the array
    Returns minimum number of platforms required
    '''

    # plat_needed indicates number of platforms
    # needed at a time
    plat_needed = 1
    result = 1

    # run a nested loop to find overlap
    for i in range(n):
        # minimum platform needed
        plat_needed = 1

        for j in range(n):
            # check for overlap
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1
        print(plat_needed)

        # update result
        result = max(result, plat_needed)

    return result


# Driver code



arr = [200, 210, 300, 320, 350, 500]
dep = [230, 320, 340, 400, 430, 520]

print(findPlatform(arr,dep,6))


# FloydWarshall(w,n):
#     for i = 1 to n do:
#         for j = 1 to n do:
#             D_0 [i, j] = w[i, j]
#             pred[i, j ] = nil;
#
#     for k = 1 to n do:
#         for i = 1 to n do:
#             for j = 1 to n d；
#             if d_k-1 [i, k] + d_k-1 [k, j] < d_k [i, j]:
#                 d_k[i, j] = d_k-1 [i, k] + d_k-1 [k, j]
#                 pred[i, j ] = k
#             else:
#                 d_k[i,j] = d_k-1 [i, j]
#     return d_n[1..n, 1..n]