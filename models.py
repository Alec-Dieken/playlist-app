"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlists."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(250))
    
    playlists_songs = db.relationship('PlaylistSong', backref='playlists')
    songs = db.relationship('Song', secondary='playlists_songs', backref='playlists')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))


class Song(db.Model):
    """Songs."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    playlists_songs = db.relationship('PlaylistSong', backref='songs')


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)