#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    table = [float('inf')] * (total + 1)
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        min_coins = float('inf')
        for j in range(m):
            if coins[j] > i:
                break
            subres = table[i - coins[j]]
            if subres + 1 < min_coins:
                min_coins = subres + 1
        table[i] = min_coins

    if table[total] == float('inf'):
        return -1
    return table[total]
