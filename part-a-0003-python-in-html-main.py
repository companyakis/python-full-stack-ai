from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    
    year = 2025
    
    who_i_am = "Mustafa Büyükdereli"
    
    some_data = {"USA": "$", "Europe": "€", "Turkiye": "₺"}
    
    return render_template("index.html", year = year, who_i_am = who_i_am, some_data = some_data)

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
