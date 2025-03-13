from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    
    names = ["Mustafa", "Aygün", "Bengü", "Kağan", "Bilge"]
    
    return render_template("index.html", people = names)

@app.route("/products")
def products():
    
    return render_template("products.html")

@app.route("/about")
def about():
    
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
