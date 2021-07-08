import csv

if __name__ == '__main__':
    channel = [
        {
            "id": 1,
            "channel_third_id": 221,
            "subject_type": 1
        },
        {
            "id": 3,
            "channel_third_id": 221,
            "subject_type": 2
        },
        {
            "id": 2,
            "channel_third_id": 221,
            "subject_type": 4
        },
        {
            "id": 4,
            "channel_third_id": 222,
            "subject_type": 1
        },
        {
            "id": 6,
            "channel_third_id": 222,
            "subject_type": 2
        },
        {
            "id": 5,
            "channel_third_id": 222,
            "subject_type": 4
        },
        {
            "id": 7,
            "channel_third_id": 223,
            "subject_type": 1
        },
        {
            "id": 9,
            "channel_third_id": 223,
            "subject_type": 2
        },
        {
            "id": 8,
            "channel_third_id": 223,
            "subject_type": 4
        },
        {
            "id": 16,
            "channel_third_id": 226,
            "subject_type": 1
        },
        {
            "id": 18,
            "channel_third_id": 226,
            "subject_type": 2
        },
        {
            "id": 17,
            "channel_third_id": 226,
            "subject_type": 4
        },
        {
            "id": 19,
            "channel_third_id": 227,
            "subject_type": 1
        },
        {
            "id": 21,
            "channel_third_id": 227,
            "subject_type": 2
        },
        {
            "id": 20,
            "channel_third_id": 227,
            "subject_type": 4
        },
        {
            "id": 22,
            "channel_third_id": 228,
            "subject_type": 1
        },
        {
            "id": 24,
            "channel_third_id": 228,
            "subject_type": 2
        },
        {
            "id": 23,
            "channel_third_id": 228,
            "subject_type": 4
        },
        {
            "id": 28,
            "channel_third_id": 230,
            "subject_type": 1
        },
        {
            "id": 30,
            "channel_third_id": 230,
            "subject_type": 2
        },
        {
            "id": 29,
            "channel_third_id": 230,
            "subject_type": 4
        },
        {
            "id": 34,
            "channel_third_id": 235,
            "subject_type": 1
        },
        {
            "id": 36,
            "channel_third_id": 235,
            "subject_type": 2
        },
        {
            "id": 35,
            "channel_third_id": 235,
            "subject_type": 4
        },
        {
            "id": 37,
            "channel_third_id": 236,
            "subject_type": 1
        },
        {
            "id": 39,
            "channel_third_id": 236,
            "subject_type": 2
        },
        {
            "id": 38,
            "channel_third_id": 236,
            "subject_type": 4
        },
        {
            "id": 40,
            "channel_third_id": 237,
            "subject_type": 1
        },
        {
            "id": 42,
            "channel_third_id": 237,
            "subject_type": 2
        },
        {
            "id": 41,
            "channel_third_id": 237,
            "subject_type": 4
        },
        {
            "id": 43,
            "channel_third_id": 238,
            "subject_type": 1
        },
        {
            "id": 45,
            "channel_third_id": 238,
            "subject_type": 2
        },
        {
            "id": 44,
            "channel_third_id": 238,
            "subject_type": 4
        },
        {
            "id": 46,
            "channel_third_id": 349,
            "subject_type": 1
        },
        {
            "id": 48,
            "channel_third_id": 349,
            "subject_type": 2
        },
        {
            "id": 47,
            "channel_third_id": 349,
            "subject_type": 4
        },
        {
            "id": 76,
            "channel_third_id": 365,
            "subject_type": 1
        },
        {
            "id": 78,
            "channel_third_id": 365,
            "subject_type": 2
        },
        {
            "id": 77,
            "channel_third_id": 365,
            "subject_type": 4
        }
    ]

    csv_reader = csv.reader(open("C:\\Users\\Administrator\\Downloads\\工作簿1.csv"))
    for row in csv_reader:
        chi3 = row[5]
        subject = row[6]
        level = row[7]
        for c in channel:
            if str(c.get("channel_third_id")) == str(chi3) and str(c.get("subject_type")) == str(subject):
                id = c.get("id")
                sql_str = "update channel_quality set activity_quality_level=" + str(
                    level) + " , clue_quality_level =" + str(level) + " where id =" + str(id) + ";"


                print(sql_str)
