import flask
from flask import request
import json
import base64
import io
import cv2
import numpy as np
import requests

api = flask.Flask(__name__)


@api.route('/AICheckIsolaterREjpg', methods=['post'])
def chose():
    ren = {'msg': 'COPY_THAT', 'msg_code': 202}
    return json.dumps(ren, ensure_ascii=False)


@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 101}
    return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    api.run(port=17888, debug=True, host='0.0.0.0')
