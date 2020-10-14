from flask import Flask, render_template

SECRET_KEY = b'\xf2\xb7\x99\x96\x99/K,t\x07\x08\x14RM\x0f\xd5'

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def index():
    return render_template('index.html')




