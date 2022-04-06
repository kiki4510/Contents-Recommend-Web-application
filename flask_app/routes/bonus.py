from flask import Blueprint,render_template,request,g
from sqlite3 import dbapi2 as sqlite3


bp = Blueprint('bonus', __name__, url_prefix='/bonus')
def connect_db():
    return sqlite3.connect('OTT.db')

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = connect_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@bp.route('/',methods=['GET','POST'])
def index():
    return render_template('bonus.html')

@bp.route('/where',methods=['GET','POST'])
def where():
    title = request.form.items("title")
    cur=connect_db()
    data = cur.execute('SELECT Title FROM Netflix WHERE Title == ?',title)
    if data is None:
        return 'Not in Netflix!'
    else:
        return 'You can find it in Nexflix!'