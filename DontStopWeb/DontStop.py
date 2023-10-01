from flask import Flask, render_template
from flask import request
from flask import session
from flask import url_for
import pymysql
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
# from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=11245, user='RentalStart', passwd='vip0818!', db='RentalStart', charset='utf8')
visitor_ips = []
secret_key = os.urandom(24)


@app.route('/', methods= ['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        if form.username.data == 'admin' and form.password.data == 'admin':
            flash('Login successful!', 'success')
            return render_template('index.html')
        else:
            return redirect(url_for('RentalStart_Login.html'))

    return render_template('RentalStart_Login.html', form=form)

@app.route('/visitor', methods= ['POST','GET'])
def visitor():
    visitor_ip = request.remote_addr
    visitor_ips.append(visitor_ip)
    return render_template('visitor.html', visitor_ips=visitor_ips)

@app.route('/inquire', methods=['GET'])
def inquire():
    return render_template('inquire.html')

@app.route('/inquire_food', methods=['GET'])
def inquire_food():
    return render_template('inquire_food.html')

@app.route('/inquire_cafe', methods=['GET'])
def inquire_cafe():
    return render_template('inquire_cafe.html')

@app.route('/notice', methods=['GET'])
def notice():
    return render_template('notice.html')


@app.route('/inquire_process', methods=['post'])
def inquire_process():
    if request.method == 'POST':
        item = request.form.getlist('checkOptions')
        name = request.form['name']
        business = request.form['radioOptions']
        duty = request.form['list']
        email = request.form['email']
        phone = request.form['phone']
        comment = request.form['comment']

        cursor = db.cursor()
        query = "INSERT INTO Simple_Counseling(name, phone, duty, email, comment, item, business) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,phone,duty,email,comment,item,business))

        db.commit()
        cursor.close()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['comments']

        cursor = db.cursor()
        query = "INSERT INTO Counseling(name, email, comment) VALUES (%s, %s,%s)"
        cursor.execute(query,(name,email,message))

        db.commit()
        cursor.close()
        return render_template('index.html')
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.secret_key = secret_key  # Replace 'secret_key' with your generated secret key
    app.run(host='0.0.0.0', port=8888, debug=True)
