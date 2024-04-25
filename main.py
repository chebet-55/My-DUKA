from flask import Flask,render_template

# flask instance
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/home')
def home():
    return "hello brian"

# create for products

@app.route('/sales')
def sales():
    return render_template("sales.html")


@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


app.run(debug=True)
