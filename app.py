import os

from flask import Flask
from dotenv import load_dotenv
from extensions import mail
from routes.main import main


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)


app.register_blueprint(main, url_prefix='/')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
