from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddPost(FlaskForm):
    title = StringField("Title")
    content = StringField("Content")
    submit = SubmitField("Submit")
