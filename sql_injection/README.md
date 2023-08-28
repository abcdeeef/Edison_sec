1. 这是一个判断是否为字符型SQL注入的脚本
2. 需要手动在py脚本中输入要测试的url
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/081203cf-2112-4f5e-9358-c3d86122f8bd)

3. 判断方法就是根据利用union select 注入爆出数据库的版本，然后判断页面的返回源码中是否出现响应的字段
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/98522843-9e68-4511-b27a-6aab653ca3be)

4. 如果存在字符型注入，那么执行结果为
![image](https://github.com/abcdeeef/Edison_sec/assets/87749200/2271f468-987c-42b6-a1fd-035f703da988)

5. 如果不存在。那么结果为
![Uploading image.png…]()

6. 
