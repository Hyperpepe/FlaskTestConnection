import json
import base64
import io
import cv2
import requests
import socket
import re


class DataChecker:
    def __init__(self, data):
        self.data = data
        self.operator = data.get("operator")

        self.listen_port_info = data.get('listenPortInfo')
        self.isolater_info = data.get('IsolaterInfo')
        self.pic_info = data.get('picinfo')

        self.ip_address = self.listen_port_info.get('IpAddress')
        self.port = self.listen_port_info.get('Port')

        self.issue_number = self.isolater_info.get('issueNumber')
        self.isolater_id = self.isolater_info.get('IsolaterID')
        self.isolater_name = self.isolater_info.get('IsolaterName')
        self.isolater_cmd = self.isolater_info.get('IsolaterCmd')

        self.a_pic_info = self.pic_info.get('APicInfo')
        self.b_pic_info = self.pic_info.get('BPicInfo')
        self.c_pic_info = self.pic_info.get('CPicInfo')

    # 检查转化后的图片是否可以读取
    def check_image_valid(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            # 图片加载失败，不完整
            return False
        else:
            # 图片加载成功，完整
            return True

    # 解析base64编码的图片
    def base64_decode_jpg(self, picinfo, picname):
        base64_code = re.sub('^data:image/.+;base64,', '', picinfo)
        image_data = base64.b64decode(base64_code)
        buf = io.BytesIO(image_data)
        filename = 'image' + picname + '.jpg'
        try:
            with open(filename, 'wb') as f:
                f.write(buf.getbuffer())
            self.check_image_valid('./filename')
            print("图片可以读取")
            return True
        except Exception:
            return picname

    # ping 通端口返回True
    def request_post(self, ip_address, port, bodyin):
        host = "http://" + ip_address + ":" + port + "/"
        login_url = "/AICheckIsolaterjpg"
        url = host + login_url  # 拼接地址
        r = requests.post(url=url, json=bodyin)
        print(r.text)

    # 写入json文件
    def write_json_data_to_file(self, params):
        with open('yolov5_config.json', 'w') as r:
            json.dump(params, r)

    def check_args_ipaddress(self, data):
        # ret = False
        if data:
            operator = data['operator']
            listen_port_info = data.get('listenPortInfo')  # 读取 listenPortInfo 中的 IpAddress 和 Port
            if listen_port_info:
                ip_address = listen_port_info.get('IpAddress')
                port = listen_port_info.get('Port')
                if ip_address and port:
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

    def check_args_IsolaterInfo(self, data):
        isolater_info = data.get('IsolaterInfo')  # 读取 IsolaterInfo 中的 issueNumber、IsolaterID、IsolaterName 和 IsolaterCmd
        if isolater_info:
            print("取到整个info")
            issue_number = isolater_info.get('issueNumber')
            isolater_id = isolater_info.get('IsolaterID')
            isolater_name = isolater_info.get('IsolaterName')
            isolater_cmd = isolater_info.get('IsolaterCmd')
            # isolater_cmd = int(isolater_cmd)
            if all(value for value in isolater_info.values()):
                print("IsolaterInfo 中所有值都有值")
                if (isolater_cmd == "1" or isolater_cmd == "2"):
                    print("isolater_cmd 是数字 1 或 2")
                    ret = True
                else:
                    print("isolater_cmd 不是数字 1 或 2")
                    ret = False
            else:
                print("IsolaterInfo 中有值为空")
                ret = False
        else:
            print("取不到整个info")
            ret = False
        return ret

    def check_args_picinfo(self, data):
        pic_info = data.get('picinfo')  # 读取 picinfo 中的 APicInfo、BPicInfo 和 CPicInfo
        if pic_info:
            a_pic_info = pic_info.get('APicInfo')
            b_pic_info = pic_info.get('BPicInfo')
            c_pic_info = pic_info.get('CPicInfo')
            if a_pic_info and b_pic_info and c_pic_info:
                reta = self.base64_decode_jpg(a_pic_info, 'APicInfo')
                retb = self.base64_decode_jpg(b_pic_info, 'BPicInfo')
                retc = self.base64_decode_jpg(c_pic_info, 'CPicInfo')
                if reta and retc and retb:
                    print("base64图片检查——以下参数符合条件:", reta, retb, retc)
                    return True
                else:
                    print("base64图片检查——以下参数不符合条件:", reta, retb, retc)
                    return False
        else:
            print("pic_info 不完整")
            return False
