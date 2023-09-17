c = 10000000000 #наше число в системе Фибоначчи
firstFibNum, secondFibNum = 1, 1 #первое второе число Фиб
a = 0 #наше число в десятичной системе

while c > 0:
    if c % 10 == 1:
        a += secondFibNum
    firstFibNum, secondFibNum = secondFibNum, firstFibNum+secondFibNum
    c /= 10
print(f'Ответ {a}')
