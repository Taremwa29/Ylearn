import sqlite3, datetime
from flask import *

# load models/verify.py
from resources.modules.ylearnmodules import *

app = Flask(__name__)
app.secret_key = "edutechhasasecretS"

con = sqlite3.connect('resources/databank/users/db.db3',
                      check_same_thread=False)
con.row_factory = dict_factory
cur = con.cursor()

# 1st Merge

app.route('/')
def index():
    return render_template("index.html")

@app.route('/a/<path>')
def subpath(path):
    return subPathsOfA(path)

@app.route('/<username>')
def profile(username):
    return f'{username}\'s profile'


'''@app.route("/")
def index():
    print(session)
    return render_template('ylearn2/index.html')'''


@app.route("/signupstudent")
def signupstudent():
    return render_template("ylearn2/signupstudent.html")


@app.route("/pay")
def pay():
    return render_template("payment.html")


@app.route('/verify')
def verify():
    return verify_trans(con, cur, request.args.get('transaction_id'))


@app.route("/signup", methods=["POST"])
def signup():
    # Get thew user submitted form data
    username = request.form.get("username")
    fullname = request.form.get("yrname")
    email = request.form.get("email")
    passkey = request.form.get("psw")

    classid = request.form.get("class")
    dob = request.form.get("DOB")
    gender = request.form.get("gender")
    parentid = request.form.get("parentid")

    # store data in database
    #cur.execute(f'INSERT INTO parents ("Username", "Name", "Email", "Children", "Pass") VALUES ("{username}","{fullname}", "{email}", "[]", "{passkey}");')

    cur.execute(f'INSERT INTO children ("Username", "Name", "Class", "DOB", "Gender", "Parent") VALUES'
                f' ("{username}","{fullname}", "{classid}", "DOB", "{gender}", "{parentid}");')

    print(con.commit())
    return "success"

#cur.execute(''' ''')

app.route('/login', methods=['GET', 'POST'])
def login(username, passkey):
    account_type = request.args.get('as'); username = request.form.get("username"); passkey  =  request.form.get("password")
    login_(account_type=account_type, username=username, passkey=passkey);

# flask debug mode
if __name__ == "__main__":
    app.run(debug=True)


