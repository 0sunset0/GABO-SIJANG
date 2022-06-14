from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()  

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    markets = db.relationship("Market", backref="area", lazy=True)
    
    def __init__(self, name, **kwargs):
        self.name = name
    
    def __repr__(self):
        return f"Area('{self.id}', '{self.name}', '{self.markets}')"
    
    
class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    address = db.Column(db.String(128))
    map_link = db.Column(db.String(128)) 
    score =  db.Column(db.Integer)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    reviews = db.relationship("Review", backref="market")
    
    def __init__(self, name, address, map_link, area_id, **kwargs):
        self.name = name
        self.address = address
        self.map_link = map_link
        self.area_id = area_id
        
    def __repr__(self):
        return f"Market('{self.id}', '{self.name}', '{self.address}', '{self.map_link}', '{self.reviews}')"
    
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    content = db.Column(db.String(128))  
    score =  db.Column(db.Integer)
    password =  db.Column(db.Integer)
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'))

    def __init__(self, title, content, score, password, market_id, **kwargs):
        self.title = title
        self.content = content
        self.score = score
        self.market_id = market_id
        self.password = password
        
    def __repr__(self):
        return f"Review('{self.id}', '{self.title}', '{self.content}', '{self.score}', '{self.password}')"