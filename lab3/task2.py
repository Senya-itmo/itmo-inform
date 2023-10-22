import re

def task2(text):
	if len(re.findall('/', text))!=2:
		Answer = "Не хайку. Должно быть 3 строки."
		return Answer

	sentences = text.split('/')
	counts = []
	key = [5,7,5]

	for s in sentences:
		s = s.lower()
		counts.append(len(re.findall("[аеёиоуыэюя]", s)))


	if counts == key:
		return "Хайку!" 
	else:
		return "Не хайку."


s_list = []
s_list.append("Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...")
s_list.append("Вечер за окном. / Еще один день прожит. ")
s_list.append("Вечер за окном. / Еще один день прожит. /ЩК№ШТЩ№йшпзймйтмтщцу")
s_list.append("Буби боба чел / ляляляляляляля /боба буби чел")
s_list.append("")

for s in s_list:
	print(task2(s))
