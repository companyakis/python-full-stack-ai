from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    
    ages = [17, 21, 32, 87, 91, 96, 12]
        
    return render_template("index.html", ages = ages)

@app.route("/products")
def products():
    
    return render_template("products.html")

@app.route("/about")
def about():
    
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
