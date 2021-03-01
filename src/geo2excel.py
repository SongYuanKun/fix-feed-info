import csv
import json

import requests

if __name__ == '__main__':
    response = requests.get("http://127.0.0.1:8080/geo/child/info/v2?pid=54489")
    p = json.loads(response.content)
    with open('国内所有城市.csv', 'w', newline='') as csv_file:
        sp = csv.writer(csv_file)
        sp.writerow(["id", '名称'])
        for info in p['data']:
            if info['municipality'] == 1:
                sp.writerow([info['id'], info['name']])
            else:
                response = requests.get("http://127.0.0.1:8080/geo/child/info/v2?level=2&pid="+str(info['id']))
                c = json.loads(response.content)
                for city in c['data']:
                    sp.writerow([city['id'], city['name']])
