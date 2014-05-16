'''
Created on May 16, 2014

@author: jacky
'''
'''
2.1 A : mao pao ...
'''


'''
2.1 B
'''
import string
def initial_data(n=52 ):
    return string.letters

def duplication_left(src , offset ):
    dest = ''
    length =  len(src)
    i = length 
    while i > 0:
        dest+=src[offset]
        i-=1
        
print len(initial_data())
