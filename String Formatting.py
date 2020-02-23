# Old way

str_1 = "I like %s" % "Python"

tmp = "C++"
str_2 = "I like %s & %s" % ("Python",tmp)
print(str_2)

str3 = "%i not equal %i" % (1,5)
print(str3)

str3 = "%.2f & %f" %  (3.3333333, 2)
print(str3)


# New way

print("%(lang)s is fun" % {"lang":"Python"})
print("%(value)s %(x)i + %(y)f = %(z).2f & %(value)s" % {"value":"Python", "x":1, "y":3, "z":4})

print("Python is as simple as {0}, {1}, {2}" .format("a", "b", "c"))
print("Python is as simple as {1}, {0}, {2}" .format("a", "b", "c"))

ab = {"c":1, "d":2}
print("Graph a poin where x={c} and y={d}" .format(**ab))

###
name = 'Aumit Hasan'
greeting = 'Hello'

tmp = '{}, {}, welcome.'.format(greeting, name) #format string
message = f'{greeting.upper()} , {name} welcome' # F String 