#import library
from flask import Flask, render_template
from routes import main_bp
import pyodbc
import sqlite3
app = Flask(__name__,static_url_path='/static')

# Đăng ký Blueprint
app.register_blueprint(main_bp)
app.secret_key = 'cuongtring25'


#MAIN RUN
if __name__ == '__main__':
    app.run()
