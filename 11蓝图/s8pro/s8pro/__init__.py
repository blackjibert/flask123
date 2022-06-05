from flask import Flask

from .views import account
from .views import admin
from .views import user


apprun = Flask(__name__)


apprun.register_blueprint(account.ac)
apprun.register_blueprint(admin.ad)
apprun.register_blueprint(user.us)
