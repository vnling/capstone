import requests
import json
import sys

data_file = sys.argv[1]
result_file = sys.argv[2]
url = "https://v2.namsor.com/NamSorAPIv2/api2/json/diasporaBatch"

with open(data_file, 'r', encoding='utf-8') as f:
    with open(result_file, 'a', encoding='utf-8') as g:
        for line in f:
            full_name = line.split(',')[12]
            first_name = full_name.split(' ')[0]
            last_name = full_name.split(' ')[-1]

            payload = {
            "personalNames": [
                {
                "firstName": first_name,
                "lastName": last_name,
                }
            ]}
            headers = {
                "X-API-KEY": "",
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

            response = requests.request("POST", url, json=payload, headers=headers)

            res = json.loads(response.text)
            ethnicity = res["personalNames"][0]["ethnicity"]
            prob = res["personalNames"][0]["probabilityCalibrated"]

            result_line = line.rstrip('\n') + ',' + ethnicity + ',' + str(prob) + '\n'
            g.write(result_line)