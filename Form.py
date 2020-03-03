from flask import Flask 
from flask import render_template
from flask import request

info={}

app=Flask(__name__)
@app.route('/')
def main():
    return render_template('Form.html')

@app.route('/NextPage',methods=['POST'])
def main2():
    username=request.form['Name'] 
    email=request.form['Email']
    info[username]=email
    user_name=username
    user_email=email
    return render_template('NextPage.html',name=username)

@app.route('/login')
def main3():
    return render_template('login.html')

@app.route('/profile',methods=['POST'])
def main4():
    username=request.form['username']
    email=request.form['email']
    if username in info.keys() and email==info.get(username):
        return render_template('profile.html', username=username)
    else:
        return render_template('Wrong.html')         
@app.route('/profile/receivedata',methods=['POST'])
def main5():
    text=request.form['text']
    user_name=request.form['username']
    # with open(f'Info/info_.txt','a') as file:
    #     file.write(text)
    print(user_name)
    return 'Data received successfully'
app.run(debug=True)