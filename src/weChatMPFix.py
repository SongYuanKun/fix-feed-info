import json
import time
import uuid

import requests

if __name__ == '__main__':
    access_token = '41_4KHBsYtZyprn8qfV-C4SttkNKGQbmz3Q07FgiPKQ8jKfJucGrMgE4WFaaKfaFn2R49sMy1Y5zgpCc63AwtqzuXe-eP_kG2G1J2TpWGt0kS0K_WaVN56-t_KKOHMglItPz7Skx8h3r9lCP4YWFAXiAFAQLI'
    headers = {'Content-Type': 'application/json'}
    list = ['wx0plslnhpl7h5xe00',
            'wx05i62fi6pfiiuk00',
            'wx0vb7r7jalyjjdq00',
            'wx047p7vm2io7dxe00',
            'wx0qpy72n467xj7k00',
            'wx0onwnj5efv3rgo00',
            'wx0wsrd5jmnvhe7w00',
            'wx0q2frxjbrtvkao00',
            'wx0t5l7hpi2lhr7c00',
            'wx06jmdrue3hcgfg00',
            'wx06l3veur5brio200',
            'wx0ziwakynoyzbrc00',
            'wx0kk7zuptdho3km00',
            'wx0s3kg6o2asoxzg00',
            'wx07yd7eno4ajhz600',
            'wx0tq6coi2lxrn7200',
            'wx0in5bqsemofcvq00',
            'wx0jm7tgecyct6ro00',
            'wx0dhqivfm44u3es00',
            'wx0vis6p44wsacwu00',
            'wx06osefflnxgwko00',
            'wx0ogz4uidp276ki00',
            'wx0gwjlfy6adn6bq00',
            'wx0mj3voavimk6xi00',
            'wx02q4m2nyqabi2o00',
            'wx05f7rxvjlbt7ji00',
            'wx0ltraqqevlx2l400',
            'wx0lnkdgkcr7xeza00',
            'wx0l5rd7f3rxxct200',
            'wx02o2zw2map3bnq00',
            'wx0oflkktr2pedu200',
            'wx0sjroqxfkfejzk00',
            'wx0rngow6imarnzg00',
            'wx0hazxnbbbai6dy00',
            'wx04ay53ufk5hxty00',
            'wx0dfy5cmisvtu6400',
            'wx07henutqsfatgy00',
            'wx0zhb233igu45bg00',
            'wx0r3o3giet6cgcu00',
            'wx0eqs5enyy7tone00',
            'wx0jq3pm3ixotgyc00',
            'wx0lkjd5facbfotu00',
            'wx0ndywyevqclmea00',
            'wx0h7eswmmgimwog00',
            'wx0ots2yt2efy7di00']

    timestamp = str(int(time.time()))
    uid = str(uuid.uuid4())
    nonce = ''.join(uid.split('-'))
    for click_id in list:
        body = {"actions": [{"trace": {"click_id": click_id}, "action_time": timestamp, "action_type": "RESERVATION",
                             "url": "https://m.huohua.cn/landing/H1"}], "user_action_set_id": 1109706321}
        url = "https://api.weixin.qq.com/marketing/user_actions/add?version=v1.0&access_token=" + access_token + "&timestamp=" + timestamp + "&nonce=" + nonce
        s = requests.post(
            url,
            headers=headers, json=body)
        print(url + ' -------------' + json.dumps(body) + ' ---------------- ' + str(s.content))
