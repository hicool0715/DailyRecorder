import yaml
from os import path, makedirs


class YamlHandler:
    def __init__(self, file_dir, file_name):
        self.filepath = f"{file_dir}/{file_name}"
        if not path.exists(file_dir):
            makedirs(file_dir)
        if not path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as file: pass

    def read_yaml(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data

    def write_yaml(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True)

    record_dir = '.records'