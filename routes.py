from flask import Blueprint,render_template,request,redirect,url_for,session,jsonify
from controllers import sqlinsert,sqllogin,hienthidichvu,get_dichvu_detail,get_all_bacsi_detail,get_db,laylichbanbacsi
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
@main_bp.route('/datlich')
def datlich():
    db = get_db()
    dichvu_list = db.execute("SELECT dichvu_id, tendichvu FROM dichvu").fetchall()
    bacsi_list = db.execute("SELECT * FROM bacsi").fetchall()
    return render_template('datlich.html', dichvu_list=dichvu_list,bacsi_list = bacsi_list)
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
@main_bp.route('/bacsipage')
def home():
    return render_template('home.html')
@main_bp.route('/benhnhan')
def benhnhan():
    return render_template('benhnhan.html')
@main_bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        bacsiid = sqllogin(username,password)
        if bacsiid:
            session['username'] = username
            session['bacsiid'] = bacsiid
            print(session['bacsiid'])
            print(session['username'])
            return redirect(url_for('main.home'))
    return render_template('login.html')
