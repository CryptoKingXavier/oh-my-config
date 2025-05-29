from http import HTTPMethod, HTTPStatus
from flask import Blueprint, render_template, redirect, url_for

core: Blueprint = Blueprint("core", __name__, template_folder="templates", static_folder="static", static_url_path="/")

@core.route("/", methods=[HTTPMethod.GET.value])
def index():
  return redirect(url_for("users.index")), HTTPStatus.OK.value

@core.route("/unauth", methods=[HTTPMethod.GET.value])
def unauth():
  return render_template("core/unauth.html"), HTTPStatus.UNAUTHORIZED.value