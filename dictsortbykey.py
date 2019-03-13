handsome = {}
p = int (input('how many entries you want to store : '))
for x in range(p):
    y = int(input('enter the key :'))
    z = input('enter the value :')
    handsome.update({y : z})

sorted(handsome.keys())
print(handsome)
# for x in sorted(handsome.keys()):
#     print(x," : ",handsome[x])
 