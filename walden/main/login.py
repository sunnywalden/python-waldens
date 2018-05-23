#!/usr/bin/python
#-*- coding:utf-8 -*-

from walden.db.logindb import *
from walden.db.userdb import *

def login(acc, pas):
    account = acc
    passwd = pas
    n = 1

    while n < 4:
        res = user_login(account, passwd)
        if res:
            print('Congratulations.Login Succedss!')
            #set_login_status(id, True)
        else:
            print('Wrong username or password!')
            if n == 3:
                print('Out of three tries,exitting now!')
                break
            else:
                n += 1

def is_login(id):
    userid = id

    sql = "SELECT is_login FROM login_status WHERE user_id='%s'" %  userid
    if conn(sql):
        return True
    else:
        return False

def lgout(id):
    userid = id
    sql = "UPDATE login_status SET is_login=False WHERE user_id='%s'" % userid
    conn(sql)
    print('Logging out!')
