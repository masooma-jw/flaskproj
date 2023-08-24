from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET KEY'] = '6952c9374d563e443be9b74bfe266c2a'


posts = [
    {
    'author':'Masooma',
    'title':'Blog post 1',
    'date_posted': 'August 5, 2023',
    'content': 'post content'   
    },
    {
    'author':'Sanah',
    'title':'Blog post 2',
    'date_posted': 'May 23, 2023',
    'content': 'post content'   
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)