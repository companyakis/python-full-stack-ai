from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    
    sales = 5000
    
    cost = 4000
    
    return render_template("index.html", total_sales = sales, total_cost = cost)

@app.route("/products")
def products():
    
    return render_template("products.html")

@app.route("/about")
def about():
    
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
