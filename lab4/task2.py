import re

def task2():
    json_text= open("text.json", "r").read()
    json_text = re.split(",", json_text)
    yaml_file = open("text.yaml", "w+")
    yaml_file.write("---")

    for s in json_text:
        s = re.sub(r'}', '', s)
        s = re.sub('"', ' ', s)
        s = re.sub("\n", '', s) #удаляем лишние переносы
        s = re.sub(r'{', '\n', s) #добавляем переносы на новую строку после {
        yaml_file.write(s)
