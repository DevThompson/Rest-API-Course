import os

#Package imports
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
#File imports
from Resources.user import UserRegister, User, UserLogin
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'wan'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWTManager(app)



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
  app.run(port=5000, debug=True)