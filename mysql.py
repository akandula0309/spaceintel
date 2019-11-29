from flask import Flask, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "floor_object_detection_db"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_admin_details(self):
        username = 'admin'
        password = 'e10adc3949ba59abbe56e057f20f883e'
        self.cur.execute("SELECT * FROM admin_details WHERE username = '"+username+"' and password = '"+password+"' LIMIT 1")
        result = self.cur.fetchall()

        return result

@app.route('/')
def admin_details():

    def db_query():
        db = Database()
        emps = db.list_admin_details()

        return emps

    res = db_query()

    return render_template('admin_details.html', result=res, content_type='application/json')