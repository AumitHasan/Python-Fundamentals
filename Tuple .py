
empty_tuple = tuple()
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[1])
print(my_tuple[0:3])
    

new_tuple = tuple([10, 20, 30, 40]) #List casting to Tuple

new_tuple_list = list(new_tuple) #tuple to list
new_tuple_2 = tuple(new_tuple_list) #list to tuple

print(new_tuple_list, new_tuple_2)