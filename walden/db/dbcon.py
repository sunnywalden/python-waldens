#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
import hashlib

def conn(sql):
    # 打开数据库连接
    db_host = "18.217.27.29"
    db_user = "walden"
    db_pass = "walden0209"
    db_name = "sunnywalden"

    sqls = sql

    db = pymysql.connect(db_host, db_user, db_pass, db_name)

    cursor = db.cursor()
    # noinspection PyBroadException
    try:
        cursor.execute(sqls)
        result = cursor.fetchone()
        #print("result %s:" % result)
        db.commit()
        if result:
            return result
        # 提交到数据库执行
        else:
            return True
    except:
        # 如果发生错误则回滚
        print('exception occurred')
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

