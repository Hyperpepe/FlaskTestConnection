'''
*******************************************************************************
函数名称: AICheckIsolaterjpg
描    述:应用服务请求算法服务检测信息
作    者：lxh
编写时间：2023.1.3
*******************************************************************************/
'''
import base64
import re

import cv2
import numpy as np
import requests
import json

def convert_base64_to_image(encoded_data):
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

host = "http://192.168.3.48:55555/"  # 部署的服务器地址，根据main.py中的服务地址而改变
login_url = "/AICheckIsolaterjpg"  # 请求地址
url = host + login_url  # 拼接地址
with open('base64_incode_opened.json', 'rb') as p:
# with open('base64_incode_closed.json', 'rb') as p:
# with open('base64_incode_running.json', 'rb') as p:
# with open('base64_incode_running2.json', 'rb') as p:
# with open('base64_incode_running3.json', 'rb') as p:
# with open('base64_incode_None.json', 'rb') as p:
    params = json.load(p)  # 加载json文件
    source = params["base64_code"]
# 参数
body = {

    "IsolaterCmd": 0,
    "IsolaterInfo": {
        "issueNumber": "221228-51411-1",
        "IsolaterID": "51411",
        "IsolaterName": "I 间隔隔离刀闸",
        "IsolaterCmd": "1"
    },
    "picinfo": {
        "APicInfo": source,
        "BPicInfo": source,
        "CPicInfo": source
    }
}
# 发送请求
r = requests.post(url=url, json=body)
response_dict = json.loads(r.text)
# print(response_dict)

APicInfo_base64 = response_dict["picinfo"]["APicInfo"]
BPicInfo_base64 = response_dict["picinfo"]["BPicInfo"]
CPicInfo_base64 = response_dict["picinfo"]["CPicInfo"]

imgA = convert_base64_to_image(APicInfo_base64)
imgB = convert_base64_to_image(BPicInfo_base64)
imgC = convert_base64_to_image(CPicInfo_base64)

cv2.imshow('Image A', imgA)
cv2.imshow('Image B', imgB)
cv2.imshow('Image C', imgC)


if "picinfo" in response_dict:
    del response_dict["picinfo"]
# 输出返回
print(response_dict)
cv2.waitKey(0)
cv2.destroyAllWindows()