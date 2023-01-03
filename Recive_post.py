import flask
from flask import request
import json
import base64
import io
import cv2
import numpy as np
import requests

api = flask.Flask(__name__)


def checkjpg(base64_code):
    image_data = base64.b64decode(base64_code)
    buf = io.BytesIO(image_data)
    buf = np.frombuffer(buf.getbuffer(), np.uint8)
    if cv2.imdecode(buf, cv2.IMREAD_COLOR):
        return


def request_post(ip_address, port, bodyin):
    host = "http://" + ip_address + ":" + port + "/"
    login_url = "/AICheckIsolaterjpg"
    url = host + login_url  # 拼接地址
    requests.post(url=url, json=bodyin)


@api.route('/AICheckIsolaterjpg', methods=['post'])
def chose():
    data = request.get_json()
    # print(data)
    operator = data['operator']

    # 读取 listenPortInfo 中的 IpAddress 和 Port
    listen_port_info = data['listenPortInfo']
    # isolater_info = data['IsolaterInfo']
    pic_info = data['picinfo']
    ip_address = listen_port_info['IpAddress']
    port = listen_port_info['Port']
    # 读取 picinfo 中的 APicInfo、BPicInfo 和 CPicInfo
    a_pic_info = pic_info['APicInfo']
    b_pic_info = pic_info['BPicInfo']
    c_pic_info = pic_info['CPicInfo']
    print(listen_port_info)

    ren = {'msg': 'COPY_THAT', 'msg_code': 202}

    print(r.text)
    # ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}
    return json.dumps(ren, ensure_ascii=False)


@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 101}
    return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    api.run(port=5000, debug=True, host='0.0.0.0')
