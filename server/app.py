from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db  # Import the db object
#from routes import api
from config import SQLALCHEMY_DATABASE_URI  # Import the database URI
app = Flask(__name__)

# Configure the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension with the Flask app
db.init_app(app)

# Register the blueprint
#app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
