#list creation
my_list = []
new_list = list()


#value assign
my_list = [1, "Python", 2.50, "a"]
new_list = ["x", "y", 200]


#nested list
nested_list = [my_list, new_list]

#Append new item to list
my_list.append('java')
my_list.append(new_list) #see what happend :) 

# insert item 
my_list.insert(0, 'new') # (location,item)

#combine list / add multiple item 
combo_list = [10, 20]
combo_list.extend(my_list)

combo_list = my_list + new_list   #add two list

# When we add multiple item we use EXTEND, for single element we use INSERT

#sort list
alpha_list = [5, 1, 25, 15]
alpha_list.sort()
# tmp_list = alpha_list.sort()   // it won't work. sort & assin the result isn't possible
tmp_list = alpha_list   


#Length of list
print(len(alpha_list))

#slice list
print(alpha_list[0:4])
print(alpha_list[-1])

#Striding list
print(alpha_list[::2])



