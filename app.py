#Package imports
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#File imports
from security import authenticate, identity
from Resources.user import UserRegister
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'wan'
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all()

jwt = JWT(app, authenticate, identity) #/Auth



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
  db.init_app(app)
  app.run(port=5000, debug=True)