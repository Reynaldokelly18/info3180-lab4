from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    fileField = FileField('image upload',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Illegal file detected. Ensure your file has a name and is in one of the following formats: png, jpg, jpeg.')])