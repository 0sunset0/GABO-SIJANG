from flask import Flask, render_template, jsonify, request
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/market-list/<area>', methods=['GET'])
def market_list(area):
    return render_template('market-list.html', area=area)

@app.route('/detail/<area>/<market>', methods=['GET', 'POST'])
def detail(area, market):
    return render_template('detail.html', area=area, market=market)

@app.route('/create/<market>', methods=['GET'])
def create(market):
    return render_template('create.html', market=market)

@app.route('/update/<market>', methods=['GET'])
def update(market):
    return render_template('update.html', market=market)

 
if __name__ == '__main__':
    app.run(debug=True)
