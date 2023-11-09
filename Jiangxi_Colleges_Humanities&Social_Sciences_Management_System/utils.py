import http.client
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('.env'))
env = os.environ


def get_info(url, method="GET", payload=""):
    conn = http.client.HTTPConnection(env.get('base_url'), env.get('port'))
    headers = {
        'Cookie': env.get('cookie'),
        'User-Agent': 'WHU-C303/1.0.0',
        'Accept': '*/*',
        'Host': env.get('base_url') + ':' + env.get('port'),
        'Connection': 'keep-alive'
    }
    conn.request(method, url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode('utf-8')
