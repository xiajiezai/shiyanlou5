from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course

def register_blueprints(app):
    from .handlers import front,course,admin,user
    #because you changed the directory in __init__.py, you don't have to write from .handlers.front import front etc
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)


def create_app(config):
    """ load different configuration based on argument config
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # initialize SQLAlchemy object in models.py
    db.init_app(app)
    register_blueprints(app)



    return app
