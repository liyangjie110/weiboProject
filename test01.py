# -*- coding: utf-8 -*-
print "hello,test!"
str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910222"
for i in range(len(str)/5+1):
    print(str[i*5:5*(i+1)]+'\n')


str = "中国看到框架上搭建随大流就胜利大街中国"
new_str = unicode(str,'utf-8')
li = list(new_str)
for i in range(len(li)/5+1):
    t = li[i*5:5*(i+1)]
    print("".join(t))
{}
nums =[10,9,8,7,6,5]
nums[0] =nums[1]-5
if 4 in nums:
    print nums[3]
else:
    print nums[4]
