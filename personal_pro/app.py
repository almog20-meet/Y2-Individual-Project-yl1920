
from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/', methods=['GET','POST'])
def home():
	return render_template("home.html")

@app.route('/aid')
def aid():
	return render_template("aid.html")


@app.route('/police')
def police():
	return render_template("police.html")

@app.route('/fire')
def fire():
	return render_template("fire.html")



###########

if __name__ == '__main__':
    app.run(debug=True)