from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String)

class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean)
    role_id = Column(Integer, ForeignKey('roles.id'))

# Database connection
engine = create_engine('sqlite:///theater.db')  # Adjust the database URL as needed

def upgrade():
    # Create tables
    Base.metadata.create_all(bind=engine)

def downgrade():
    # Drop tables
    Base.metadata.drop_all(bind=engine)
    # Drop tables
    Base.metadata.drop_all(bind=engine)

# Database connection
engine = create_engine('sqlite:///theater.db')  # Adjust the database URL as needed
Session = sessionmaker(bind=engine)
session = Session()
