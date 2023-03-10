from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import jsonify
from sqlalchemy import select, engine
from .functions import *

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return render_template("login.html", zmienna=2)

@auth.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template("chat.html")

@auth.route('/about')
def about():
    return render_template("about.html")

@auth.route('/contact-us')
def contactUs():
    return render_template("contactUs.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/home')
def home():
    random_stat()
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
    print_whole_table()
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

@auth.route('/statistics', methods=['GET', 'POST'])
def statistics():
    # hair statistics
    blonde_prc = stat("hair_colour", "Blonde")
    black_prc = stat("hair_colour", "Black")
    bronze_prc = stat("hair_colour", "Bronze")
    ginger_prc = stat("hair_colour", "Ginger")
    gray_prc = stat("hair_colour", "Gray")
    white_prc = stat("hair_colour", "White")
    hair_other_prc = stat("hair_colour", "Other")

    # silhouette statistics
    slim_prc = stat("silhouette", "Slim")
    skinny_prc = stat("silhouette", "Skinny")
    overweight_prc = stat("silhouette", "Overweight")
    athletic_prc = stat("silhouette", "Athletic")

    # facial hair statistics
    none_prc = stat("facial_hair", "None")
    moustache_prc = stat("facial_hair", "Moustache")
    beard_prc = stat("facial_hair", "Beard")
    moustache_beard_prc = stat("facial_hair", "Moustache + Beard")

    # glasses statistics
    glasses_yes_prc = stat("glasses", "Yes")
    glasses_no_prc = stat("glasses", "No")

    # gender statistics
    male_prc = stat("gender", "Male")
    female_prc = stat("gender", "Female")

    # skin colour statistics tion>White</option>
    skin_white_prc = stat("skin_colour", "White")
    skin_black_prc = stat("skin_colour", "Black")
    skin_yellow_prc = stat("skin_colour", "Yellow")
    skin_other_prc = stat("skin_colour", "Other")

    # eye colour statistics
    eye_brown_prc = stat("eye_colour", "Brown")
    eye_blue_prc = stat("eye_colour", "Blue")
    eye_green_prc = stat("eye_colour", "Green")
    eye_gray_prc = stat("eye_colour", "Gray")
    eye_other_prc = stat("eye_colour", "Other")

    return render_template("statistics.html",
                            #hair_variables
                            blonde=blonde_prc, black=black_prc,
                            bronze=bronze_prc, ginger=ginger_prc, gray=gray_prc,
                            white=white_prc, hair_other=hair_other_prc,

                            #silhouette_variables
                            slim=slim_prc, skinny=skinny_prc,
                            overweight=overweight_prc, athletic=athletic_prc,

                            #facial_hair_variables
                            _none=none_prc, moustache=moustache_prc,
                            beard=beard_prc, moustache_beard=moustache_beard_prc,

                            #gender_variables
                            male = male_prc, female = female_prc,

                            #glasses_variables
                            glasses_yes = glasses_yes_prc, glasses_no = glasses_no_prc,

                            # skin_colour_variables
                            skin_white = skin_white_prc, skin_black = skin_black_prc,
                            skin_yellow = skin_yellow_prc, skin_other = skin_other_prc,

                            # eye_colour_variables
                            eye_brown = eye_brown_prc, eye_blue = eye_blue_prc,
                            eye_green = eye_green_prc, eye_gray = eye_gray_prc,
                            eye_other = eye_other_prc)

