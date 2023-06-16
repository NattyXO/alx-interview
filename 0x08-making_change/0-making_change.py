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
    if total <= 0:
        return 0

    coins_set = set(coins)
    table = [float('inf')] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins_set:
            if coin <= i:
                subres = table[i - coin]
                if subres != float('inf') and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == float('inf'):
        return -1
    return table[total]
