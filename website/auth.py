from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return render_template("login.html", zmienna=2)

@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if signUpValidation():
            pass
    return render_template("sign_up.html")

@auth.route('/you', methods=['GET', 'POST'])
def you():
    if request.method == 'POST':
        ip = jsonify({'ip': request.remote_addr}), 200
        gender      = request.form.get('gender')
        age         = request.form.get('age')
        height      = request.form.get('height')
        weight      = request.form.get('weight')
        silhouette  = request.form.get('silhouette')
        hairColour  = request.form.get('hairColour')
        facialHair  = request.form.get('facialHair')
        glasses     = request.form.get('glasses')
        skinColour  = request.form.get('skinColour')
        eyeColour   = request.form.get('eyeColour')
        date        = request.form.get('date')


        if youDataValidation():

            user = User.query.filter_by(gender=gender, age=age, height=height, weight=weight, silhouette=silhouette,
                                        hair_colour=hairColour, facial_hair=facialHair, glasses=glasses,
                                        skin_colour=skinColour, eye_colour=eyeColour
                                        ).first()

            new_user = User(gender=gender, age=age, height=height, weight=weight, silhouette=silhouette,
                            hair_colour=hairColour, facial_hair=facialHair, glasses=glasses,
                            skin_colour=skinColour, eye_colour=eyeColour, date=date
                            )
            db.session.add(new_user)
            db.session.commit()
            flash('Added you successfully!', category='success')

            if user:
                flash('Znaleziono identycznego zioma!', category='success')
            else:
                flash('Nie znaleziono identycznego zioma', category='error')


                return redirect(url_for('views.home'))

    return render_template("you.html")



def signUpValidation():
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
        flash('Email must be longer than 3 characters', category='error')
        return False
    elif len(firstName) < 2:
        flash('Name must be longer than 1 character', category='error')
        return False
    elif password1 != password2:
        flash('Passwords doesn\'t match!', category='error')
        return False
    elif len(password1) < 7:
        flash('Password must be at least 7 characters', category='error')
        return False
    else:
        flash('Account created!', category='success')
        return True
def youDataValidation():
    gender = request.form.get('gender')
    age = request.form.get('age')
    height = request.form.get('height')
    weight = request.form.get('weight')
    hairColour = request.form.get('hairColour')
    skinColour = request.form.get('skinColour')
    eyeColour = request.form.get('eyeColour')
    silhouette = request.form.get('silhouette')

    if gender == '-':
        flash('You forgot to choose gender!', category='error')
        return False

    elif age == '':
        flash('You forgot to bring your age!', category='error')
        return False
    elif int(age) < 0 or int(age) > 120:
        flash('Are you sure you\'re that old?', category='error')
        return False

    elif height == '':
        flash('You forgot to bring your height!', category='error')
        return False

    elif int(height) < 50 or int(height) > 273:
        flash('Height is invalid!', category='error')
        return False

    elif weight == '':
        flash('You forgot to bring your weight!', category='error')
        return False
    elif int(weight) < 10 or int(weight) > 610:
        flash('Weight is invalid!', category='error')
        return False

    elif hairColour == '-':
        flash('You forgot to bring hair colour!', category='error')
        return False

    elif skinColour == '-':
        flash('You forgot to bring skin colour!', category='error')
        return False

    elif eyeColour == '-':
        flash('You forgot to bring eye colour!', category='error')
        return False
    elif silhouette == '-':
        flash('You forgot to bring the silhouette!', category='error')
        return False

    else:
        return True
