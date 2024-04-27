from flask import Flask, render_template
from app import routes
from app import app
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ivan'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True) 