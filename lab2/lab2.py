def main(number):
	powersCount = 1 #количество степеней двойки

	lenghtForPowers = len(number)
	twoInPowers = [1] #Единица есть всегда тк 0 степень
	falseNum = 0

	#получаем сколько степеней двойки
	while lenghtForPowers>2:
		twoInPowers.append(2**(powersCount))
		powersCount+=1
		lenghtForPowers /= 2

		

	for r in twoInPowers:
		summIndex = 0 #переменная для подсчета сумм по мод 2
		for step in range(r, len(number)+1, 2*r): #шаг и начало зависят от степени
			if step == r: #убираем саму r (- тк в след ходу она +)
				summIndex -= int(number[r-1])
			for i in range(r):
				if step-1+i<=len(number): #проверка выхода за границу
					summIndex += int(number[step-1+i])
		if summIndex%2 != int(number[r-1]): # подсчет сумм по мод 2
			falseNum += r
	if falseNum != 0: #проверка есть ли ошибка
		number = number[:falseNum-1] + str(abs(int(number[falseNum-1])-1)) + number[falseNum:]
	else:
		falseNum = "ошибки нету"
	print(f"Правильное сообщение: {number}, индекс ошибки: {falseNum}")

#примеры с лабы
main("1010000")
main("1100010")
main("1100100")
main("1001101")
main("001010100110101")
#пример сообщения без ошибки
main("1110000")