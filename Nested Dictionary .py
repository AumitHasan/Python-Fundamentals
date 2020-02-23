
#Nested Dictionary

Dict = { 'Dict_1' : {"name":"Aumit", "height":5.6},
        'Dict_2' : {"one":1, 5:"Five"} }

Dict['Dict_1']['age'] = 25              #adding more elements


print(Dict['Dict_2'][5])                #print index of Dict
print(Dict['Dict_1'].keys())            #print all keys

del Dict['Dict_1']
#Dict.pop('Dict_1')



