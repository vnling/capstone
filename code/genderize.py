"""
takes a file name as command line arg, file should be comma-separated data 
the first element in each line in the file should be a name
generates a result file with the original name and the genderize result for the first name
"""

import sys
import requests

data_file = sys.argv[1]
result_file = sys.argv[2]

with open(data_file, 'r', encoding='utf-8') as f:
    with open(result_file, 'a', encoding='utf-8') as g:
        for line in f:
            full_name = line.split(',')[0]
            first_name = full_name.split(' ')[0]
            url = 'https://api.genderize.io?name=' + first_name 
            r = requests.get(url)
            # protect against null gender values (name not in genderize db)
            if r.json()['count']:
                result_line = line.rstrip('\n') + ',' + r.json()['gender'] + ',' + str(r.json()['probability']) + '\n'
            else:
                result_line = line.rstrip('\n') + ',' + 'None' + ',' + str(r.json()['probability']) + '\n'
            g.write(result_line)
