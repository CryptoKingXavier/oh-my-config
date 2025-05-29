from flaskapp import db, bcrypt
from flaskapp.users.models import User
from http import HTTPMethod, HTTPStatus
from flask_login import login_user, logout_user
from flask import render_template, request, redirect, url_for, Blueprint, flash

users: Blueprint = Blueprint("users", __name__, template_folder="templates", static_folder="static2", static_url_path="/static2/")

@users.route("/", methods=[HTTPMethod.GET.value])
def index():
  return render_template("users/index.html"), HTTPStatus.OK.value

@users.route("/signup", methods=[HTTPMethod.GET.value, HTTPMethod.POST.value])
def signup():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    hashed_password = bcrypt.generate_password_hash(password)

    user = User(username=username, password=hashed_password)

    db.session.add(user)
    db.session.commit()
    flash("User created successfully!", "info")
    return redirect(url_for("users.login"), code=HTTPStatus.TEMPORARY_REDIRECT.value)
  return render_template("users/signup.html"), HTTPStatus.OK.value

@users.route("/login", methods=[HTTPMethod.GET.value, HTTPMethod.POST.value])
def login():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter(User.username == username).first()

    # if bcrypt.check_password_hash(user.password, password):
    if user:
      login_user(user)
      flash("User logged in successfully!", "info")
      return redirect(url_for("notes.index"), code=HTTPStatus.TEMPORARY_REDIRECT.value)
  return render_template("users/login.html"), HTTPStatus.OK.value

@users.route("/logout", methods=[HTTPMethod.GET.value])
def logout():
  logout_user()
  flash("User logged out successfully!", "info")
  return redirect(url_for("users.index"), code=HTTPStatus.TEMPORARY_REDIRECT.value)
