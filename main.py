from flask import *
from database import *
from public import public
from admin import admin
from shop import shop
from customer import customer

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin,url_prifix="/admin")
app.register_blueprint(shop,url_prifix="/shop")
app.register_blueprint(customer,url_prifix="/customer")
app.secret_key="hai"
app.run(debug=True,port="5778")