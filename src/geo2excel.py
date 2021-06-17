import csv
import json

import requests

if __name__ == '__main__':
    # QA系统
    host = 'http://10.251.127.40:8080'

    response = requests.get(host + "/geo/child/info/v2?pid=54489")
    p = json.loads(response.content)
    with open('国内所有省份+城市+区.csv', 'w', newline='') as csv_file:
        sp = csv.writer(csv_file)
        sp.writerow(["省份id", '省份名称', "城市id", '城市名称', "区id", '区名称'])
        for info in p['data']:
            if info['municipality'] == 1:
                sp.writerow([info['id'], info['name'], '', '', '', ''])
                response = requests.get(host + "/geo/child/info/v2?level=2&pid=" + str(info['id']))
                c = json.loads(response.content)
                for city in c['data']:
                    sp.writerow(['', '', '', '', city['id'], city['name'], ])
            else:
                sp.writerow([info['id'], info['name'], '', '', '', ''])
                response = requests.get(host + "/geo/child/info/v2?level=2&pid=" + str(info['id']))
                c = json.loads(response.content)
                for city in c['data']:
                    sp.writerow(['', '', city['id'], city['name'], '', ''])
                    response = requests.get(host + "/geo/child/info/v2?level=3&pid=" + str(city['id']))
                    d = json.loads(response.content)
                    for ac in d['data']:
                        sp.writerow(['', '', '', '', ac['id'], ac['name']])
