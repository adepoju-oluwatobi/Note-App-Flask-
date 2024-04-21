from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from models import db
from flask_login import LoginManager

# Routes
from models.user import User
from routes.index import index
from routes.auth import auth
from routes.add_note import addNote

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.user_login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# Load environment variables from .env file
load_dotenv()

secret_key = os.getenv("SECRET_KEY")

# Set the secret key
app.config['SECRET_KEY'] = secret_key

# Access the variables using os.getenv()
db_url = os.getenv("DATABASE_URL")

# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

# Suppress SQLAlchemy modification tracking overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

app.register_blueprint(index)
app.register_blueprint(auth)
app.register_blueprint(addNote)

if __name__ == "__main__":
    app.run(debug=True)
