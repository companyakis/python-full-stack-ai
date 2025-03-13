from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    
    salaries = [
        {"name": "Ayhan Bilir", "salary": 45000},
        {"name": "Hakan Az", "salary": 34000},
        {"name": "Bengü Kaya", "salary": 28000},
        {"name": "Ferda Kara", "salary": 24000},
    ]
        
    return render_template("index.html", salaries = salaries)

@app.route("/products")
def products():
    
    return render_template("products.html")

@app.route("/about")
def about():
    
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
