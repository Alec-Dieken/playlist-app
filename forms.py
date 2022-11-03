"""Forms for playlist app."""
from wtforms import SelectField, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name',
        validators=[DataRequired()])

    description = StringField('Description',
        validators=[DataRequired()])

    submit = SubmitField('Create playlist')


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title',
        validators=[DataRequired()])

    artist = StringField('Artist',
        validators=[DataRequired()])

    submit = SubmitField('Create song')


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
