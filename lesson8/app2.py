from flask import Flask
from flask import render_template

app = Flask(__name__)

dict_to_buy = {
    'milk': 2,
    'fish': 1,
    'meat': 2,
    'orange': 10,
}

@app.route('/product')
def hellow_world():

    my_name = 'Sasha'
    dict_to_buy = {
        'milk': 2,
        'fish': 1,
        'meat': 2,
        'orange': 10,
    }

    list_of_items = ['qwe', 'qwe', 'qwe']

    return render_template('index.html', list_of_items=list_of_items,
                                            to_buy=dict_to_buy)

@app.route('/product/<string:name>')
def get_product_by_name(name):
    return str(dict_to_buy[name])


if __name__ == '__main__':
    app.run(debug=True)