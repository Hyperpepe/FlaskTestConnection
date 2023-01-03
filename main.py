import flask
from flask import request
import json
import base64
import io
import cv2

api = flask.Flask(__name__)


@api.route('/AICheckIsolaterjpg', methods=['post'])
def chose():
    data = request.get_json()
    # print(data)
    operator = data['operator']

    # 读取 listenPortInfo 中的 IpAddress 和 Port
    listen_port_info = data['listenPortInfo']
    isolater_info = data['IsolaterInfo']
    pic_info = data['picinfo']

    ip_address = listen_port_info['IpAddress']
    port = listen_port_info['Port']

    # 读取 IsolaterInfo 中的 issueNumber、IsolaterID、IsolaterName 和 IsolaterCmd
    # isolater_info = data['IsolaterInfo']
    # issue_number = isolater_info['issueNumber']
    # isolater_id = isolater_info['IsolaterID']
    # isolater_name = isolater_info['IsolaterName']
    # isolater_cmd = isolater_info['IsolaterCmd']

    # 读取 picinfo 中的 APicInfo、BPicInfo 和 CPicInfo
    # pic_info = data['picinfo']
    # a_pic_info = pic_info['APicInfo']
    # b_pic_info = pic_info['BPicInfo']
    # c_pic_info = pic_info['CPicInfo']




    ren = {'msg': 'COPY_THAT','args': data,'msg_code': 202}

    # ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}
    return json.dumps(ren, ensure_ascii=False)

@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 101}
    return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    api.run(port=5000, debug=True, host='0.0.0.0')
