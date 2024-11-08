from flask import render_template
from app import app

# Rota para o index (página inicial)
@app.route('/')
def index():
    return render_template('index.html')
