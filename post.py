import requests   #导包
import logging
logging.basicConfig(level=logging.DEBUG)
import http.client
http.client.HTTPConnection.debuglevel = 1
host="http://192.168.1.254:5000/"  #部署的服务器地址
login_url="/post"  #请求地址
url=host+login_url #拼接地址
#参数
body={
"A":"rtsp://192.168.3.6:8554/mystream",
"B":"rtsp://192.168.3.6:8554/mystream",
"C":"rtsp://192.168.3.6:8554/mystream",
"UUID":"1"
      }
#发送请求
r=requests.post(url=url,json=body)
#输出返回
print(r.text)
