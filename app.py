from flask import Flask
from src.api.admin import admin
from src.middleware import MiddleWare

app = Flask(__name__)
app.register_blueprint(admin)

app.wsgi_app = MiddleWare(app.wsgi_app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8081", debug=True)