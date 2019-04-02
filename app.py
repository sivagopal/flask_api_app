from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'manager',
    'db': 'csoc',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db=SQLAlchemy(app)
db.init_app(app)
@app.route('/')
def index():
	return 'Hello, Flask';
if __name__ == '__main__':

    app.run(debug=True)
