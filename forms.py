from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, URLField, SubmitField
from wtforms.validators import InputRequired, URL, Optional, ValidationError

def validate_species(form, field):
    """Custom validator for species"""
    allowed_species = ['dog', 'cat', 'porcupine']
    if field.data.lower() not in allowed_species:
        raise ValidationError(f'Species must be one of: {", ".join(allowed_species)}')
    
def validate_age(form, field):
    """Custom validator for age"""
    if field.data < 0 or field.data > 30:
        raise ValidationError('Age must be between 0 and 30')

class PetForm(FlaskForm):
    """Add pet form """
    name = StringField('Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), validate_species])
    photo_url = URLField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), validate_age])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available', default=True)
    submit = SubmitField('Add Pet')

class EditPetForm(FlaskForm):
    """Edit pet form"""
    name = StringField('Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), validate_species])
    photo_url = URLField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), validate_age])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available', default=True)
    submit = SubmitField('Update')