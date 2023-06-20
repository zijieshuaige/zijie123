import requests
from get_token import get_token
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

pydata = {
    'accessKeyId':'hA9VcrK4JkXPjaF6@platform',
    "accessKeySecret":"3Tu0cZeYjkvyHERw1M89AgVQxhGStrJs"
}
r = requests.get('https://api.winrobot360.com/oapi/token/v2/token/create',params=pydata).json()
token = r['data']['accessToken']

headers = {
"authorization": "Bearer " + str(token)
}
#注意：输入token的时候，前面的Bearer不要动，Bearer后边加一个空格然后再输入token值！！！

response = requests.post(url=url,json=params,headers=headers)
print(response.text)
