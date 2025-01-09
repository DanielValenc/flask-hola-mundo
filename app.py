from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>¡Hola, mundo!</h1><p>Esta es una aplicación web simple con Flask.</p>"

if __name__ == "__main__":
    # Usa el puerto asignado por Render o 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)