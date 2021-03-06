
from flask import Flask, redirect, url_for, request
from flask_mail import Mail, Message
app = Flask(__name__)


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'a.jehoshua@gmail.com'
app.config['MAIL_PASSWORD'] = '*************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail/<name>/<colleg>")
def success(name,college):
   msg = Message('Hello', sender = 'a.jehoshua@gmail.com', recipients = ['a.jehoshua@gmail.com'])
   msg.body = "Name: %s " % name 
   mail.send(msg)
   return "Sent"

@app.route('/task1',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
      		user = request.form['name']
      		
     	 	return redirect(url_for('success',name = user,))
   	else:
      		user = request.args.get('name')
      		return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)

