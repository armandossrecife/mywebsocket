from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

STATIC_PATH = os.path.join(app.root_path, 'static')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(STATIC_PATH, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)