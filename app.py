from flask import Flask, render_template, request, flash
from forms import RsvpForm
from flask_mail import Message, Mail
import os

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'thmcmahon@gmail.com'
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PASSWORD')
 
mail.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RsvpForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', form=form, section='rsvp')
        else:
            msg = Message('Wedding RSVP', sender='thmcmahon@gmail.com', recipients=['thmcmahon@gmail.com'])
            msg.body = """
            From: %s <%s>
            Dietary Requirements: %s
            Bus Y/N: %s
            """ % (form.names.data, form.email.data, form.reqs.data, form.bus.data)
            mail.send(msg)
            return render_template('index.html', form=form, section='rsvp', completed=True)

    elif request.method == 'GET':
        return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)