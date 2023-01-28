from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "123"

    from routes import routes
    from auth import auth
    #Use the http routes as defined in auth and routes as Blueprints
    app.register_blueprint(routes, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    app.run(debug=True)
