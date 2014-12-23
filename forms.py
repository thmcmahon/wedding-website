from flask_wtf import Form
from wtforms import TextField, RadioField, SubmitField, validators, ValidationError

class RsvpForm(Form):
  names = TextField("Names of you and any other guests", [validators.Required('Please enter your and any other guests names')])
  email = TextField("Enter your email address", [validators.Required('Please enter your email'), validators.Email('Please enter a valid email address')])
  reqs = TextField("Do you have any dietary requirements?")
  bus = RadioField("Are you catching the bus to the ceremony?", [validators.Required('We need to know if you\'re catching the bus')], choices=[('Yes', 'Yes'), ('No', 'No')])
  submit = SubmitField("Send")