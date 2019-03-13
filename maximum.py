thislist=[]
maxi=0
for i in range(0,10):
    number = int(input('enter the number   '))
    thislist.append(number)
print(thislist)
for x in thislist:
    if x > maxi:
        maxi = x
print('maximum is', maxi)
