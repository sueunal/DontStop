from flask import Flask, render_template
from flask import request
from flask import session
from flask import url_for
# import pymysql


app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')
# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='RentalStart', charset='utf8')

@app.route('/', methods= ['POST','GET'])
def index():
    return render_template('index.html')

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
    


@app.route('/register', methods=['GET', 'POST']) # 회원가입->관리자 페이지
def register():
	# if request.method == 'POST':  # POST방식의 요청일 경우 회원정보 생성
    # 	userid = request.form.get('userid') # request.form.get에 요청정보들이 저장되므로 이것을 통해 접근할 수 있다.
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     re_password = request.form.get('re-password')
        
    #     if (userid and username and password and re_password) and password == re_password:
    #     	fcuser = Fcuser()
    #         fcuser.userid = userid
    #         fcuser.username = username
    #         fcuser.password = password # 모든 정보가 있는지와 비밀번호와 비밀번호 확인이 일치하는지 체크
            
    #         db.session.add(fcuser)  # 회원 데이터베이스 추가
    #         db.session.commit()  # 회원 데이터베이스 추가 https://ohdowon064.tistory.com/115
            
    #         return redirect('/')
            
    return render_template('register.html')
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
