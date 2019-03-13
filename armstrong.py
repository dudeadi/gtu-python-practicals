def armstrong():
    x = int(input('enter the number : '))
    temp = x
    summ = 0
    while temp > 0:
        temp = int(temp)
        digit = temp % 10
        summ += digit ** 3
        temp = temp/10
    if x == summ:
        print('entered number is armstrong number :')
    else:
        print('entered number is not armstrong number :')
    
armstrong()
