from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import jsonify
from sqlalchemy import select, engine
from .validation import *
from .functions import *

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

        if sign_up_valid(email, first_name, password1, password2):
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

        if you_valid(gender, age, height, weight, silhouette, hair_colour, skin_colour, eye_colour):

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
