square = {}
for x in range(1,16):
    y = x*x
    square.update({x : y})
for x in square:
    print(x ," : ", square[x])
