from flask import Flask, render_template, url_for
from flask import request
import pymysql


app = Flask(__name__)
db = pymysql.connect(host='localhost', port=11245, user='RentalStart', passwd='vip0818!', db='RentalStart', charset='utf8')


@app.route('/', methods= ['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/inquire', methods=['GET'])
def inquire():
    return render_template('inquire.html')

@app.route('/inquire_process', methods=['post'])
def inquire_process():
    if request.method == 'POST':
        item = request.form['checkOptions']
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
    app.run(host='0.0.0.0', port=8888, debug=True)
