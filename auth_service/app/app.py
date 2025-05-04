from flask import Flask, request, render_template, redirect, url_for, session
from models import db, User
from config import Config
from flask_migrate import Migrate, upgrade

app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = 'vraiment_un_secret'

db.init_app(app)
migrate = Migrate(app, db)



# creation auto table
with app.app_context():
    db.create_all()


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return "ERREUR\nL'utilisateur existe déja dans la BDD", 409
        
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username ### enregistre le nom d'utilisateur
            return redirect(url_for("home"))

        return "ERREUR\nL'utilisateur n'existe pas", 401

    return render_template("login.html")

@app.route("/home")
def home():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    return render_template("home.html",username=username)

if __name__ == "__main__" :
    with app.app_context():
        upgrade() # flask db upgrade

    app.run(host='0.0.0.0', port=5000)
