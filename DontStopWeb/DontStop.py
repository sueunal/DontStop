from flask import Flask, render_template, url_for
from flask import request
import pymysql


app = Flask(__name__)
# """
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'DontStop'
# app.config['MYSQL_PASSWORD'] = 'vip0818!'
# app.config['MYSQL_DB'] = 'DontStop'

# mysql = pymysql.connect(
#     host=app.config['MYSQL_HOST'],
#     user=app.config['MYSQL_USER'],
#     password=app.config['MYSQL_PASSWORD'],
#     db=app.config['MYSQL_DB']
# )
# ""

# db 접속시 필요한 설정 없으면 디비 연결 X, 은지 개인PC에서 실행시 주석 처리 해주고 실행해야함
# 실행방법 python3 DonStop.py cmd 에서 명령어 쳐야함 또는 오른쪽 위 실행 아이콘 클릭
db = pymysql.connect(host='localhost', port=11245, user='RentalStart', passwd='vip0818!', db='RentalStart', charset='utf8')


@app.route('/', methods= ['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/inquire', methods=['GET'])
def inquire():
    return render_template('inquire.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['comments']

        cursor = db.cursor()
        # no, date time 사용자가 입력시 db 에 자동으로 날짜 삽입
        query = "INSERT INTO Counseling(name, email, comment) VALUES (%s, %s,%s)"
        cursor.execute(query,(name,email,message))
        db.commit()
#        cursor.execute("SELECT * FROM Messages")
#        data = cursor.fetchall()

        cursor.close()
        return render_template('index.html')
    else:
        return render_template('index.html')
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
