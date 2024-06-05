from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.init_app(app)

    with app.app_context():
        db.create_all()
    


class Pet(db.Model):
    """Pet adoption model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False)
    
    species = db.Column(db.Text,
                     nullable=False)
    
    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, 
                          nullable=False,
                          default=True)