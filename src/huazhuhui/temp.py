import json
import os

file_path = os.path.join(os.getcwd(), 'src', 'huazhuhui', 'alreadyBook.json')
print(file_path)
with open(file_path) as json_file:
    data = json.load(json_file)
    print(data)