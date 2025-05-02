import sqlite3
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
data = get_dichvu_detail(3)
print(data)
for row in data["loi_ich"]:
    print(row)
