'''
*******************************************************************************
函数名称: AICheckIsolaterjpg
描    述:应用服务请求算法服务检测信息
作    者：lxh
编写时间：2023.1.3
*******************************************************************************/
'''

import requests  # 导包
import json

host = "http://192.168.3.9:5000/"  # 部署的服务器地址，根据main.py中的服务地址而改变

login_url = "/AICheckIsolaterjpg"  # 请求地址

url = host + login_url  # 拼接地址

with open('base64_incode.json', 'rb') as p:
    params = json.load(p)  # 加载json文件
    source = params["A-result-pic"]

# 参数
body = {

    "operator": " AICheckIsolaterjpg",
    "listenPortInfo": {
        "IpAddress": "192.168.3.9",
        "Port": "17888",
    },
    "IsolaterInfo": {
        "issueNumber": "221228-51411-1",
        "IsolaterID": "51411",
        "IsolaterName": "I 间隔隔离刀闸",
        "IsolaterCmd": "1"
    },
    "picinfo": {
        "APicInfo": "data: image/jpeg;base64," + source,
        "BPicInfo": "data: image/jpeg;base64," + source,
        "CPicInfo": "data: image/jpeg;base64," + source

    }
}
# 发送请求
r = requests.post(url=url, json=body)
# 输出返回
print(r.text)
