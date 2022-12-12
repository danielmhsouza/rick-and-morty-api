from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField


class CharacterForm(FlaskForm):

    id = IntegerField("Identificador", render_kw={"placeholder": "ID"})
    name = StringField("Nome do Personagem", render_kw={"placeholder": "Name"})