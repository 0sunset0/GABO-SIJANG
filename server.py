from flask import Flask, render_template, jsonify, request
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market-list')
def market_list():
    return render_template('market-list.html')

@app.route('/detail/<market_id>', methods=['GET'])
def detail(market_id):
    return render_template('detail.html', market_id=market_id)

@app.route('/detail/<market_id>/create')
def create(market_id):
    return render_template('create.html', market_id=market_id)

@app.route('/detail/<market_id>/update')
def update(market_id):
    return render_template('update.html', market_id=market_id)

@app.route('/detail/<market_id>/delete')
def delete(market_id):
    return render_template('detail.html', market_id=market_id)
 
if __name__ == '__main__':
    app.run(debug=True)
