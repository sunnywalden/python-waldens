#!/usr/bin/python
#-*- coding:utf-8 -*-

a = '123'
b = int(a)
c = -321
d = 'SunnyWalden'

#int functions
print(type(int(a)))

print(b.bit_length())


print(b.conjugate())


print(b.to_bytes(2,'big'))


# string funcitons
#
#str
st1 = 'Welcome to {site}'

username = 'sunnywalden'
passwd = 'sunny0902'

print(d.capitalize(), d.casefold(), d.lower(), d.center(25,'#'), d.find('n',0,4))


print(st1.format(site=d), st1.format_map({'site':d}), d.count('sunny'), d.find('nn'), d.endswith('lden'), d.index('alden'))

print(passwd.isalnum(), username.isalpha())


print(username.islower(), d.upper().isupper(), a.isdigit(), a.isnumeric())


s = 'username\tsex\temail\tphone number\nsunnywalden\tM\tsunnywalden@gmail.com\t18792648142\nsunnywalden\tM\tsunnywalden@gmail.com\t18792648142\nsunnywalden\tM\tsunnywalden@gmail.com\t18792648142'

print(s.expandtabs(25))



print(' '.join(username))