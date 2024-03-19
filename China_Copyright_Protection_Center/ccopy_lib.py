import os
import http.client
import json
import time
import random
from dotenv import find_dotenv, load_dotenv
from uid.uid0 import uid0_list
from uid.uid1 import uid1_list
from uid.uid2 import uid2_list
from uid.uid3 import uid3_list
from uid.uid4 import uid4_list
from uid.uid5 import uid5_list
from uid.uid6 import uid6_list
from uid.uid7 import uid7_list

# from lib.Download import download_source

uid_list = [uid0_list, uid1_list, uid2_list, uid3_list, uid4_list, uid5_list, uid6_list, uid7_list]

load_dotenv(find_dotenv('.env'))
env_dist = os.environ

storageUrl = 'https://storage.ccopyright.com.cn/scrr/'



def get_data(url, payload):
    ccopy_host = env_dist.get('ccopy_host')
    authorization_key = env_dist.get('ccopy_authorization_key')
    authorization_token = env_dist.get('ccopy_authorization_token')
    conn = http.client.HTTPSConnection(ccopy_host)
    headers = {
        'Authorization': 'Bearer ' + authorization_token,
        'Authorization_key': authorization_key,
        'Authorization_token': authorization_token,
        'Device': 'pc',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': ccopy_host,
        'Connection': 'keep-alive',
        'Cookie': 'wzws_sessionid=gDU4LjQ4LjI2LjEyNIFkNDliMjOCYzM5YjRmoGUneOU='
    }
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


# uid = '640553895260762112' # 个人-项月文
# uid = 'M488739788363579392' # 组织-松发
# uid = 'M488232' # 组织-不存在
# uid = 'S709865264472309760'  # 组织-个人-刘陶
# uid = 'M48823'  # 组织-陶大

def sub_account_list(index):
    payload = env_dist.get('ccopy_payload_sub_account_list')
    e_url = env_dist.get('ccopy_url_sub_account_list')
    count = 1
    for uid in uid_list[index]:
        # for index in range(start_index, end_index):
        # db_lib = lib.db_op()
        # uid = "M" + str(index)
        print("====No.：" + str(count) + "|" + uid + "====")
        url = e_url + uid
        timestamp = str(int(time.mktime(time.localtime(time.time()))))
        try:
            data_json = get_data(url, payload)
            re_data = json.dumps(data_json['data'], ensure_ascii=False)
            # print(url, re_data, timestamp)
            # print(data_str)
            if data_json['returnCode'] == 'SUCCESS':
                if data_json['data']:
                    data_str = "'" + url + "','" + re_data + "','" + timestamp + "'"
                    # db_lib.add_scanner(values=data_str)
                    print("success:" + str(data_json['data']))
                else:
                    print("success: No Data")
            else:
                print("fail:" + str(data_json['message']))
        except Exception as e:
            print("--exception handler--")
            if str(e) == 'Expecting value: line 1 column 1 (char 0)':
                print("结束批处理\n结束URL：" + url + "\n结束UID：" + uid + "\n结束时间：" + str(
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                break
            elif str(e) == 'data':
                print('No Data')
                pass
            else:
                print(str(e))
                pass
        # db_lib.close()
        time.sleep(random.randint(1, 2))
        count = count + 1
        continue


def account_detail(index):
    payload = env_dist.get('ccopy_payload_account_detail')
    e_url = env_dist.get('ccopy_url_account_detail')
    count = 1
    for uid in uid_list[index]:
        # for index in range(start_index, end_index):
        # db_lib = lib.db_op()
        # uid = "M" + str(index)
        print("====No.：" + str(count) + "|" + uid + "====")
        url = e_url + uid
        timestamp = str(int(time.mktime(time.localtime(time.time()))))
        try:
            data_json = get_data(url, payload)
            re_data = json.dumps(data_json['data'], ensure_ascii=False)
            # print(url, re_data, timestamp)
            # print(data_str)
            if data_json['returnCode'] == 'SUCCESS':
                if data_json['data']:
                    data_str = "'" + url + "','" + re_data + "','" + timestamp + "'"
                    # db_lib.add_scanner(values=data_str)
                    print("success:" + str(data_json['data']))
                else:
                    print("success: No Data")
            else:
                print("fail:" + str(data_json['message']))
        except Exception as e:
            print("--exception handler--")
            if str(e) == 'Expecting value: line 1 column 1 (char 0)':
                print("结束批处理\n结束URL：" + url + "\n结束UID：" + uid + "\n结束时间：" + str(
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                break
            elif str(e) == 'data':
                print('No Data')
                pass
            else:
                print(str(e))
                pass
        # db_lib.close()
        time.sleep(random.randint(1, 2))
        count = count + 1
        continue
