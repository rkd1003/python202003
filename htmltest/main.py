from flask import Flask, render_template
app = Flask(__name__)

@app.route('/info')
def index():
    return 'hello Flask'

@app.route('/')
def info():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8891",debug=True)