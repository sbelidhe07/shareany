from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'shareany'
app.config[
    'MONGO_URI'] = 'mongodb+srv://portalappuser:admin123@cluster0.89wan.mongodb.net/shareany?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true'

mongo = PyMongo(app)



@app.route('/index')
def index():
    if 'username' in session:
        if session['role'] == 'Admin':
            return redirect(url_for('dashboarda'));
        else:
            return redirect(url_for('dashboardo'));

    return render_template('index.html')


@app.route('/dashboarda')
def dashboarda():
    if 'username' in session:
        if session['role'] == 'Admin':
           return render_template('dashboard_admin.html');
        return render_template('index.html')

@app.route('/tracking')
def tracking():
    if 'username' in session:
        return render_template('tracking.html');
    return render_template('index.html')

@app.route('/request')
def request():
    if 'username' in session:
        return render_template('request.html');
    return render_template('index.html')

@app.route('/logout')
def logout():
    session['username'] = ''
    return render_template('index.html')

@app.route('/dashboardo')
def dashboardo():
    if 'username' in session:
        return render_template('dashboard_other.html');
    return render_template('index.html')

@app.route('/menubara')
def menubara():
    if 'username' in session:
        return render_template('menubar_admin.html');
    return render_template('index.html')

@app.route('/logisticsa')
def logisticsa():
    if 'username' in session:
        return render_template('logistics_add.html');
    return render_template('index.html')

@app.route('/categorya')
def categorya():
    if 'username' in session:
        return render_template('category_add.html');
    return render_template('index.html')

@app.route('/gifta')
def gifta():
    if 'username' in session:
        return render_template('gift_add.html');
    return render_template('index.html')

@app.route('/clienta')
def clienta():
    if 'username' in session:
        return render_template('client_add.html');
    return render_template('index.html')

@app.route('/menubar')
def menubar():
    if 'username' in session:
        return render_template('menubar.html');
    return render_template('index.html')

@app.route('/support')
def support():
    if 'username' in session:
        return render_template('support.html');
    return render_template('index.html')

@app.route('/notifications')
def notifications():
    if 'username' in session:
        return render_template('notifications.html');
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    print(request.form['role']);
    login_user = users.find_one({'username': request.form['username'], 'role': request.form['role']})
    if login_user:
           hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
           if bcrypt.checkpw(request.form['pass'].encode('utf-8'),hashpass): 
             session['username'] = request.form['username']
             session['role'] = request.form['role']
             return redirect(url_for('index'))
    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username'], 'role': request.form['role']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password': hashpass, 'role': request.form['role']})
            session['username'] = request.form['username']
            session['role'] = request.form['role']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
