__author__ = 'Ronald Bister'
__email__ = 'mini.pelle@gmail.com'
__license__ = 'CC-BY'
__version__ = '0.1'

from flask import Flask
from clapi import config
#from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(config)

#mongo = PyMongo(app)

from clapi.views import stargate

app.register_blueprint(stargate.appmodule)

if __name__ == '__main__':
    app.run()
