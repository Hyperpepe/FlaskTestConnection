'''
*******************************************************************************
函数名称: AICheckIsolaterREjpg
描    述:算法服务在检测完成后推送至应用服务器信息
         此处为模拟返回时算法服务的post操作，直接运行即可，注意修改host参数
作    者：lxh
编写时间：2023.1.3
*******************************************************************************/
'''

import json
import requests
host = "http://192.168.1.254:5000/"  # 部署的服务器地址，根据main.py中的服务地址而改变
login_url = "/AICheckIsolaterREjpg"  # 请求地址
url = host + login_url  # 拼接地址
with open('base64_incode.json', 'rb') as p:
    params = json.load(p)  # 加载json文件
    source = params["A-result-pic"]
# 参数
body = {
    {
        "operator": " AICheckIsolaterREjpg",
        " IsolaterInfo": {
            " issueNumber ": "221228-51411-1",
            "IsolaterID": "51411",
            "IsolaterName": "I 间隔隔离刀闸",
            "IsolaterCmd": "1"
        },
        "picinfo": {
            "APicInfo": "data:image/jpeg;base64,"+ source,
            "BPicInfo": "data:image/jpeg;base64,"+ source,
            "CPicInfo": "data:image/jpeg;base64,"+ source
        }
    }
}
# 发送请求
r = requests.post(url=url, json=body)
# 输出返回
print(r.text)
