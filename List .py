#list creation
my_list = []
new_list = list()


#value assign
my_list = [1, "Python", 2.50, "a"]
new_list = ["x", "y", 200]


#nested list
nested_list = [my_list, new_list]


#combine list
combo_list = [10, 20]
combo_list.extend(my_list)

combo_list = my_list + new_list   #add two list


#sort list
alpha_list = [5, 1, 25, 15]
alpha_list.sort()
# tmp_list = alpha_list.sort()   // it won't work. sort & assin the result isn't possible
tmp_list = alpha_list   


#slice list
print(alpha_list[0:4])



