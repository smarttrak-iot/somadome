from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from ma import ma
#from blocklist import BLOCKLIST
from resources.user import UserRegister, UserLogin, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "somadome"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)


#@app.before_first_request
##def create_tables():
#    db.create_all()


jwt = JWTManager(app)




api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
#api.add_resource(TokenRefresh, "/refresh")
#api.add_resource(UserLogout, "/logout")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)