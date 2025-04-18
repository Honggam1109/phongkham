from flask import Blueprint,render_template,request,redirect,url_for
from controllers import sqlinsert
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
    return render_template('bacsi.html')
@main_bp.route('/blog')
def blog():
    return render_template('blog.html')
@main_bp.route('/datlich')
def datlich():
    return render_template('datlich.html')
@main_bp.route('/dichvu')
def dichvu():
    return render_template('dichvu.html')
@main_bp.route('/vechungtoi')
def vechungtoi():
    return render_template('vechungtoi.html')
@main_bp.route('/lamsachrang')
def lamsachrang():
    return render_template('lamsachrang.html')
#routes cua bac si
# @main_bp.route('/')
# def home():
#     return render_template('home.html')
@main_bp.route('/benhnhan')
def benhnhan():
    return render_template('benhnhan.html')