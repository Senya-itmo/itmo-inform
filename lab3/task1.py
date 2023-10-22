#код душевно больного
import re

def crazy_code(text, smile):
	print(f"кол-во символов с помощью регулярки: {len(re.findall(smile, text))}")

#человеческий код
def normal_code(text, smile):

	count = 0

	while smile in text:
		count+=1
		text = text[text.find(smile)+len(smile)-1:]

	print(f"кол-во смайлов самостоятельно: {count}")

#наш смайл
def smileSettings(i):
	print(f'face: {i%6}\nnose: {i%4}\nmouse: {i%7}\n\n')



icu_number = 408138
#smileSettings(icu_number)

smile = r':-{\|'
smile2 = ":-{|"
s_list = []
s_list.append('aaa:-{|bb:-{|c:-{|:<):-{|')
s_list.append(':-{|hrqhq4hshh:-{|4q3hqrha:-{|')
s_list.append(':-{|:-{:-{|:{|')
s_list.append(':-{|nnnnn:-{|')
s_list.append('fjkagj[qnqbn]')

for s in s_list:
	crazy_code(s, smile)
	normal_code(s, smile2)
	print()