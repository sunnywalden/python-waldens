#!/usr/bin/python
# -*- coding:utf-8 -*-
from walden.db.dbcon import *
from walden.db.logindb import *


def set_login_status(id, istrue):
    userid = id

    sql = "UPDATE login_status SET is_login='%d' WHERE user_id='%d'" % (istrue, userid)
    conn(sql)

def login_init(id):
    userid = id
    set_login_status(userid, False)


def user_login(acc, pas):
    account = acc
    passwd = pas

    # SQL 查询语句
    sql = "SELECT user_id \
           FROM users \
           WHERE account = '%s' AND passwd = '%s'" % \
          (account, passwd)

    res = conn(sql)
    if res:
        set_login_status(res, True)
        return True
    else:
        return False

