#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pymongo

# 获取连接mongo对象
client = pymongo.MongoClient('hadoop04',port=27017)

# 获取数据库（没有则创建）
db = client.pymongo

# 获取集合（没有则创建，类似于mysql的表）
collection = db.qa


# 插入数据
# collection.insert({'username':'aaa'})

# collection.insert_many([
#     {'username':'aaa','age':18},
#     {'username':'bbb','age':20},
# ])


# 查找数据
# cursor = collection.find()
# for x in cursor:
#     print(x)

# res = collection.find_one({'age':18})
# print(res)


# 更新数据
# collection.update_one({'username':'aaa'},{'$set':{'age':19}})
# collection.update_many({'username':'aaa'},{'$set':{'username':'bbb'}})


# 删除数据
# collection.delete_one({'username':'bbb'})
# collection.delete_many({'username':'bbb'})