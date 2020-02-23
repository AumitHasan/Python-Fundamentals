my_string = "AumitHasan" 


# Slicing
print(my_string[1]) 
print(my_string[-1]) #reverse order 1st pos 
    # ascending order index start with 0 but Reverse order starts with 1

print(my_string[:]) #print the hole string
print(my_string[0:5]) # starts at 0 end at 4
print(my_string[1:5])
print(my_string[0:]) #starts at 0 ends at last position of string
print(my_string[:8]) #start at 0 ends at 7
print(my_string[0:-3])  #starts at 0 ends before last 3 character s
print(my_string[-3:-1]) #starts at last 3 end at last 1 (Output: sa)




# Striding 
    # (the third parameter specifies the stride or jump)
    # string[start:end:stride(jump)] start & end can be negetive
    # stride negetive means Reverse 

print(my_string[0:10:1])
print(my_string[0:10:2]) #after starting 1 char every step
print(my_string[::-2]) #same but reverse order
print(my_string[-6:-8:-1])
print(my_string[-6::1])
