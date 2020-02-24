num = [1, 2, 3, 4, 5, 6]

#for loop
for val in num:
  if val%2: 
    continue
  if val == 6:
    break
  print(val)

#nested loop
for val in num:
  for ch in '123':
    #print(val, ch)
    pass # when we don't want to do with any part


for i in range(10): # starts at 0 ends at 9
  print(i)

for i in range(1, 10):
  print(i)


#while
x = 0
while x < 10:
  print(x)
  if x == 4: break
  x += 1