from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    print("Servidor ativo em http://127.0.0.1:5000")
    app.run(debug=True, port=5000)