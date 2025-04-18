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
