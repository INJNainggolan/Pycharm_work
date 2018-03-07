'''
plaincode = input("请输入明文：")
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):
        print(chr(ord("a") + (ord(p) - ord("a") +3)%26), end = '')
    else:
        print(p, end = '')
'''

#print("{:<15s}:{:>8.2f}".format("Length",23.87501))

'''
import time
scale = 10
print("-----执行开始-----")
for i in range(scale + 1):
    a, b = '**' * i,'..' * (scale - i)
    c = (i / scale) * 100
    print("%{:^3.0f}[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("-----执行结束-----")
'''
'''
import time
for i in range(101):
    print("\r{:2}%".format(i), end = "")
    time.sleep(0.5)
'''

import time
scale = 50
print("执行开始".center(scale//2,'-'))
t = time.clock()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b,-t),end = '')
    time.sleep(0.5)
print("\n" + "执行结束".center(scale//2,'-'))