x = 1
count = 0
y = int(input('how many armstrong numbers you want :'))

while(count <= y):
    temp = x
    summ = 0
    while temp > 0:
        digit = temp % 10
        summ += digit ** 3
        temp = temp//10
    if x == summ:
        print(x)
        count = count + 1
    x+=1




