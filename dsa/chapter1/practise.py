'''
Created on May 8, 2014

@author: veb
'''
'''
yin shi fen jie
'''
def _ysfj_1(m):
    pass
def ysfj(m):
    return _ysfj_1(m)
'''
yin shi fen jie----
'''

'''
o ji li de
'''
def _ojld_1(m  , n):
    m , n = (m , n) if m >= n   else (n , m)
    i = n 
    loop = 0
    try:
        while i > 0:
            loop += 1
            if m % i == 0 and n % i == 0 :
                return i 
            i -= 1
        return 1
    finally:
        print 'loop=%s' % loop
def _ojld_2(m , n):
    m , n = (m , n) if m >= n   else (n , m)
    loop = 1
    try:
        mod = m % n
        while mod != 0:
            m , n = n , mod
            mod = m % n
            loop += 1
        return n
    finally:
        print 'loop=%s' % loop
        
def ojld(m , n):
    '''
    find the zui da gong yue shu
    '''
    # version 1
#    return _ojld_1(m , n)
    # version 1
    return _ojld_2(m , n)
'''
o ji li de ----
'''
'''
jie cheng
'''
def _jiecheng_1(n):
    i = 1
    res = 1
    while i <= n :
        res *= i
        i+=1
    return res
    
def jiecheng(n):
    return _jiecheng_1(n)
if __name__ == '__main__':
    print jiecheng(1000)
#    print ojld(5675 , 654)
