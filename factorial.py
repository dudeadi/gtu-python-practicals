def fact(x):
    if x==1:
        return x
    else:
        return x*fact(x-1)
x = int(input('enter the number '))
print('factorial of ' +str(x) + ' is '+ str(fact(x)))
      
