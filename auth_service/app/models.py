from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    ### hasher et stocker le mp
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # verifier le mp
    def check_password(self, password):
        return check_password_hash(self.password, password)
