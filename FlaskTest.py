import flask
from flask import json,request
from utils import check_args_ipaddress,check_args_picinfo,check_args_IsolaterInfo

api = flask.Flask(__name__)


@api.route('/AICheckIsolaterjpg', methods=['post'])
def main():
    data = request.get_json()
    IPret = check_args_ipaddress(data)
    Isoret = check_args_IsolaterInfo(data)
    Picret = check_args_picinfo(data)
    isArgsOk = IPret and Isoret and Picret
    if isArgsOk:
        ren = {'msg': 'COPY_THAT', 'msg_code': 202}
    else:
        ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}
        print(IPret, Isoret, Picret)

    return json.dumps(ren, ensure_ascii=False)

@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 101}
    return json.dumps(ren, ensure_ascii=False)

if __name__ == '__main__':
    api.run(port=5000, debug=True, host='0.0.0.0')
