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

if __name__ == '__main__':
    app.run()
