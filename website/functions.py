import sqlalchemy
import random
from .models import User
from flask import flash


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
    if b is None:
        return False
    elif abs(a-b) <= max_difference:
        return True

    return False


def print_whole_table():
    users = User.query.all()
    for user in users:
        print(user.id, user.ipaddress, user.date ,user.gender, user.age, user.height, user.weight, user.silhouette, user.hair_colour, user.facial_hair, user.glasses, user.skin_colour, user.eye_colour)


def sign_up_validation(email, firstName, password1, password2):

    if len(email) < 4:
        flash('Email must be longer than 3 characters', category='error')
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
#test

def stat(column, argument):
    users = User.query.all()
    argument_counter = int(0)
    other_counter = int(0)
    column = 'user.'+column

    for user in users:
        if (eval(column)==argument):
            argument_counter += 1
        else:
            other_counter +=1

    if argument_counter+other_counter==0:
        return "Pusta baza danych"

    statistic = argument_counter / (argument_counter + other_counter)
    print(statistic)
    return round(argument_counter / (argument_counter + other_counter),2)


def random_stat():
    #Function gives random statistic
    users = User.query.all()
    arguments = ["gender", "silhouette", "hair_colour", "facial_hair", "glasses", "skin_colour", "eye_colour"]
    for i in range(20):
        argument1 = random.choice(arguments)
        argument2 = random.choice(arguments)
        while argument1 == argument2:
            argument1 = random.choice(arguments)
            argument2 = random.choice(arguments)
        #To this moment, program only have choosen two features to look for (they are always different)
        print(argument1, argument2)
        print("======")

