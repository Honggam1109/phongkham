from flask import Flask, render_template
from user_routes import main_bp
app = Flask(__name__, static_url_path='/static')
app.register_blueprint(main_bp)  # Đảm bảo biến main_bp đã được import
if __name__ == '__main__':
    app.run()