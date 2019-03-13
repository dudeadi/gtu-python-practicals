smallest= []
for x in range(10):
    y = int(input('enter a number: '))
    smallest.insert(x,y)
min = smallest[0]
for x in smallest:
    if x<min:
        min = x
print(min)    