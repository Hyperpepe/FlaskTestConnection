import base64
import cv2
import flask
import numpy as np
from flask import json, request, render_template
# from flask_cors import CORS, cross_origin
api = flask.Flask(__name__)

received_data = None  # 用于存储接收到的数据z


def convert_base64_to_image(encoded_data):
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img
@api.route('/GISdetect', methods=['post'])
def main():
    data = request.get_json()
    APicInfo_base64 = data["picinfo"]["APicInfo"]
    BPicInfo_base64 = data["picinfo"]["BPicInfo"]
    CPicInfo_base64 = data["picinfo"]["CPicInfo"]

    imgA = convert_base64_to_image(APicInfo_base64)
    imgB = convert_base64_to_image(BPicInfo_base64)
    imgC = convert_base64_to_image(CPicInfo_base64)
    cv2.imshow('Image A', imgA)
    cv2.imshow('Image B', imgB)
    cv2.imshow('Image C', imgC)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(json.dumps(data, indent=4))  # 这样会美化输出的JSON数据
    ren = {'msg': 'COPY_THAT', 'msg_code': 202}
    return json.dumps(ren, ensure_ascii=False)
    # return render_template('display.html', data=data)
# @api.route('/', methods=['GET'])
# def display():
#     return render_template('display.html', data=received_data)
@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 201}
    return json.dumps(ren, ensure_ascii=False)

if __name__ == '__main__':
    api.run(port=9999, debug=True, host='0.0.0.0')
