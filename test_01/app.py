from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, emit
from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
users = [
    User(id=1, username='user1', password='password'),
    User(id=2, username='user2', password='password2')
]

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((user for user in users.username == username and user.password == password), None)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

chats = []

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('create_chat')
def create_chat(data):
    chat_name = data.get('chat_name')
    chat_id = len(chats) + 1
    new_chat = {
        'id': chat_id,
        'name': chat_name,
        'message': []
    }
    chats.append(new_chat)
    emit('chat_created', new_chat, broadcast=True)


@socketio.on('send_message')
def send_message(data):
    chat_id = data.get('chat_id')
    message = {
        'sender': data.get('sender'),
        'text': data.get('text'),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    for chat in chats:
        if chat['id'] == chat_id:
            chat['message'].append(message)
            emit('message_received', message, room=chat_id, broadcast=True)
            break


if __name__ == '__main__':
    socketio.run(app)
