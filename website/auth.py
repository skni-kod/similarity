from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import jsonify
from sqlalchemy import select, engine

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
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if sign_up_validation(email, first_name, password1, password2):
            pass
    return render_template("sign_up.html")


@auth.route('/you', methods=['GET', 'POST'])
def you():
    #print_whole_table()
    if request.method == 'POST':
        ip = jsonify({'ip': request.remote_addr}), 200
        gender       = request.form.get('gender')
        age          = request.form.get('age')
        height       = request.form.get('height')
        weight       = request.form.get('weight')
        silhouette   = request.form.get('silhouette')
        hair_colour  = request.form.get('hair_colour')
        facial_hair  = request.form.get('facial_hair')
        glasses      = request.form.get('glasses')
        skin_colour  = request.form.get('skin_colour')
        eye_colour   = request.form.get('eye_colour')
        date         = request.form.get('date')

        if you_data_validation(gender, age, height, weight, silhouette, hair_colour, skin_colour, eye_colour):

            number_of_smlrs = number_of_similars(gender, age, height, weight, skin_colour)
            number_of_idntcl = number_of_identical(gender, age, height, weight, silhouette, hair_colour, facial_hair, glasses, skin_colour, eye_colour)

            new_user = User(gender=gender, age=age, height=height, weight=weight, silhouette=silhouette,
                            hair_colour=hair_colour, facial_hair=facial_hair, glasses=glasses,
                            skin_colour=skin_colour, eye_colour=eye_colour, date=date
                            )

            db.session.add(new_user)
            db.session.commit()
            flash('Added you successfully!', category='success')

            if number_of_idntcl > 0:
                message = 'Found ' + str(number_of_idntcl) + ' identical person!'
                flash(message, category='success')

            elif number_of_smlrs > 0:
                message = 'Found ' + str(number_of_smlrs) + ' similar person!'
                flash(message, category='success')

            else:
                flash('You are unique.', category='error')

            return redirect(url_for('views.home'))

    return render_template("you.html")


def sign_up_validation(email, first_name, password1, password2):

    if len(email) < 4:
        flash('Email must be longer than 3 characters', category='error')
        return False
    elif len(first_name) < 2:
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


def you_data_validation(gender, age, height, weight, silhouette, hair_colour, skin_colour, eye_colour):
    result = True
    #niepoprawnie sprawdza warunki. dla sylwetki sprawdza poprawnie, dla hair_colour, skin_colour... jakby ignorował, do naprawienia
    print(gender, age, height, weight, silhouette, hair_colour, skin_colour, eye_colour)
    if gender == '-':
        flash('You forgot to choose gender!', category='error')
        result = False

    if age == '':
        flash('You forgot to bring your age!', category='error')
        result = False

    elif int(age) < 0 or int(age) > 120:
        flash('Are you sure you\'re that old?', category='error')
        result = False

    if height == '':
        flash('You forgot to bring your height!', category='error')
        result = False

    elif int(height) < 50 or int(height) > 273:
        flash('Height is invalid!', category='error')
        result = False

    if weight == '':
        flash('You forgot to bring your weight!', category='error')
        result = False

    elif int(weight) < 10 or int(weight) > 610:
        flash('Weight is invalid!', category='error')
        result = False

    if hair_colour == '-':
        flash('You forgot to bring hair colour!', category='error')
        result = False

    if skin_colour == '-':
        flash('You forgot to bring skin colour!', category='error')
        result = False

    if eye_colour == '-':
        flash('You forgot to bring eye colour!', category='error')
        result = False

    if silhouette == '-':
        flash('You forgot to bring the silhouette!', category='error')
        result = False

    return result


def number_of_similars(gender, age, height, weight, skin_colour):
    age = int(age)
    height = int(height)
    weight = int(weight)

    users = User.query.all()
    counter = int(0)
    for user in users:
        if (gender == gender and difference(age, user.age, 2) and difference(height, user.height, 3) and
                difference(weight, user.weight, 2) and skin_colour == user.skin_colour):
            counter += 1

    return counter


def number_of_identical(gender, age, height, weight, silhouette, hair_colour, facial_hair, glasses, skin_colour, eye_colour):

    age = int(age)
    height = int(height)
    weight = int(weight)

    number_of_identic = User.query.filter_by(
                                gender=gender, age=age, height=height, weight=weight, silhouette=silhouette,
                                hair_colour=hair_colour, facial_hair=facial_hair, glasses=glasses,
                                skin_colour=skin_colour, eye_colour=eye_colour
                                ).count()

    return number_of_identic


def difference(a, b, max_difference):
    a = int(a)
    max_difference = int(max_difference)

    if abs(a-b) <= max_difference:
        return True

    return False


def print_whole_table():
    users = User.query.all()
    for user in users:
        print(user.id, user.ipaddress, user.date ,user.gender, user.age, user.height, user.weight, user.silhouette, user.hair_colour, user.facial_hair, user.glasses, user.skin_colour, user.eye_colour)
