#!/usr/bin/python
# -*- coding:utf-8 -*-
from walden.db.dbcon import *
from walden.db.logindb import *

def add_user(name, sex, passwd, birth, account):
    name = name
    sex = sex
    account = account
    birth = birth
    passwd = passwd

    # SQL 新增语句
    sql = "INSERT INTO users(name, sex, passwd, birth, account) \
           VALUES('%s', '%s', '%s', '%s', '%s')" % \
          (name, sex, passwd, birth, account)

    res = conn(sql)
    if res:
        return True
        login_init(user_id)
    else:
        return False


def search_user(acc):
    account = acc

    # SQL 查询语句
    sql = "SELECT user_id \
           FROM users \
           WHERE account = '%s'" % \
          account

    res = conn(sql)
    if res:
        return True
    else:
        return False


def update_user(account, passwd):
    account = account
    passwd = passwd
    hash = hashlib.md5()
    hash.update(passwd.encode("utf-8"))
    m_passwd = hash.hexdigest()

    # SQL 新增语句
    sql = "UPDATE users \
           SET passwd = '%s' WHERE account = '%s'" % \
          (m_passwd, account)

    res = conn(sql)
    if res:
        return True
    else:
        return False


def delete_user(account):
    account = account

    # SQL 新增语句
    sql = "DELETE FROM users \
           WHERE account = '%s' AND user_id=4" % \
          (account)

    res = conn(sql)
    if res:
        return True
    else:
        return False





# us = 'walden'
# ps = 'walden0114'
#
# a = hashlib.md5()
# a.update(b'walden0114')
# psw = a.hexdigest()
#
# search_user(us, psw)
#
# # add_user('sunny', 'F', hashlib.md5(b'sunny0114').hexdigest(), '1992-05-17', 'sunny')
#
# update_user('sunny', 'sunny0209')
#
# delete_user('sunny')

