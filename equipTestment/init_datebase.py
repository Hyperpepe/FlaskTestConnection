import os
import sqlite3


def create_tables_for_device(sn, folder_name="device_databases"):
    # 确保文件夹存在
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 连接到特定设备SN对应的SQLite数据库
    db_path = os.path.join(folder_name, f"{sn}.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 创建复杂的表
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        status TEXT,
        status_code TEXT
    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_GPIO (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        status TEXT,
        status_code TEXT
    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_checkAI (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        num TEXT,
        result TEXT,
        status TEXT,
        status_code TEXT
        
    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_setDefault (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        status TEXT,
        status_code TEXT
    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_GISdetect (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        IsolaterCmd TEXT,
        IsolaterInfo TEXT,
        timeout TEXT,
        status_code TEXT,
        status TEXT
    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_GISdetect_result (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        IsolaterCmd TEXT,
        AStatus TEXT,
        BStatus TEXT,
        CStatus TEXT,
        IsolaterInfo TEXT,
        APicInfo  TEXT,
        BPicInfo  TEXT,
        CPicInfo  TEXT,
        status_code TEXT,
        status TEXT
    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_getcurrentfarm (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
Time TEXT,
        image_blob BLOB

    )''')

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {sn}_gisdetect_status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT,
        status TEXT,
        status_code TEXT,
        threads TEXT
    )''')

    # 提交更改并关闭数据库连接
    conn.commit()
    conn.close()




# 为 _test 类型的表插入数据
def insert_into_test(db_name, table_name, data):
    conn = sqlite3.connect("./device_databases/"+db_name+".db")
    db_name = "./device_databases/" + db_name
    print(db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])
    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()

# 为 _GPIO 类型的表插入数据
def insert_into_GPIO(db_name, table_name, data):
    # 同上

    db_name = "./device_databases/" + db_name
    insert_into_test(db_name, table_name, data)

# 为 _checkAI 类型的表插入数据
def insert_into_checkAI(db_name, table_name, data):
    conn = sqlite3.connect("./device_databases/"+db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])

    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()

# 为 _setDefault 类型的表插入数据
def insert_into_setDefault(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])

    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()

# 为 _GISdetect 类型的表插入数据
def insert_into_GISdetect(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])

    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()

# 为 _GISdetect_result 类型的表插入数据
def insert_into_GISdetect_result(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])

    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()

# 为 _getcurrentfarm 类型的表插入数据
def insert_into_getcurrentfarm(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])

    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()

# 为 _gisdetect_status 类型的表插入数据
def insert_into_gisdetect_status(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    valid_data = {k: v for k, v in data.items() if v is not None}
    keys = ', '.join(valid_data.keys())
    question_marks = ', '.join(['?' for _ in valid_data])

    cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({question_marks})", list(data.values()))
    conn.commit()
    conn.close()


# # 使用函数为特定的设备SN创建表
# create_tables_for_device("GIS230901002")
# create_tables_for_device("GIS230901003")
# create_tables_for_device("GIS230901004")
# create_tables_for_device("GIS230901005")
# create_tables_for_device("GIS230901006")
# create_tables_for_device("GIS230901007")
# create_tables_for_device("GIS230901008")
# create_tables_for_device("GIS230901010")
# create_tables_for_device("GIS230901009")
