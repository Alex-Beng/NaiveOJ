import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or '我裂开了居然让我写OJ'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER =  'smtp.163.com'
    MAIL_PORT =  465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'yfast_send@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'KZXYSNSKSKWUJILA'
    ADMINS = ['yfast_send@163.com']