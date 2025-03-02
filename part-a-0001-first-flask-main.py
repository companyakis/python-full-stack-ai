from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Main Page"

@app.route("/products")
def products():
    return "Our products"

@app.route("/about")
def about():
    return "About"

if __name__ == "__main__":
    app.run(debug = True)
