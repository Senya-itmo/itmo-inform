import json, yaml

def task1():
    json_text= open("text.json", "r").read()
    python_dict=json.loads(json_text)
    ymal_text=yaml.dump(python_dict, allow_unicode=True)
    yaml_file = open("text.yaml", "w+")
    yaml_file.write(ymal_text)