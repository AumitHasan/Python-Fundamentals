def new_func(*args, **kwargs):
  print(args)
  print(kwargs)

def func():
  #pass
  print('Check Function')

def ret_func():
  return 'hi'


#
new_func('aumit', 'hasan', age=26, edu='swe')

#
def func2(name, greeting):
  return '{} {}'.format(greeting, name)

#
print(func2('Aumit Hasan', greeting='Welcome'))

#
str = ret_func()
print(str.upper())

#
for i in range(4):
  func()




####
def department(*args, **kwargs):
  print(args)
  print(kwargs)

courses = ['math', 'english']
info = {'name':'Aumit', 'age':26}

department(*courses, **info)