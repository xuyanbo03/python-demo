#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(
    host='hadoop01',
    user='root',
    password='root',
    database='pymysql',
    port=3306
)
cursor = conn.cursor()

# 测试数据库
# cursor.execute("select 1")
# res = cursor.fetchone()
# print(res)


# 插入数据
# sql = """
# insert into user(id,username,age,password) values (2,'bbb',20,'111111')
# """
# cursor.execute(sql)
# conn.commit()

# sql = """
# insert into user(id,username,age,password) values (null,%s,%s,%s)
# """
# username = 'ccc'
# age = 21
# password = '111111'
# cursor.execute(sql,(username,age,password))
# conn.commit()


# 查询数据
# fetchone
# sql = """
# select * from user
# """
# cursor.execute(sql)
# while True:
#     res = cursor.fetchone()
#     if not res:
#         break
#     print(res)

# fetchall
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchall()
# for result in results:
#     print(result)

# fetchmany(size)
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchmany(2)
# for result in results:
#     print(result)


# 删除数据
# sql = """
# delete from user where id = 3
# """
# cursor.execute(sql)
# conn.commit()


# 更新数据
# sql = """
# update user set username='sss' where id=2
# """
# cursor.execute(sql)
# conn.commit()

conn.close()
