def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """

    for i in range(len(gas)):
        cur_gas = 0
        new_gas = gas[i:] + gas[:i]
        new_cost = cost[i:] + cost[:i]
        for j in range(len(gas)):
            cur_gas = cur_gas + new_gas[j]
            if cur_gas < new_cost[j]:
                break
            cur_gas = cur_gas - new_cost[j]

            if j == len(gas) - 1:
                return i
    return -1

# this works, but too slow

def complete(gas, cost):
    total_gas = total_cost = 0
    cur_gas = 0
    idx = 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        cur_gas += gas[i] - cost[i]

        if cur_gas < 0:
            idx = i + 1
            cur_gas = 0

    if total_gas < total_cost:
        return -1

    return idx



gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas, cost))