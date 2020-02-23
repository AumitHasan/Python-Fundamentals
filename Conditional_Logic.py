num = 6

if num > 6:
  print('true')
else:
  print('false')


if num < 6:       # < , >= , <= , not equal
  print('false')

#
if num < 6:
  print('false')
elif num > 6:
  print('false')
elif num == 6:
  print('true')

# not
if not num:
  print('True not')
else:
  print('False not')

# and or 
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
  print('Admin Page')
else:
  print('Something is wrong')


# Comapre list
a = [2, 3]
b = [2, 3]

print(id(a), id(b))
print(a == b)
print(a is b) # False bcase id of a & b is different

b = a
print(id(a), id(b))
print(a is b) # True bcase id of a & b is equal


# Check empty [], {}, ()
condition = []        
if condition:
  print('Not Empty')
else:
  print('Empty')

