import re

def task3(text, group):
	sentences = text.split("\n")
	Answer = []

	for i in range(len(sentences)):

		if len(re.findall(group, sentences[i])) == 1:
			uppers = re.findall("[А-Я]", sentences[i])

			if uppers[0] == uppers[len(uppers)-2] and uppers[0] == uppers[len(uppers)-3]:
				pass
			elif len(uppers) == 4 and uppers[1] == uppers[len(uppers)-2] and uppers[1] == uppers[len(uppers)-3]:
				pass
			else:
				Answer.append(sentences[i])
		else:
			Answer.append(sentences[i])
	print('\n'.join(Answer))

text = """Петров П.П. P0000
Анищенко А.А. P33113
Примеров Е.В. P0000
Иванов И.И. P0000
Эщкеривич Иванов И.И. P0000"""
group = "P0000"
task3(text, group)