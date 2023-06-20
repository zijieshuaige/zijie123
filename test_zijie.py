import requests
url = "https://api.winrobot360.com/oapi/dispatch/v2/job/start"


params = {
"accountName": "zj@fckjcsj", #机器人注册时候使用的账号名
"robotUuid": "465b720a-f041-4028-a6d2-c3ab31243bd1", #应用的uuid，可以在客户单的应用详情中获取
"params":[

    {
    "name":"填写内容", #应用参数名称1
    "value":"你好呀，字节" ,#应用参数值1
    "type":"str"
    }
]

}

headers = {
"authorization": "Bearer 8064b710-bff9-4681-a78b-d0b7191ddfb4"
}   #注意：输入token的时候，前面的Bearer不要动，Bearer后边加一个空格然后再输入token值！！！

response = requests.post(url=url,json=params,headers=headers)
print(response.text)