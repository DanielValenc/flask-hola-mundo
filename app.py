from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>¡Hola, mundo!</h1><p>Esta es una aplicación web simple con Flask.</p>"

if __name__ == "__main__":
    app.run(debug=True)
