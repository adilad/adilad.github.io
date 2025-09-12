import os
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mystory.html')
def mystory():
    return render_template('mystory.html')

if __name__ == '__main__':
    app.run(debug=True)
