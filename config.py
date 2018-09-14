#config .py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

'''
class Config(object):
    #Configuring to use variable or base dir
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''

#Enable Flask Debug (Set to false in production)
DEBUG = True
