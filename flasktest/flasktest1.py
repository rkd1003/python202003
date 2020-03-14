from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        return 'A horse no name'
    else:
        return 'A horse named %s'%name

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        return render_template('list.html', data=request.form)

        # return redirect(url_for('listdata',name=request.form['Name']))  리다이렉트
    else:
        return "get"

@app.route('/list/<name>')
def listdata(name):
    return name

@app.route('/form/')
def form():
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8890)