from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
    print 'New user created'
    name = request.form['name']
    # passes in 'name' from form with magic
    print 'Welcome ' + name
    return redirect('/')


app.run(debug=True)