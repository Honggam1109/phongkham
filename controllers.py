import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
db_path = os.getenv('db_path')
def sqlinsert(sqlstring,parameter):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sqlstring,parameter)
    conn.commit()
    cursor.close()
    conn.close()
def sqllogin(username,password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("select * from testdn where tendn = ?", (username,))
    data = cursor.fetchone()
    print(data)
    if not data:
        return False
    else:
        db_password = data[1]
        if password != db_password:
            print('mat khau khong dung')
            return False
        else:
            print('dang nhap thanh cong')
            return data[2]
