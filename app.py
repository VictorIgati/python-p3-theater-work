from flask import Flask
from flask_migrate import Migrate
from lib.models import Base  # Import the Base from models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///theater.db"  # Example database URL
engine = create_engine(DATABASE_URL)  # Create the engine
migrate = Migrate(app, engine)  # Initialize Flask-Migrate
Base.metadata.create_all(engine)  # Create tables

@app.route('/')
def index():
    return "Welcome to the Theater API!"

if __name__ == '__main__':
    app.run(debug=True)
