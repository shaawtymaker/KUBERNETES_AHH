from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the ML model API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    