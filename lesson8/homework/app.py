from flask import Flask, request
from flask import render_template, redirect
import sqlite3

app = Flask(__name__)

class Connection_db():

    def __enter__(self):
        self._conn = sqlite3.connect('shop.db')
        cursore = self._conn.cursor()
        return cursore

    def __exit__(self, *args):
        self._conn.commit()
        self._conn.close()

@app.route('/')
def home_page():

    with Connection_db() as db:
        q = db.execute("SELECT * FROM categorys")
        category = dict(q.fetchall())
        print(category)
    return render_template('index.html', cat=category)

@app.route('/category/<int:id_category>')
def category_page(id_category):
    
    with Connection_db() as db:
        q = db.execute("SELECT * FROM products WHERE category=id_category") # осмотреть как поле 
        products = dict(q.fetchall())
        print(products)

    return render_template('category.html')



if __name__ == '__main__':
    app.run(debug=True)