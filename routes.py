from flask import Blueprint,render_template,request,redirect,url_for,session
from controllers import sqlinsert,sqllogin,hienthidichvu,get_dichvu_detail,get_all_bacsi_detail,get_db
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
@main_bp.route('/get_price/<int:dichvu_id>')
def get_price(dichvu_id):
    db = get_db()
    result = db.execute("SELECT gia FROM dichvu WHERE dichvu_id = ?", (dichvu_id,)).fetchone()
    if result:
        return {"gia": result['gia']}
    else:
        return {"gia": 0}
@main_bp.route('/datlich')
def datlich():
    db = get_db()
    dichvu_list = db.execute("SELECT dichvu_id, tendichvu FROM dichvu").fetchall()
    return render_template('datlich.html', dichvu_list=dichvu_list)
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
