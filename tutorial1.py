from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime



app = Flask(__name__)

app.config['SECRET_KEY'] = '6952c9374d563e443be9b74bfe266c2a'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"



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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'masooma.jw@gmail.com' and form.password.data=='password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

 
    
    return render_template('login.html', title = 'Login', form=form)



if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    #     user_1 = User(username='Masooma', email='masooma@arcgate.com', password='password')
    
    # # Add the user to the session
    #     db.session.add(user_1)
    
    # # Commit the changes to the database
    # db.session.commit()

    app.run(debug=True)