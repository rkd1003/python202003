from flask import Flask, render_template
app = Flask(__name__)

@app.route('/info')
def index():
<<<<<<< HEAD
    return 'Hello Flask'
    
@app.route('/')
def info():
     return render_template('index.html')

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8890",debug=True)
=======
    return 'hello Flask'

@app.route('/')
def info():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8891",debug=True)
>>>>>>> b2909666a18466e8e018966d90d52045a10b8e6a
