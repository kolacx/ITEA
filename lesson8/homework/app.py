from flask import Flask, request
from flask import render_template, redirect
from models import Product, Category

app = Flask(__name__)

@app.route('/')
def home_page():
    cat = Category.objects.all()

    return render_template('index.html', categorys=cat)

@app.route('/category/<string:id_category>')
def category_page(id_category):
    
    cat = Category.objects.get(id=id_category)

    prod = Product.objects.filter(in_sale=True, category=cat)

    return render_template('category.html', products=prod)

@app.route('/product/<string:id_product>')
def product_page(id_product):

    prod = Product.objects.get(id=id_product)

    return render_template('product.html', product=prod)

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/add_category')
def add_category_page():
    return render_template('add_category.html')

@app.route('/add_product')
def add_product_page():

    cat = Category.objects.all()

    return render_template('add_product.html', category=cat)


@app.route('/add_cat', methods=['POST'])
def add_category():

    cat = Category.objects.create(**dict(request.form))

    return render_template('/add_category.html', added_category=cat)


@app.route('/add_prod', methods=['POST'])
def add_product():
    
    cat = Category.objects.all()
    prod = Product.objects.create(**dict(request.form))

    return render_template('/add_product.html', added_product=prod, category=cat)

if __name__ == '__main__':
    app.run(debug=True)