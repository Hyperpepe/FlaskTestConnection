import flask
api = flask.Flask(__name__)
@api.route('/post', methods=['post'])
def chose():
    url1 = flask.request.json.get('A')
    url2 = flask.request.json.get('B')
    url3 = flask.request.json.get('C')
    UUID = flask.request.json.get('UUID')
    if url1 and url2 and url3:
        ren = {'msg': 'COPY_THAT', 'UUID': UUID, 'msg_code': 202}
        stream = newtxt(url1, url2, url3, UUID)
        thread = threading.Thread(target=run, args=(stream,), daemon=True)
        thread.start()
    else:
        ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}
    return json.dumps(ren, ensure_ascii=False)
# 检查rtsp流是否可用
@api.route('/CheckRTSP', methods=['post'])
def checkRTSP():
    # source_address = request.remote_addr
    url1 = flask.request.json.get('A')
    url2 = flask.request.json.get('B')
    url3 = flask.request.json.get('C')
    if not url1 or not url2 or not url3:
        # 如果缺少参数，则返回错误信息
        ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}
        return json.dumps(ren, ensure_ascii=False)
    if url1 and url2 and url3:
        urls = {'A': url1, 'B': url2, 'C': url3}
        invalid_urls = {}
        for key, url in urls.items():
            cap = cv2.VideoCapture(url)
            if not cap.isOpened():
                invalid_urls[key] = url
        if invalid_urls:
            invalid_urls = list(invalid_urls.keys())
            ren = {'msg': 'ERROR_INVALID_URLS', 'invalid_urls': invalid_urls}
        else:
            ren = {'msg': 'STREAM_AVAILABLE', 'msg_code': 2048}
    else:
        ren = {'msg': 'ERROR_NONE_ARGS', 'msg_code': 404}
    return json.dumps(ren, ensure_ascii=False)
@api.route('/test', methods=['post'])
def test():
    ren = {'msg': 'OK', 'msg_code': 101}
    return json.dumps(ren, ensure_ascii=False)

if __name__ == '__main__':
    api.run(port=5000, debug=True, host='0.0.0.0')