import os
import json

langs_directory = 'langs'

if not os.path.exists(langs_directory):
    os.makedirs(langs_directory)

with open("data/complete_output.json") as f:
    obj = json.load(f)
    langs = list()
    for key in obj:
        with open(f"{langs_directory}/{key}.json", 'w') as output_file:
            print(obj[key], file=output_file)

        langs.append({'lang': key,
                      'files': len(obj[key]['reports']),
                      'lines': obj[key]['code']
                      + obj[key]['comments']
                      + obj[key]['blanks'],
                      'code': obj[key]['code'],
                      'comments': obj[key]['comments'],
                      'blanks': obj[key]['blanks']})
    with open("data/minimized_output.json", 'w') as output_file:
        json.dump(langs, output_file)
