import os

#Package imports
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#File imports
from security import authenticate, identity
from Resources.user import UserRegister
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ('DB_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'wan'
api = Api(app)



jwt = JWT(app, authenticate, identity) #/Auth



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
  app.run(port=5000, debug=True)