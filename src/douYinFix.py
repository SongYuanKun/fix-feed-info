import time
import urllib.parse
import uuid
from urllib import parse

import requests

if __name__ == '__main__':
    headers = {'Content-Type': 'application/json'}
    list = [
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=5efbd76cb7524013836c3647a66c250c&adid=1691783412577284&creativeid=1691783479389244&creativetype=15&clickid=ELzYzcqw1YADGPf0wKiZ9e8GIK2T8KiZ9fsEMAw4wbgCQiIyMDIxMDIxOTIxNTAzNDAxMDE1MTE5MTA3OTMzMzAxQTQzSMG4ApABAA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=5efbd76cb7524013836c3647a66c250c&adid=1691783412577284&creativeid=1691783479389244&creativetype=15&clickid=ELzYzcqw1YADGOL8pNOPAiDr4_P_lQEwDDjBuAJCIjIwMjEwMjIwMDUyNDI5MDEwMTMzMDU0MTUzMTU1NTVCMzhIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=27572c42df364b448d3e3b91ce9decfc&adid=1690580586446867&creativeid=1691684334691335&creativetype=15&clickid=EIfI3Z6_0oADGJOPgLHg9K0FINPlsPCVATAMONjqAUIiMjAyMTAyMjAwNTU5MzcwMTAyMTIxNjQwMTQ0MzA3MDE3RUix6gGQAQA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=e407e6b309ba4a1b9d73d2f61fdfdf93&adid=1691778240099380&creativeid=1691778960656403&creativetype=15&clickid=EJOQ9N-f1YADGNTk4K-g9LEFIM2k4OOb9OMDMAw4htsBQiIyMDIxMDIyMDA2MDUyOTAxMDIxMjE1NzIwODE5MDcyNTcxSMG4ApABAA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=27572c42df364b448d3e3b91ce9decfc&adid=1690580586446867&creativeid=1691684334691335&creativetype=15&clickid=EIfI3Z6_0oADGP615d2YAyDM4bPu5AEwDDjh2gFCIjIwMjEwMjIwMDYzMzQyMDEwMTMzMDU0MTU3MDk1M0ExNEFIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?huohua_sign=23adf95c12ecdade653edf329b58a44d&ch_i=73620aea9a354e76b58ddb4d0dbafbec&adid=1692028822540334&creativeid=1692035256859694&creativetype=15&clickid=EK74usPa3IADGO2bgOHs9YYHIKf10fr-9UMwDDiK2wFCIjIwMjEwMjIwMDY0NTUwMDEwMjEyMjA0MDE5NDcwNzQ1RDRIwbgCkAEA&launch_mode=standard',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=7fd7ff9278c6438fbfd69ddc4d265101&adid=1691234646476855&creativeid=1691235781955646&creativetype=15&clickid=EL6gj6C4xYADGPjY8NS99ZACIIfToLPD9eMHMAw41JwBQiIyMDIxMDIyMDA2NTUzMDAxMDEzMzA1NDE0ODJDMEU1MTI3SMG4ApABAA',
        'https://market-api.huohua.cn/landing/v4/b4801f41d5994e1aa0c70d7bbb69a986?huohua_sign=b332d898126973bbe896c34dac8a40d8&ch_i=da50729e125e48eba6b224d7c8a091dd&adid=1689649996760123&creativeid=1689931597016076&creativetype=15&clickid=EIzYo-S9n4ADGJe_lt3FAiCLxIWq_gEwDDiG2wFCIjIwMjEwMjIwMDcwMzQ5MDEwMjA0MDUwMDgzMTIwNzgwMjRIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/b4801f41d5994e1aa0c70d7bbb69a986?huohua_sign=b332d898126973bbe896c34dac8a40d8&ch_i=da50729e125e48eba6b224d7c8a091dd&adid=1689649996760123&creativeid=1689931597016076&creativetype=15&clickid=EIzYo-S9n4ADGNieoYCZ9Xsgl_ag3cn1vwYwDDiG2wFCIjIwMjEwMjIwMDcwODAzMDEwMjEyMTQ4MDE2MTkwNzgyN0VIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?huohua_sign=23adf95c12ecdade653edf329b58a44d&ch_i=51c290c853774458ba79f4c1e06be6d4&adid=1692031247780919&creativeid=1692031448270887&creativetype=15&clickid=EKeQsavM3IADGPb3gujtAiC5xLKHigEwDDjBuAJCIjIwMjEwMjIwMDY1MDE4MDEwMTMzMDU0MTY3NUQ1NzA0OTlIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?huohua_sign=23adf95c12ecdade653edf329b58a44d&ch_i=31705af93d0341148566e0fabd61fb03&adid=1692026159546414&creativeid=1692026716775543&creativetype=15&clickid=EPfIndu63IADGNK4rLuZAyC12tG-5QEwDDjBuAJCIjIwMjEwMjIwMDcyOTA0MDEwMjA0MDU5MDkyNDY5MjZDNkJIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=58edfe35dd7b4670b4a876e83f198a67&adid=1692121894108189&creativeid=1692133544840244&creativetype=15&clickid=ELSY6dbI34ADGPWf5LrCAiDf462tgAIwDDjBuAJCIjIwMjEwMjIwMDc0NDI1MDEwMjEyMTg1MTY0NTc5MUY0NjJIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?huohua_sign=23adf95c12ecdade653edf329b58a44d&ch_i=31705af93d0341148566e0fabd61fb03&adid=1692026159546414&creativeid=1692026716775543&creativetype=15&clickid=EPfIndu63IADGJnA_K8NIL7e4Mbd9cEHMAw4vssBQiIyMDIxMDIyMDA3NDcwMjAxMDE1MDIxODEzNTA3MERENDczSMG4ApABAA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?huohua_sign=23adf95c12ecdade653edf329b58a44d&ch_i=31705af93d0341148566e0fabd61fb03&adid=1692026159546414&creativeid=1692026716775543&creativetype=15&clickid=EPfIndu63IADGI_8jPwzIN_C3eaGAjAOOMG4AkIiMjAyMTAyMjAwNzQ2MDAwMTAxMzMwNTUwMjM1RjVDNDREQUjBuAKQAQA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=58edfe35dd7b4670b4a876e83f198a67&adid=1692121894108189&creativeid=1692133545592836&creativetype=15&clickid=EISQl9fI34ADGPi_79maAyDD0vj3_gEwDDjBuAJCIjIwMjEwMjIwMDc1MTMwMDEwMTUwMjIyMDMyMUQzOEJGMTlIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?huohua_sign=23adf95c12ecdade653edf329b58a44d&ch_i=4286e3868dae49d9937e340bd6805fbc&adid=1692115443760163&creativeid=1692127282406430&creativetype=15&clickid=EJ7I1Kyx34ADGIyaqcvZAiDIgrnKhAIwDDiG2wFCIjIwMjEwMjIwMDkxMzQwMDEwMjEyMDc1MDk0NUIwOTE0QzVIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=c6b56f80d5a14a1b8d9f9d590758195b&adid=1692125924611117&creativeid=1692126912176222&creativetype=15&clickid=EN7Aj_yv34ADGLWI58P1AiCnm8C27fTjBDAMOMG4AkIiMjAyMTAyMjAxMDI2MTMwMTAyMTIxNDYyMTMxRjk3NkI0MEjBuAKQAQA',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=a7f14b125ed944d382bf98beb334785d&adid=1691328721581067&creativeid=1691342312281096&creativetype=15&clickid=EIio3o3FyIADGKOpn5SLAiDy-tTglAEwDDjBuAJCIjIwMjEwMjIwMTAzNTQ0MDEwMjA0MDUwMjA1MzY5QUI1NzlIwbgCkAEA',
        'https://market-api.huohua.cn/landing/v4/077a19c5bc4546d48192c19c4175f74c?adid=1691409656006165&ch_i=04405ac79a574dc7b55d84bc39bf63eb&clickid=EJWM3f2_yoADGM2ouPKJkIADKI7wx_-ttIAD&creativeid=1691409656006165&creativetype=1&huohua_sign=23adf95c12ecdade653edf329b58a44d',
        'https://market-api.huohua.cn/landing/v4/877127d148cf43e4bf509299faf16b2f?huohua_sign=6e79419e7be7ee712d42eff957e6604c&ch_i=c353b2349a9a4ab9ab249962f83e0002&adid=1692120466557005&creativeid=1692121505095694&creativetype=15&clickid=EI7A6emb34ADGJj_oIH_9e8BIIj_gLru9Y8FMAw4s-oBQiIyMDIxMDIyMDExMjU0ODAxMDEzMzAzODEwNjFBMDAwQkRFSMG4ApABAA']

    timestamp = str(int(time.time()))
    uid = str(uuid.uuid4())
    nonce = ''.join(uid.split('-'))

    event_type = 3
    for link in list:
        url = "https://ad.toutiao.com/track/activate/"
        s = requests.get(url, params={
            'link': link,
            'event_type': event_type,
            'conv_time': timestamp,
        })
        print(url + '-------------' + str(s.content))
