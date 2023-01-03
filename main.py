import flask
from flask import request
import json
import base64
import io
import cv2
import numpy as np
import requests
import socket
import threading
api = flask.Flask(__name__)


def checkjpg(base64_code):
    image_data = base64.b64decode(base64_code)
    buf = io.BytesIO(image_data)
    buf = np.frombuffer(buf.getbuffer(), np.uint8)
    if cv2.imdecode(buf, cv2.IMREAD_COLOR):
        return
def is_jpeg(base64_code):
  try:
    image_data = base64.b64decode(base64_code)
    buf = io.BytesIO(image_data)
    buf = np.frombuffer(buf.getbuffer(), np.uint8)
    if cv2.imdecode(buf, cv2.IMREAD_COLOR):
      return True
  except Exception as e:
    print(e)
  return False

def request_post(ip_address, port, bodyin):
    host = "http://" + ip_address + ":" + port + "/"
    login_url = "/AICheckIsolaterjpg"
    url = host + login_url  # 拼接地址
    requests.post(url=url, json=bodyin)


def check_args_IP(data):
    # ret = False
    if data:
        operator = data['operator']
        listen_port_info = data.get('listenPortInfo')# 读取 listenPortInfo 中的 IpAddress 和 Port
        if listen_port_info:
            ip_address = listen_port_info.get('IpAddress')
            port = listen_port_info.get('Port')
            if ip_address and port :
                port = int(port)
                # 创建一个 socket
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # 连接到 IP 地址和端口
                s.connect((ip_address, port))
                print("IP 地址和端口可达")
                s.close()
                ret = True
                return ret
            else:
                ret = False
                return ret
        else:
            ret = False
            return ret
    else:
        ret = False
        return ret
def check_args_IsolaterInfo(data):
    isolater_info = data.get('IsolaterInfo')  # 读取 IsolaterInfo 中的 issueNumber、IsolaterID、IsolaterName 和 IsolaterCmd
    if isolater_info:
        issue_number = isolater_info.get('issueNumber')
        isolater_id = isolater_info.get('IsolaterID')
        isolater_name = isolater_info.get('IsolaterName')
        isolater_cmd = isolater_info.get('IsolaterCmd')
        isolater_cmd = int(isolater_cmd)
        if all(value for value in isolater_info.values()):
            print("IsolaterInfo 中所有值都有值")
            if isolater_cmd.isnumeric() and (isolater_cmd == '1' or isolater_cmd == '2'):
                print("isolater_cmd 是数字 1 或 2")
                ret = True
            else:
                print("isolater_cmd 不是数字 1 或 2")
                ret = False
        else:
            print("IsolaterInfo 中有值为空")
            ret = False
    else:
        ret = False
    return ret



@api.route('/AICheckIsolaterjpg', methods=['post'])
def chose():
    data = request.get_json()
    IPret = check_args_IP(data)
    Isoret = check_args_IsolaterInfo(data)
    isArgsOk = IPret and Isoret
    if isArgsOk:
        ren = {'msg': 'COPY_THAT', 'msg_code': 202}
    else:
        ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}

    return json.dumps(ren, ensure_ascii=False)


@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 101}
    return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    api.run(port=5000, debug=True, host='0.0.0.0')
