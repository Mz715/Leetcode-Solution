'''
@Author: your name
@Date: 2020-06-19 11:14:42
@LastEditTime: 2020-06-19 11:35:24
@LastEditors: Please set LastEditors
@Description: 硬币找零问题的递归优化解法
@FilePath: \python_code\leetcode\recDC.py
'''

def recDC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knowResults)
            print(i,numCoins)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins

print(recDC([1,5,10,25], 63, [0]*64)) 
