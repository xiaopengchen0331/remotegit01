import re

show_mod="""
SC1:MISC15 >>         LC1 : PING_PASS POSTCODE 0x45 | DM2_UP
SC1:MISC15 >>         332 : Not present
SC1:MISC15 >>         LC3 : Not present
SC1:MISC15 >>         LC4 : Not present
SC1:MISC15 >>         LC5 : Not present
SC1:MISC15 >>         LC6 : Not present
SC1:MISC15 >>         LC7 : Not present
SC1:MISC15 >>         LC8 : Not present
SC1:MISC15 >>         FM1 : Not present
SC1:MISC15 >>         FM2 : Not present
SC1:MISC15 >>         FM3 : Not present
SC1:MISC15 >>         FM4 : Not present
SC1:MISC15 >>         FM5 : Not present
SC1:MISC15 >>         FM6 : Not present
SC1:MISC15 >>        SUP1 : PING_PASS POSTCODE 0x3B | DIAG_UP
SC1:MISC15 >>        SUP2 : PING_PASS POSTCODE 0x3B | DIAG_UP
SC1:MISC15 >>    OTHER_SC : PING_PASS POSTCODE 0x3B | DIAG_UP
SC1:MISC15 >>        FAN1 : is present
SC1:MISC15 >>        FAN2 : is present
SC1:MISC15 >>        FAN3 : Not present
SC1:MISC15 >>        PSU1 : Not present
SC1:MISC15 >>        PSU2 : Not present
SC1:MISC15 >>        PSU3 : is present
SC1:MISC15 >>        PSU4 : Not present
SC1:MISC15 >>        PSU5 : Not present
SC1:MISC15 >>        PSU6 : is present
SC1:MISC15 >>        PSU7 : Not present
SC1:MISC15 >>        PSU8 : is present
SC1:MISC15 >>        PSU9 : Not present
SC1:MISC15 >>       PSU10 : Not present
[UT000000141.605] SC1:MISC15:0 >> ##== EXEC TASK ==## [module-status] It(0) [P.A.S.S]
[UT000000141.608] SC1:MISC15:0 >> ##== DONE ==##
SC1:MISC15 => module-status Passed. ReturnCode:[0x0]
===========================================
===== System Info: LC1 =====
SERIAL_NUMBER   : SAL1817R5W9
PRODUCT_NUMBER  : N9K-X9464PX
HW_REV          : 0.1060
===== System Info: SC1 =====
SERIAL_NUMBER   : SAL1736CB4M
PRODUCT_NUMBER  : N9K-SC-A
HW_REV          : 0.2190
===== System Info: SC2 =====
SERIAL_NUMBER   : SAL1746G7KK
PRODUCT_NUMBER  : N9K-SC-A
HW_REV          : 1.1
===== System Info: SUP1 =====
SERIAL_NUMBER   : SAL1734BXEC
PRODUCT_NUMBER  : N9K-SUP-A
HW_REV          : 0.5050
===== System Info DONE =====
"""
diagup = '([\w\d]+)\s+\:\s+(\w+)\s+\w+\s+(\w+)+\s+\|\s(\w+)'
match1 = re.findall(diagup, show_mod, re.MULTILINE)
fanpsu = '([\w\d]+)\s+\:\s+([a-z]+\s+[a-z]+)'
match2 = re.findall(fanpsu, show_mod, re.MULTILINE)
psu_cn = re.search(r'SERIAL_NUMBER1  : (SAL[0-9]{4}[0-9A-Z]{4})',show_mod)
cxp='''
01 999.99 999 00000
02 235.04 100 00965
03 072.36 097 00803
04 068.76 096 00722
05 061.84 098 00600
06 053.93 098 00899
07 068.62 097 01022
08 050.16 098 00214
09 999.99 999 00000
10 137.14 035 00001
'''
led1_expect = '09 999.99 999 00000'
led1_output = '[0-1][0-9]\s([0-9]{3}).[0-9]{2}\s[0-9]{3}\s[0-9]{5}'
led1_match = re.findall(led1_output, cxp, re.MULTILINE)
led1_name = ['N', 'BCN', 'SUP', 'FAB', 'IOM', 'PSU', 'FAN', 'PWRMGMT', 'N', 'N']

print(led1_match)
print(len(led1_match))
print('ledtest system {} on'.format(led1_name[3].lower()))

print(match1)
print(match2)
print(psu_cn)

if psu_cn == None:
    print('psu sn error')
else:
    print(psu_cn.group(1))
fm_list=[]
for fm in fm_list:
    print(fm)
print ('PSU3'.lower())
ttt= {'PSU3':'1234567','PSU4':'1234568'}

print(ttt['PSU4'])
#ttt= ttt.split('PSU')[1]
#ttt=ttt.split(':')[0]
#print('PSU'+str(int(ttt)-2))
'''
a = 'Python'
try:
	print(a[len(a) + 1])
except Exception as e:
  	raise IndexError('Wrong Index') from e
end
'''
'''
names1 = ['Amir', 'Barry', 'Charles', 'Dao']
#names2 = [name.lower() for name in names1]
names2 = [name for name in names1]
print (names2)
print (names2[2][0])
c
'''
'''
import re
sum = 0

pattern = 'back'
if re.match(pattern, 'backup.txt'):
	sum += 1
if re.match(pattern, 'text.back'):
	sum += 2
if re.search(pattern, 'backup.txt'):
	sum += 4
if re.search(pattern, 'text.back'):
	sum += 8
print (sum)
13
'''
'''
a = 'Ian'
c = 'Hey'
b = 'I'
d = 'am'
#HeyIamIan!
#print('{c}{b}{d}{a}'.format(a=a,b=b,c=c,d=d))
print('{}{}{}{}'.format(a,b,c,d))
'''
'''
days_of_week = ['Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
  'Sunday']

months = ['Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec']

#print ('DAYS: {},\rMONTHS: {}'.format(days_of_week, months))
print ('DAYS: {},\r\nMONTHS: {}'.format(days_of_week, months))
'''
'''
def simple_function():
	"""This is a cool simple function that returns 1"""
	return 1

print (simple_Function.__doc__[10:14])
'''
'''
def a(b, c, d):
  pass
'''
'''
a= 'I love you abc 123 ef 345 gh'
print(a[:3])
print(a[-1:])
print(a[-8:-3:2])
'''
'''
class Person:
	def __init__(self, id):
		self.id = id

steve = Person(100)

steve.__dict__['age'] = 25
print (steve.id)
print (steve.age)
print (steve.age + len(steve.__dict__))
27

class Account:
	def __init__(self, id):
   		self.id = id
   		id = 666

acc = Account(123)
print (acc.id)
'''
'''
foo = (3, 4, 5)
print (type(foo))
print (type([1,2]))

def dostuff(param1, **param2):
	print(type(param2))

dostuff('capitals', Arizona='Phoenix',
California='Sacramento', Texas='Austin')


a = 'Python'
try:
  	print(a[len(a) + 1])
except Exception as e:
	raise TypeError('123') from e

'''