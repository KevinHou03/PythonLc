def isValidSerialization(preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    pos_avail = 1
    preorder = preorder.split(',')
    for i in range(len(preorder)):
        pos_avail -= 1
        if preorder[i] < 0:
            return False
        if preorder[i] != '#':
            pos_avail += 2
    return pos_avail == 0



