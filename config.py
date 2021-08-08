import os


basedir = os.path.abspath(os.path.dirname(__file__))
class Config():
    FLASK_APP='run'
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SECRET_KEY='07241991'
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
# flask db init 
# flask db migrate
# flask db upgrade
    SQLALCHEMY_TRACK_MODIFICATIONS = False