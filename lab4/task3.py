def task3():
    def main(json_file, yaml_file):
        yaml_file.write("---")
        SpaceStatus = -1  # кол-во пробелов
        for line in json_file:
            line = line.strip()  # убираем пробелы
            line = line.replace(",", '')  # убираем запятые
            line = line.replace('"', "")  # убираем ковычки
            yaml_file.write(" " * SpaceStatus)  # кол-во отступов
            if "{" in line:
                SpaceStatus += 1
                yaml_file.write(line[:-1])
            elif "}" in line:
                SpaceStatus -= 1
            else:
                yaml_file.write(line)
            yaml_file.write("\n")  # переход на новую строку

    json_file = open("text.json", "r").read().split('\n') #разбиение файла по строкам
    yaml_file = open("text.yaml", "w+")
    json_file1 = open("text1.json", "r").read().split('\n')
    yaml_file1 = open("text1.yaml", "w+")

    main(json_file, yaml_file)
    main(json_file1, yaml_file1)