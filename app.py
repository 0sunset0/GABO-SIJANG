from flask import Flask, redirect, render_template, request, request_finished
from flask_sqlalchemy import SQLAlchemy
from controller import Controller
from models import db
from models import Area, Market, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///models.db'
controller = Controller()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/market-list', methods=['GET'])
def market_list():
    area_id = request.args.get('area_id')
    area = controller.find_area(area_id)
    markets_order_by_city = controller.order_by_city(area_id)
    markets_order_by_score = controller.order_by_score(area_id)
    return render_template('market-list.html',area=area,markets_order_by_city=markets_order_by_city,
                           markets_order_by_score=markets_order_by_score)

@app.route('/detail', methods=['GET'])
def detail():
    market_id = request.args.get('market_id')
    market = controller.find_market(market_id)
    reviews = controller.find_reviews(market_id)
    return render_template('detail.html', market=market, reviews=reviews)


@app.route('/create', methods=['GET', 'POST'])
def create():
    market_id = request.args.get('market_id')
    market = controller.find_market(market_id)
    reviews = controller.find_reviews(market_id)
    if request.method =='POST':
        title = request.form['title']
        content = request.form['content']
        score = int(request.form.get('score'))
        password = int(request.form.get('password'))
        new_review = Review(title=title, content=content, score=score, password=password,  market_id=market_id)
        try:
            controller.create_review(new_review, market, reviews)
            return redirect('/')
        except:
            return'There was an issue adding your task'
    else:
        return render_template('create.html', market=market)


@app.route('/update', methods=['GET', 'POST'])
def update():
    review_id = request.args.get('review_id')
    review = controller.find_reivew(review_id)
    market = controller.find_market(review.market_id)
    reviews = controller.find_reviews(review.market_id)
    if request.method =='POST':
        password = int(request.form.get('password'))
        if password == review.password:
            review.title = request.form['title']
            review.content = request.form['content']
            review.score = int(request.form.get('score'))
            try:
                controller.update_review(market, reviews)
                return redirect('/') 
            except:
                return '수정할 수 없습니다'
        else:
            return '잘못된 비밀번호입니다'
    else:
        return render_template('update.html', review=review)
    
@app.route('/delete')
def delete():
    review_id = request.args.get('review_id')
    review = controller.find_reivew(review_id)
    try:
        controller.delete_review(review)
        return redirect('/')
    except:
        return '삭제할 수 없습니다'

 
if __name__ == '__main__':
    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(debug=True)
