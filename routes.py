from flask import Blueprint,render_template,request,redirect,url_for,session,jsonify
from controllers import sqlinsert,sqllogin,hienthidichvu,get_dichvu_detail,get_all_bacsi_detail,get_db,get_one_bac_si_detail,insertlichhen
from datetime import datetime
main_bp = Blueprint('main', __name__)

# routes cua benh nhan
@main_bp.route('/')
def homepage():
    return render_template('homepage.html')
@main_bp.route('/tuvan',methods=['POST'])
def tuvan():
    hovaten = request.form['hoten']
    email = request.form['email']
    sdt = request.form['sdt']
    dichvu = request.form['dichvu']
    ngayhen = request.form['ngayhen']
    print(f"{hovaten} {email} {sdt} {dichvu} {ngayhen}")
    sqlinsert("""
    INSERT INTO formtuvan (hovaten, sdt, email, dichvu, ngayhen, ngaytao)
    VALUES (?, ?, ?, ?, ?, datetime('now'));
    """,(hovaten,sdt,email,dichvu,ngayhen,))
    return redirect(url_for('main.homepage'))  # Đã sửa thành 'main.homepage'
@main_bp.route('/bacsi')
def bacsi():
    bacsidata = get_all_bacsi_detail()
    return render_template('bacsi.html', bacsis = bacsidata)
@main_bp.route('/blog')
def blog():
    return render_template('blog.html')
@main_bp.route('/datlich')
def datlich():
    db = get_db()
    dichvu_list = db.execute("SELECT dichvu_id, tendichvu FROM dichvu").fetchall()
    bacsi_list = db.execute("SELECT * FROM bacsi").fetchall()
    return render_template('datlich.html', dichvu_list=dichvu_list,bacsi_list = bacsi_list)
@main_bp.route('/datlichmoi',methods =['POST'])
def postdatlich():
    if request.method == 'POST':
        data = request.form.to_dict()
        insertlichhen(data)
        return redirect(url_for('main.homepage'))

@main_bp.route('/dichvu')
def dichvu():
    dichvus = hienthidichvu()
    for dv in dichvus:
        print(dv["tendichvu"], dv["hinh_anh"])
    return render_template('dichvu.html',dichvus = dichvus)
@main_bp.route('/vechungtoi')
def vechungtoi():
    return render_template('vechungtoi.html')
@main_bp.route('/lamsachrang/<int:id>')
def lamsachrang(id):
    data = get_dichvu_detail(id)
    return render_template('lamsachrang.html',result=data)
#routes cua bac si
@main_bp.route('/bacsipage/<int:bacsi_id>')
def home(bacsi_id):
    bacsi_data, lichhen_data = get_one_bac_si_detail(bacsi_id)
    return render_template('home.html',bacsi_data = bacsi_data,lichhen_data=lichhen_data)
@main_bp.route('/benhnhan/<int:bacsiid>')
def benhnhan(bacsiid):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT benhnhan_id,tenBN,gioi_tinh,sdt,insurance,lan_kham_cuoi   FROM benhnhan where bacsi_id = ?", (bacsiid,))
    rows = cursor.fetchall()
    conn.close()
    return render_template('benhnhan.html',data_benhnhan = rows)
@main_bp.route("/patientEdit", methods=["POST"])
def patient_edit():
    form = request.form
    patient_id = form.get("patientId")

    data = {
        "tenBN": form.get("formName"),
        "ngaysinh": form.get("formDob"),
        "gioi_tinh": form.get("formGender"),
        "blood_type": form.get("formBloodType"),
        "id_number": form.get("formIdNumber"),
        "sdt": form.get("formPhone"),
        "email": form.get("formEmail"),
        "address": form.get("formAddress"),
        "occupation": form.get("formOccupation"),
        "insurance": form.get("formInsurance"),
        "emergency_contact": f'{form.get("formEmergencyContact")} - {form.get("formEmergencyPhone")}',
        "medical_history": form.get("formMedicalHistory"),
        "allergies": form.get("formAllergies"),
        "current_meds": form.get("formCurrentMeds"),
        "special_notes": form.get("formSpecialNotes"),
        "gum_status": form.get("formGumStatus"),
        "cavities": form.get("formCavities"),
        "wisdom_teeth": form.get("formWisdomTeeth"),
        "current_treatment": form.get("formCurrentTreatment"),
        "photo": form.get("photo", "https://via.placeholder.com/200"),  # optional
        "bacsi_id": session.get('bacsiid')  # hoặc lấy từ session / context
    }

    conn = get_db()
    cursor = conn.cursor()

    if patient_id:  # Cập nhật
        set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
        query = f"""
            UPDATE benhnhan SET {set_clause}
            WHERE benhnhan_id = ?
        """
        cursor.execute(query, list(data.values()) + [patient_id])
    else:  # Thêm mới
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        query = f"""
            INSERT INTO benhnhan ({columns})
            VALUES ({placeholders})
        """
        cursor.execute(query, list(data.values()))

    conn.commit()
    conn.close()

    return redirect(f"/benhnhan/{session.get('bacsiid')}")  # hoặc return jsonify({"success": True})
@main_bp.route('/deletePatient',methods=["POST"])
def delete_patient():
    form = request.form
    patient_id = form.get("patientId")
    conn = get_db()
    cursor = conn.cursor()
    result = cursor.execute('DELETE FROM lichhen where benhnhan_id = ?',(patient_id,))
    tes = cursor.execute('DELETE FROM benhnhan where benhnhan_id = ?',(patient_id,))
    conn.commit()
    conn.close()
    return redirect(f'benhnhan/{session.get('bacsiid')}')

@main_bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        bacsiid = sqllogin(username,password)
        if bacsiid:
            session['username'] = username
            session['bacsiid'] = bacsiid
            return redirect(f'/bacsipage/{bacsiid}')
    return render_template('login.html')
@main_bp.route('/logout')
def logout():
    session.pop('username')
    session.pop('bacsiid')
    return redirect(url_for('main.login'))

@main_bp.route('/test')
def test():
    return  render_template('cccc.html')
#api
@main_bp.route('/api/get_price')
def get_price():
    dichvu_id = request.args.get('dichvu_id')
    db = get_db()
    result = db.execute("SELECT gia FROM dichvu WHERE dichvu_id = ?", (dichvu_id,)).fetchone()
    if result:
        return {"gia": result['gia']}
    else:
        return {"gia": 0}
# @main_bp.route('/api/get-busy-times')
# def get_busy_times():
#     result = laylichbanbacsi()
#     return jsonify(result)
@main_bp.route("/api/unavailable-times")
def get_unavailable_times():
    doctor_id = request.args.get("doctor_id")
    date_str = request.args.get("date")  # YYYY-MM-DD

    if not doctor_id or not date_str:
        return jsonify({"error": "Missing parameters"}), 400

    conn = get_db()
    cursor = conn.cursor()
    # Lấy tất cả giờ bắt đầu trong ngày đó với bác sĩ
    query = """
        SELECT thoigianbatdau FROM lichhen
        WHERE bacsi_id = ? AND date(thoigianbatdau) = ?
    """
    cursor.execute(query, (doctor_id, date_str))
    rows = cursor.fetchall()

    conn.close()

    # Trả về danh sách giờ đã bận dưới dạng ["09:00", "10:00"]
    unavailable_times = []
    for row in rows:
        time_str = row["thoigianbatdau"]
        try:
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        unavailable_times.append(dt.strftime("%H:%M"))

    return jsonify(unavailable_times)
@main_bp.route("/api/patients")
def get_patients():
    bacsi_id = request.args.get('bacsi_id')
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM benhnhan where bacsi_id = ?",(bacsi_id,))
    rows = cursor.fetchall()
    conn.close()

    patients = {}
    for row in rows:
        patient_id = row['benhnhan_id']  # Tạo ID như BN001
        row_dict = dict(row)
        patients[patient_id] = {
            "name": row_dict["tenBN"],
            "dob": row_dict["ngaysinh"],
            "gender": row_dict["gioi_tinh"],
            "bloodType": row_dict.get("blood_type", ""),
            "idNumber": row_dict.get("id_number", ""),
            "insurance": row_dict.get("insurance", ""),
            "phone": row_dict["sdt"],
            "email": row_dict["email"],
            "address": row_dict.get("address", ""),
            "occupation": row_dict.get("occupation", ""),
            "emergencyContact": row_dict.get("emergency_contact", ""),
            "medicalHistory": row_dict.get("medical_history", ""),
            "allergies": row_dict.get("allergies", ""),
            "currentMeds": row_dict.get("current_meds", ""),
            "specialNotes": row_dict.get("special_notes", ""),
            "gumStatus": row_dict.get("gum_status", ""),
            "cavities": row_dict.get("cavities", ""),
            "wisdomTeeth": row_dict.get("wisdom_teeth", ""),
            "currentTreatment": row_dict.get("current_treatment", ""),
            "photo": row_dict.get("photo", "https://via.placeholder.com/200")
        }

    return jsonify(patients)