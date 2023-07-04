from flask import Flask
from qrcodegenerator.views import qr_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwertyuiop"

app.register_blueprint(qr_bp)

if __name__ == "__main__":
    app.run(debug=True)