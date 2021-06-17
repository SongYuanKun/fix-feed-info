import csv

if __name__ == '__main__':

    csv_reader = csv.reader(open("C:\\Users\\Administrator\\Downloads\\export_result (3).csv"))

    with open('updateSql.sql', 'w', newline='', encoding='utf-8') as file:
        for row in csv_reader:
            userId = row[1]
            id = row[0]
            if int(id) < 1:
                continue
            sql_str = "update statistics_setting set outside_flag='market_agent:" + userId + "' where id =" + id + ";\r\n"
            file.write(sql_str)
