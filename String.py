# strr = "abc"
# help(strr.islower) #it's called INTROSPECTION

# #string creation
my_str = '''abc'''
ch = "abc"
x = 'abc'
print(my_str)



# #Casting
number = 454
new_string = str(234)
print(number)
print(int("1234"))



# #assign new value to variable, identity will change
val = 5
print(id(val))
val = 9
print(id(val))



# # Concatenation
string_one = "Aumit"
string_two = string_one + "Hasan"
print(string_two)


#  introspection
my_string = "Aumit Hasan"
print(dir(int)) #all attriute & method for int 
print(dir(str)) #all attriute & method for string object 
help(my_string.upper) #know about a method 
print(type(my_string)) # tell the type of variable



# String Methods
my_string = " Aumit Hasan"
print(my_string.upper())
print(my_string.lower())
print(my_string.strip()) # Remove space at the beginning & End 
print(my_string.count('Aumit')) # 'any_char_or_string'
print(my_string.find('hasan'))  # if find return pos else -1

my_string.replace('Aumit' , 'hi') #first one will be replaced by 2nd one
# after replacing it will create a instance & will not chance the real string. So we need a different variale.
new_str = my_string.replace('Aumit' , 'hi') 
# or we can use like this // my_string = my_string.replace('Aumit', 'hi')
# then it will change the original stirng
print(new_str)





