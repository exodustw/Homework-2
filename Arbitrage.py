liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

class Pool:
    def __init__(self, nameA, nameB, amountA, amountB):
        self.nameA = nameA
        self.nameB = nameB
        self.amountA = amountA
        self.amountB = amountB
        self.swapFee = 0.003

    def swap(self, swapA, swapB):
        assert(swapA >= 0 and swapB >= 0)
        alpha = 1 - self.swapFee

        if(swapA > 0 and swapB == 0):
            get = (swapA*alpha)/(swapA*alpha+self.amountA)*self.amountB
            self.amountA += swapA
            self.amountB -= get
            return (0, get)
        elif(swapA == 0 and swapB > 0):
            get = (swapB*alpha)/(swapB*alpha+self.amountB)*self.amountA
            self.amountB += swapB
            self.amountA -= get
            return (get, 0)
        else:
            assert(0)



# money = 5
# money, _ = pools[0].swap(0,money)
# print(money)
# _, money = pools[2].swap(money,0)
# print(money)
# money, _ = pools[5].swap(0,money)
# print(money)

# print(pools)

def calculate(path, money):
    pools = {}
    for name, value in liquidity.items():
        # print(name, value)
        pools[name]=Pool(name[0], name[1], value[0], value[1])

    for i in range(len(path)-1):
        if(path[i] == path[i+1]):
            continue
        # print(path[i], path[i+1])
        if (path[i], path[i+1]) in pools:
            pool = pools[(path[i], path[i+1])]
            _, money = pool.swap(money, 0)
        elif (path[i+1], path[i]) in pools:
            pool = pools[(path[i+1], path[i])]
            money, _ = pool.swap(0, money)
    return money

def summary(path, money):
    print('path: ', end='')
    for i, p in enumerate(path):
       if(i != 0):
           print('->', end='')
       print(p, end='')
    
    print(f', tokenB balance={money}')

tokens = ['tokenA', 'tokenB', 'tokenC', 'tokenD', 'tokenE']
money = 5

from itertools import permutations

for x in range(1, 10):
    for p in permutations(tokens, x):
        path = ('tokenB',)+p+('tokenB',)
        # print(f"{path = }")
        
        m = calculate(path, 5)
            
        if m > 20:
            summary(path, m)
            exit(0)

# path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077447

# print(calculate(('tokenB', 'tokenA', 'tokenD', 'tokenB'), 5))