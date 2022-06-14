from models import db
from models import Area, Market, Review

class Controller:
            
    def create_review(self, new_review, market, reviews):
        db.session.add(new_review)
        self.cal_score(market, reviews)
        
        
        
    def cal_score(self, market, reviews):
        sum = count = 0
        for review in reviews:
            sum = sum + int(review.score)
            count += 1
        if count!=0:
            market.score = sum/count
            db.session.commit()
            
            
            
    def update_review(self, market, reviews):
        self.cal_score(market, reviews)
            
    def delete_review(self, review):
        db.session.delete(review)
        db.session.commit()
        
        
        
    def find_area(self, area_id):
        return Area.query.get(area_id)
    
    def find_market(self, market_id):
        return Market.query.get(market_id)
    
    def find_reivew(self, review_id):
        return Review.query.get_or_404(review_id)
    
    def find_reviews(self, market_id):
        return Review.query.filter_by(market_id=market_id).all()
    
    def order_by_city(self, area_id):
        return Market.query.filter_by(area_id=area_id).order_by(Market.address)
    
    def order_by_score(self, area_id):
        return Market.query.filter_by(area_id=area_id).order_by(Market.score.desc())
    
    
        
    