from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def func():
    return render_template('index.html')
@app.route('/showname', methods=['POST'])
def takename():
    if request.method=='POST':
        username=request.form['Name']
        age=request.form['Age']
        with open('info.txt','a') as file:
            file.write(f'Name : {username}\nAge : {age}\n') 
    return 'Okay'

if __name__=='__main__':
    app.run(debug=True)
