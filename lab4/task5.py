"""
json to csv
"""

json_file = open("text.json", "r").read().split('\n')
csv_file = open("text.csv", "w+")
firstLine = []
secondLine = []
packageName = ""
count = -1 #кол-во {


for line in json_file:
    line = line.strip()  # убираем пробелы
    line = line.replace(",", '')  # убираем запятые
    line = line.replace('"', "")  # убираем ковычки
    if "{" in line:
        count+=1
        if count>0: #пропуск первого {
            packageName = line.split(':')[0]#убираем лишние символы (: {)
    elif "}" in line:
        packageName = ""#сбрасываем PackageName при закрытии
        continue
    else:
        s_words = line.split(':')
        if len(s_words)>1: #проверка на правую левую часть
            secondLine.append(s_words[1])
            if packageName != "":
                firstLine.append(packageName + "/" + s_words[0])
            else:
                firstLine.append(s_words[0])


csv_file.write(','.join(firstLine))
csv_file.write('\n')
csv_file.write(','.join(secondLine))