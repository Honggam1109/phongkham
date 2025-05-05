import sqlite3
from dotenv import load_dotenv
import os
from flask import g,request

load_dotenv()
db_path = os.getenv('db_path')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row  # Trả về dạng dict-like: row["tên_cột"]
    return g.db

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
    cursor.close()
    conn.close()
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
def hienthidichvu():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    query = '''
            SELECT 
                d.dichvu_id,
                d.tendichvu,
                d.category,
                d.gia,
                d.gioi_thieu,
                h.ten_anh
            FROM dichvu d
            LEFT JOIN hinhanh_dichvu h ON d.dichvu_id = h.dichvu_id
            where h.loai = 1 
        '''
    rows = conn.execute(query).fetchall()
    conn.close()

    # Gom hình ảnh lại theo từng dịch vụ
    dichvu_dict = {}
    for row in rows:
        dv_id = row["dichvu_id"]
        if dv_id not in dichvu_dict:
            dichvu_dict[dv_id] = {
                "madichvu": dv_id,
                "tendichvu": row["tendichvu"],
                "category": row["category"],
                "gia": row["gia"],
                "gioi_thieu": row["gioi_thieu"],
                "hinh_anh": row["ten_anh"]
            }
    # Chuyển về list
    dichvus = list(dichvu_dict.values())
    return dichvus
def get_dichvu_detail(dichvu_id):
    conn = sqlite3.connect('./db/QLPK.db')
    conn.row_factory = sqlite3.Row

    # 1. Lấy thông tin dịch vụ chính
    dichvu = conn.execute("SELECT * FROM dichvu WHERE dichvu_id = ?", (dichvu_id,)).fetchone()

    # 2. Lấy lợi ích
    loiich = conn.execute("SELECT mo_ta_loi_ich FROM loiich_dich_vu WHERE dichvu_id = ?", (dichvu_id,)).fetchall()

    # 3. Lấy quy trình
    quytrinh = conn.execute("SELECT TT_thien, tieu_de, mo_ta FROM quy_trinh_dich_vu WHERE dichvu_id = ? ORDER BY TT_thien", (dichvu_id,)).fetchall()

    # 4. Lấy nhận xét khách hàng
    nhanxet = conn.execute("SELECT ten_KH, biet_danh, NX, ten_anh FROM KHNX_dichvu WHERE dichvu_id = ?", (dichvu_id,)).fetchall()

    # 5. Lấy câu hỏi thường gặp
    faq = conn.execute("SELECT mota, traloi FROM cauhoi_dichvu WHERE dichvu_id = ?", (dichvu_id,)).fetchall()

    # 6. Lấy hình ảnh
    hinhanh = conn.execute("SELECT ten_anh FROM hinhanh_dichvu WHERE dichvu_id = ? and loai = 2", (dichvu_id,)).fetchall()
    #7. lấy thông tin bác sĩ
    bacsi = conn.execute("select ten, kinh_nghiem, ten_anh, hoc_vi, chuyen_mon from bacsi where bacsi_id = ?",(dichvu_id,)).fetchone()
    return {
        "dichvu": dict(dichvu),
        "loi_ich": [row["mo_ta_loi_ich"] for row in loiich],
        "quy_trinh": [dict(row) for row in quytrinh],
        "nhan_xet": [dict(row) for row in nhanxet],
        "cau_hoi": [dict(row) for row in faq],
        "hinh_anh": [row["ten_anh"] for row in hinhanh],
        "bac_si": dict(bacsi)
    }
def get_all_bacsi_detail():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # 1. Lấy thông tin bacsi
    bacsis = conn.execute("SELECT * FROM bacsi ").fetchall()
    result = []
    for bs in bacsis:
        bacsi_id = bs["bacsi_id"]
        # 2. Lấy tag
        tags = conn.execute("SELECT mo_ta FROM bacsi_tag WHERE bacsi_id = ?", (bacsi_id,)).fetchall()

        # 3. Lấy thanh tuu
        thanhtuus = conn.execute("SELECT mo_ta FROM thanhtuu_bacsi WHERE bacsi_id = ? ", (bacsi_id,)).fetchall()

        # 4. lấy kinh nghiem
        kinhnghiem = conn.execute("SELECT mota FROM kinhnghiem_bacsi WHERE bacsi_id = ? ", (bacsi_id,)).fetchall()
        result.append({
            **dict(bs),
            "tags": [row["mo_ta"] for row in tags],
            "thanhtuu": [row["mo_ta"] for row in thanhtuus],
            "kinhnghiems":[row["mota"] for row in kinhnghiem]
        })
    return result
def get_one_bac_si_detail(bacsi_id):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # 1. Lấy thông tin bacsi
    bacsis = conn.execute("SELECT * FROM bacsi where bacsi_id = ?", (bacsi_id,)).fetchone()
    # 2. Lấy tag
    tags = conn.execute("SELECT mo_ta FROM bacsi_tag WHERE bacsi_id = ?", (bacsi_id,)).fetchall()
    # 3. Lấy thanh tuu
    thanhtuus = conn.execute("SELECT mo_ta FROM thanhtuu_bacsi WHERE bacsi_id = ? ", (bacsi_id,)).fetchall()
    # 4. lấy kinh nghiem
    kinhnghiem = conn.execute("SELECT mota FROM kinhnghiem_bacsi WHERE bacsi_id = ? ", (bacsi_id,)).fetchall()
    result = {
        **dict(bacsis),
        "tags": [row["mo_ta"] for row in tags],
        "thanhtuu": [row["mo_ta"] for row in thanhtuus],
        "kinhnghiems": [row["mota"] for row in kinhnghiem]
        }
    lichhen = conn.execute("select * from v_lich_hen_benh_nhan where bacsi_id = ?",(bacsi_id,)).fetchall()
    lh = []
    for l in lichhen:
        lh.append(dict(l))
    return result, lh
def laylichbanbacsi():
    doctor_id = request.args.get('doctor_id')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Lấy tất cả lịch hẹn sắp tới của bác sĩ
    cursor.execute("""
            SELECT thoigianbatdau, thoigianketthuc 
            FROM lichhen 
            WHERE bacsi_id = ? AND thoigianbatdau >= datetime('now')
        """, (doctor_id,))
    busy_times = cursor.fetchall()

    # Chuyển về dạng list dễ xử lý ở JS
    result = [{"start": row[0], "end": row[1]} for row in busy_times]
    conn.close()
    return result
def insertlichhen(data):
    conn = get_db()
    cursor = conn.cursor()

    # Bắt đầu transaction
    conn.execute("BEGIN")

    # 1. Thêm bệnh nhân mới
    cursor.execute("""
                INSERT INTO benhnhan (tenBN, gioi_tinh, bacsi_id, lan_kham_cuoi, ghi_chu, sdt, email, ngaysinh)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
        data['hoten'],
        data['gender'],
        data['doctor'],
        data['select-date'],
        data['ghichu'],
        data['sdt'],
        data['mail'],
        data['ngaysinh']
    ))

    benhnhan_id = cursor.lastrowid

    # 2. Tạo lịch hẹn
    cursor.execute("""
                INSERT INTO lichhen (bacsi_id, benhnhan_id, dichvu_id, thoigianbatdau, thoigianketthuc)
                VALUES (?, ?, ?, ?, datetime(?, '+1 hour'))
            """, (
        data['doctor'],
        benhnhan_id,
        data['dichvu_id'],
        data['select-date'],
        data['select-date']
    ))

    conn.commit()
    cursor.close()
    conn.close()

a,b = get_one_bac_si_detail(1)
print(a)
print(b)