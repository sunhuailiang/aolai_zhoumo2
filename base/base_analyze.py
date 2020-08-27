import yaml

def analyze_data(file_name, case_key):
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f,)[case_key]
        temp_list = list()
        temp_list.extend(data.values())
        return temp_list