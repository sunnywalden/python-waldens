#!/usr/bin/python
#-*- coding:utf8 -*-

a=1
while a <= 10:
    if a != 7:
        print(a)
    a += 1

result = 0
for i in range(1,100):
    result += i
print(result)

for i in range(1,100):
    if i % 2 == 0:
    	print(i)
 
for i in range(1,100):
    if i % 2 != 0:
    	print(i)

mt = 0
for i in range(1,100):
    if i % 2 == 0:
    	mt += i
    else:
    	mt -= i
print(mt)

ac = 'sunnywalden'
pw = 'walden0517'
n = 1

while True:
	account = raw_input('Your Username:')
	passwd = raw_input('Your password')

	if account == ac and passwd == pw:
		print('Congratulations! Welcome back!')
		break
	else:
		if n == 3:
			print('You have run out of try chance')
			break
		else:
			n += 1
			print('Wrong username or password!')
			
