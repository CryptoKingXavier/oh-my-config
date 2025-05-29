from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flaskapp.config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for


bcrypt: Bcrypt = Bcrypt()
db: SQLAlchemy = SQLAlchemy()


def create_app(config_class=Config):
  app: Flask = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)

  login_manager: LoginManager = LoginManager()
  login_manager.init_app(app)

  from flaskapp.users.models import User

  @login_manager.user_loader
  def load_user(uid):
    return User.query.get(uid)

  @login_manager.unauthorized_handler
  def unauthorized_callback():
    return redirect(url_for("core.unauth"))

  @app.errorhandler(401)
  def unauthorized(e):
    return redirect(url_for("notes.index"))

  bcrypt.init_app(app)

  # Importing Blueprints
  from flaskapp.core.routes import core
  from flaskapp.users.routes import users

  # Registering Blueprints
  app.register_blueprint(core, url_prefix="/")
  app.register_blueprint(users, url_prefix="/users")

  migrate: Migrate = Migrate(app, db)

  return app
