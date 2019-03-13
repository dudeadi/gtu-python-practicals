handsome = {}
smarty = {}
p = int (input('how many entries you want to store : '))
for x in range(p):
    y = int(input('enter the key :'))
    z = input('enter the value :')
    handsome.update({y : z})
for key,value in handsome.items():
    if value not in smarty.values():
        smarty[key] = value
print(smarty)