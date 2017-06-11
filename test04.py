# -*- coding: utf-8 -*-
import random

#random 方法生成0-1之间的浮点数
print random.random()
#uniform(1,10) 指定范围内的随机浮点数
random.uniform(1,10);
#randint(1,10)指定范围内的随机整数
random.randint(1,10)
li=["苹果","柚子","香蕉","葡萄"]
print(li[random.randint(0,3)])

print(range(10))
li=list(xrange(10))
print(li)