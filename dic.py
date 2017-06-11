# -*- coding: utf-8 -*-
dic01 ={"name":"liyangjie","age":"30","school":"清华"}
print dic01

print len(dic01)
print dic01.get("name")
print dic01.get("school")
new_str = {}
dic01["company"]=  u"京北方"
print dic01.get("company")
dic01.pop("company")
print dic01


#coding=UTF-8
import json
b = {'name': u'王栋轩', 'age':'二十五', 'class': u'小二班'}
print(json.dumps(b, encoding='UTF-8', ensure_ascii=False))