from flask import Flask, render_template, jsonify, request
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market-list/<area>')
def market_list(area):
    return render_template('market-list.html', area=area)

@app.route('/detail/<market>', methods=['GET'])
def detail(market):
    return render_template('detail.html', market=market)

@app.route('/create/<market>')
def create(market):
    return render_template('create.html', market=market)

@app.route('/update/<market>')
def update(market):
    return render_template('update.html', market=market)

 
if __name__ == '__main__':
    app.run(debug=True)
