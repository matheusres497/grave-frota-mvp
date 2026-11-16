# Flask app setup

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>GRAVE - MVP Frota Operacional (ODS 3)</h1><p>Status: Operacional</p>"

def calcular_revisao(km_atual, km_ultima):
    return (km_atual - km_ultima) >= 5000

if __name__ == "__main__":
    app.run(debug=True)
