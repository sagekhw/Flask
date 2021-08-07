from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import *
from flask_jwt_extended import JWTManager

from .controller.AuthController import *
from .controller.UserController import *
from .controller.FileController import *
from .controller.PublicDataController import *
from .controller.PushController import *
from app.config.AppConfig import *
import datetime

app = Flask(__name__)

CORS(app, resources={r'*': {'origins': '*'}})

#### JWT ####
# JWT 매니저 활성화

app.config["JWT_SECRET_KEY"] = FlaskConfig.JWT_SECRET_KEY
app.config['JWT_ALGORITHM'] = FlaskConfig.JWT_ALGORITHM
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=FlaskConfig.JWT_ACCESS_TOKEN_EXPIRES)
jwt = JWTManager(app)
"""
# jwt = JWTManager()
# jwt.init_app(app)
"""

app.register_blueprint(auth_API)
app.register_blueprint(user_API)
app.register_blueprint(file_API)
app.register_blueprint(publicData_API)
app.register_blueprint(push_API)

