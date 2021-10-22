from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db
from creds import *
from gevent.pywsgi import WSGIServer



app = Flask(__name__)

app.config['SECRET_KEY'] = AUTH_SECRET_KEY
app.config['PASSWORD_RESET_SECRET'] = AUTH_PASSWORD_RESET_SECRET
app.config['USERNAME'] = DB_USERNAME

@app.route("/", methods=["GET"])
def homepage():
    return "Welcome to ExamScore API."

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

if __name__ == "__main__":
    app.run("localhost", port=1313)

    http_server = WSGIServer(("localhost", 1313), app)
    http_server.serve_forever()
