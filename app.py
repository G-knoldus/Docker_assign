from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def docker_assign():
    return render_template('main.html')