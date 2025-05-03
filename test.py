import sqlite3
def get_dichvu_detail(dichvu_id):
    conn = sqlite3.connect('./db/QLPK.db')
    conn.row_factory = sqlite3.Row

    # 1. Lấy thông tin bacsi
    bacsi = conn.execute("SELECT * FROM bacsi WHERE bacsi_id = ?", (dichvu_id,)).fetchone()

    # 2. Lấy tag
    tag = conn.execute("SELECT mo_ta FROM bacsi_tag WHERE bacsi_id = ?", (dichvu_id,)).fetchall()

    # 3. Lấy thanh tuu
    thanhtuu = conn.execute("SELECT mo_ta FROM thanhtuu_bacsi WHERE bacsi_id = ? ", (dichvu_id,)).fetchall()

    return {
        "bacsi": dict(bacsi),
        "tag": [row["mo_ta"] for row in tag],
        "thanhtuu": [row["mo_ta"] for row in thanhtuu]
    }
data = get_dichvu_detail(3)
print(data)

