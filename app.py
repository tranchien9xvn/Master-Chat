from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Cấu hình Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tranchien9xvn@gmail.com'
app.config['MAIL_PASSWORD'] = 'mjsr wlij awio jctg'  # Sử dụng mật khẩu ứng dụng
mail = Mail(app)

# Cấu hình cơ sở dữ liệu SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)

# Mô hình dữ liệu
class MessageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    #is_read = db.Column(db.Boolean, default=False) 

# Trang chủ hiển thị chat
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sender = request.form['sender']
        receiver = request.form['receiver']
        content = request.form['content']

        # Lưu tin nhắn vào cơ sở dữ liệu
        new_message = MessageModel(sender=sender, receiver=receiver, content=content)
        db.session.add(new_message)
        db.session.commit()

        # Gửi email thông báo
        msg = Message("New Chat Message", sender="tranchien.rostek@gmail.com", recipients=[receiver])
        msg.body = f"You have a new message from {sender}:\n\n{content}"
        mail.send(msg)

        return redirect(url_for('index'))

    # Lấy tất cả tin nhắn
    messages = MessageModel.query.order_by(MessageModel.timestamp).all()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    #db.drop_all()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

