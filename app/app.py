from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions with app
db = SQLAlchemy(app)
jwt = JWTManager(app)
mail = Mail(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Welcome to Hitch Hiking App'

if __name__ == '__main__':
    app.run(debug=True)

