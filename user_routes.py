from flask import Blueprint,render_template

main_bp = Blueprint('main', __name__)

# routes cua benh nhan
# @main_bp.route('/')
# def homepage():
#     return render_template('homepage.html')
# @main_bp.route('/bacsi')
# def bacsi():
#     return render_template('bacsi.html')
# @main_bp.route('/blog')
# def blog():
#     return render_template('blog.html')
# @main_bp.route('/datlich')
# def datlich():
#     return render_template('datlich.html')
# @main_bp.route('/dichvu')
# def dichvu():
#     return render_template('dichvu.html')
# @main_bp.route('/vechungtoi')
# def vechungtoi():
#     return render_template('vechungtoi.html')
# @main_bp.route('/lamsachrang')
# def lamsachrang():
#     return render_template('lamsachrang.html')
#routes cua bac si
@main_bp.route('/')
def login():
    return render_template('login.html')
@main_bp.route('/')
def home():
    return render_template('home.html')
@main_bp.route('/benhnhan')
def benhnhan():
    return render_template('benhnhan.html')