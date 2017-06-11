# -*- coding: utf-8 -*-
import random
print "hello,test!"
#random 方法生成0-1之间的浮点数
print random.random()
#uniform(1,10) 指定范围内的随机浮点数
random.uniform(1,10);
#randint(1,10)指定范围内的随机整数
random.randint(1,10)
li=["苹果","柚子","香蕉"]
li[random.randint(1,2)]
num = 20
i=0

while i<3:
     b =  input("请输入数字：")
     if b == num:
         print "恭喜，猜中了！"
         break;
     elif b>num:
         print "数字太大！"
     else:
         print "数字或太小！"
     i=i+1
else:
     print "3次机会已用尽！"


for i in range(3):
     b =  input("请输入数字：")
     if b == num:
         print "恭喜，猜中了！"
         break;
     elif b>num:
         print "数字太大！"
     else:
         print "数字或太小！"
if i==2:
   print "3次机会已用尽！"



