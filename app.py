from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mystory.html')
def mystory():
    return render_template('mystory.html')


if __name__ == '__main__':
    app.run(debug=True)
