import csv

from urllib3.util import url
from urllib import parse

if __name__ == '__main__':

    csv_reader = csv.reader(open("C:\\Users\\Administrator\\Downloads\\songyk.csv"))

    with open('userid-clickid--url.csv', 'w', newline='') as csv_file:

        spamwriter = csv.writer(csv_file)

        spamwriter.writerow(["user_id", 'click_id'])

        for row in csv_reader:
            q = parse.parse_qs(url.parse_url(row[1]).query)

            u = q.get("link")[0]
            q = parse.parse_qs(url.parse_url(u).query)
            if q.get("clickid") != None:
                click_id = q.get("clickid")[0]
                if click_id == '__CLICKID__':
                    continue
                spamwriter.writerow([row[0], click_id])
