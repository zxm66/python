#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
import sys 
import pymysql
reload(sys)
sys.setdefaultencoding('utf-8')
 
if __name__ == "__main__":
    conn = pymysql.connect(host='127.0.0.1', user = "root", passwd="root", db="smp_produce", port=3306, charset="utf8")
    cur = conn.cursor()
    sql = "insert into tb_user(userName) value(%s)"
    person = [['小金1993-06-05'], ['小明 1993-04-03']]

    for i in range(len(person)):
        param = tuple(person[i])
        count = cur.execute(sql, param)
        if count > 0:
            print("添加数据成功！\n")
    conn.commit()

    cur.execute("select * from tb_user")
    users = cur.fetchall();

    for i in range(len(users)):
        print(users[i]);
    pass
    cur.close()
    conn.close()
    print("数据库断开连接！");

