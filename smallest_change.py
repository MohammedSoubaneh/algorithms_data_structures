""""
Canadian coin system
1, 5, 10, 25, 50

Given an input amount of change x, write a function to determine 
the minimum number of coins required to make that amount of change.

"""

def change(x: int, coins: list, changeList: list) ->int:
    
    
    if x == 0:
        return 0
    if x < 0:
        return False
    else:
        if coins[-1] > x:
            coins.pop()
            return change(x, coins, changeList)
        elif coins[-1] == x:
            changeList.append(coins[-1])
            return len(changeList)
        elif coins[-1] < x:
            changeList.append(coins[-1])
            return change(x - coins[-1], coins, changeList)



assert change(0, [1, 5, 10, 25, 50], []) == 0
assert change(-1, [1, 5, 10, 25, 50], []) == False
assert change(5, [1, 5, 10, 25, 50], []) == 2
assert change(13, [1, 5, 10, 25, 50], []) == 4