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

