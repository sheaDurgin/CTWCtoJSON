import json
import os

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# combine jsons into the a master json
def create_all_boards(jsons_dir='jsons/', all_json='all_boards.json'):
    all_data = []
    for json_file in os.listdir(jsons_dir):
        json_path = jsons_dir + json_file
        all_data += load_json(json_path)

    save_json(all_data, all_json)

if __name__ == '__main__':
    create_all_boards()
    print(f"Combined data saved to all_boards.json")
