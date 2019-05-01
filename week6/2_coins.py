def greedy_coins(amt, denoms):
    # denoms is sorted in ascending order
    # so loop denoms backwards
    res = [0]*len(denoms)
    have = amt
    for idx, i in enumerate(denoms[::-1]):
        while have - i >= 0:
            have -= i
            res[len(denoms)-1 - idx] += 1
    return res

res = greedy_coins(5, [1, 2, 3])
print(res)
