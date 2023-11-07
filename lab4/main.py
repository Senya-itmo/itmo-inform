"""
Понедельник В-2 (408138 38-36 = 2)
json -> yaml
"""

def main():
    json_file = open("text.json", "r").read().split('\n') #разбиение файла по строкам
    yaml_file = open("text.yaml", "w+")
    yaml_file.write("---")

    SpaceStatus = -1 #кол-во пробелов

    for line in json_file:
        line = line.strip() #убираем лишние пробелы
        newString = []  # кастыль для удаления пробелов и тд
        for sym in line:
            if sym != ',' and sym != '"':
                newString.append(sym)
        line = ''.join(newString)
        yaml_file.write(" " * SpaceStatus)  # кол-во отступов
        if "{" in line:
            SpaceStatus += 1
            yaml_file.write(line[:-1])
        elif "}" in line:
            SpaceStatus -= 1
        else:
            yaml_file.write(line)
        yaml_file.write("\n")  # переход на новую строку
