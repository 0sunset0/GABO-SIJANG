from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    markets = db.relationship("market", backref="area")
    def __repr__(self):
        return f"Area('{self.id}', '{self.name}', '{self.markets}')"
    
    
class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    address = db.Column(db.String(128))
    map_link = db.Column(db.String(128)) 
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False)
    reviews = db.relationship("review", backref="market")
    def __repr__(self):
        return f"Market('{self.id}', '{self.name}', '{self.address}', '{self.map_link}', '{self.reviews}')"
    
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    content = db.Column(db.String(128))   
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=True)
    def __repr__(self):
        return f"Review('{self.id}', '{self.title}', '{self.content}')"
    
db.create_all()