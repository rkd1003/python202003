from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index copy.html')

@app.route('/form')
def inputform():
    return render_template('form.html')

@app.route('/inputdata')
def inputdata():
    return "inputdata"

@app.route('/list')
def listdata():
    return render_template('list.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8890,debug=True)
