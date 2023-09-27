import json
import sqlite3
import threading
from datetime import datetime

import requests
from init_datebase import insert_into_test,insert_into_getcurrentfarm,insert_into_setDefault,insert_into_GPIO,insert_into_checkAI,insert_into_gisdetect_status,insert_into_GISdetect_result,insert_into_GISdetect
conn = sqlite3.connect('testStore.sqlite')
cursor = conn.cursor()


# 定义API测试函数

# 定义线程类
class ApiTestThread(threading.Thread):
    def __init__(self, base_url,sn):
        threading.Thread.__init__(self)
        self.base_url = base_url
        self.sn = sn


    def run(self):
        for i in range(100):
            self.test_api_test(self.base_url)

            # self.test_api_GISdetect(self.base_url)

            # self.test_api_LED(self.base_url)
            #
            # self.test_api_RELAY(self.base_url)

    def test_api_test(self, base_url):
        try:
            # /test 接口
            response = requests.post(f"http://{base_url}/test")
            response_dict = json.loads(response.text)
            current_time = datetime.now()
            current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # 精确到毫秒
            response_dict["Time"] = current_time_str
            insert_into_test(db_name=self.sn, table_name=f"{self.sn}_test",data=response_dict)
        except Exception as e:
            print(f"Exception for http://{base_url}: {e}")

    # def test_api_GISdetect(self, base_url):
    #     try:
    #         # /GISdetect 接口
    #         response = requests.post(f"{base_url}/test")
    #
    #     except AssertionError:
    #         print(f"Assertion Error for {base_url}")
    #     except Exception as e:
    #         print(f"Exception for {base_url}: {e}")

    def test_api_LED(self, base_url):
        try:
            # /checkled 接口
            response = requests.post(f"{base_url}/test")

        except AssertionError:
            print(f"Assertion Error for {base_url}")
        except Exception as e:
            print(f"Exception for {base_url}: {e}")

    def test_api_RELAY(self, base_url):
        try:
            # /checkrelay 接口
            response = requests.post(f"{base_url}/test")

        except AssertionError:
            print(f"Assertion Error for {base_url}")
        except Exception as e:
            print(f"Exception for {base_url}: {e}")


# 主程序
if __name__ == "__main__":
    ip_to_sn = {
        '192.168.3.32:5000': 'GIS230901002',
        '192.168.3.34:5000': 'GIS230901003',
        '192.168.3.35:5000': 'GIS230901004',
        '192.168.3.36:5000': 'GIS230901005',
        '192.168.3.37:5000': 'GIS230901006',
        '192.168.3.38:5000': 'GIS230901007',
        '192.168.3.39:5000': 'GIS230901008',
        '192.168.3.40:5000': 'GIS230901009',
        '192.168.3.41:5000': 'GIS230901010',
    }
    threads = []
    # 创建并启动线程
    for url, sn in ip_to_sn.items():
        thread = ApiTestThread(url,sn)
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for t in threads:
        t.join()

    print("Completed API testing.")
