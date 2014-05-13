'''
Created on May 9, 2014

@author: veb
'''
'''
problem 1.2
'''
import random, StringIO, time, binascii
def initial_data():
    
    
    ceiling = 10 ** 7
    i = 1
    s = list()
    se = set()
    f = open('phone.txt', 'w')
    f1 = open('phone_uniq.txt', 'w')
    buf = StringIO.StringIO() 
    num = 1
    while i <= ceiling:
        x = random.randint(1, ceiling)
        s.append(str(x) + '\n')
        se.add(str(x) + '\n')
#        if i % 10 ** (num - 1) == 0:
#    #        print len(s) 
#            buf.writelines(s)
#            f.write(buf.getvalue())
#            f.flush()
#            buf.close()
#            buf = StringIO.StringIO() 
#            s = list()
    #        print len(s) 
    #        time.sleep(1)
        i += 1
    f.writelines(s)
    f.flush()
    f.close()
    f1.writelines(se)
    f1.flush()
    f1.close()
    

# print type( 122121212134124545454545454546464646464612389012830182038102830128046123123123123+1)
def vector_sort():
    '''
    10,000,000 scale.
    '''
    out = open('ps.txt', 'w')
#    time.sleep(100)
    vector_space = [0] * 1024
    tail_index = -1 
    with open('phone.txt', 'r') as fp :
        for line in fp :
            num = int(line.strip())
            if num % 8 > 0:
                index = num / 8
                offset =  2 ** (8-num % 8)
#                print bin(offset)
            else:
                index = (num-1)  / 8
                offset = 0b00000001
            current_tail = len(vector_space) - 1
            if current_tail < index :
                vector_space.extend([0] * (index - current_tail + 1024))
            src = vector_space[index]
            dest = src | offset
            vector_space[index] = dest 
            tail_index = tail_index if tail_index >= index else index
    if len(vector_space) > tail_index:
        vector_space = vector_space [:tail_index + 1]
    index = 0
    mo = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001 ]
    buf = StringIO.StringIO()
    for e in vector_space:
        count = 1 
        for x in mo :
            if e & x > 0:
                buf.write(str(index * 8 + count) + '\n')
            count += 1
        index += 1
                
    out.write(buf.getvalue())
    out.flush()
    out.close()
begin = time.time()
#s = [1,2,3]
#print s[2:2]
initial_data()
vector_sort()
print time.time() - begin , 's'
# print 0b00000001, 0b11111111
    
