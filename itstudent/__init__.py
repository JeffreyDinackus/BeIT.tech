from flask import Flask
from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()
DB_NAME = "database.db"



if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "123"

    from routes import routes
    from auth import auth
    #Use the http routes as defined in auth and routes as Blueprints
    app.register_blueprint(routes, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_NAME}'
    database.init_app(app)
    app.run(debug=True)
