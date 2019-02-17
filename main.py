from datetime import timedelta

from serializer.serializers import SongSerializer


class Artist:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Song:
    def __init__(self, title: str, artist: Artist, duration: timedelta):
        self.title = title
        self.duration = duration
        self.artist = artist

    def serialize(self, serializer):
        serializer.app_property('title', self.title)


if __name__ == '__main__':
    clayderman = Artist(first_name='Richard', last_name='Clayderman')
    the_hit = Song(
        title='Ballade Pour Adeline',
        artist=clayderman,
        duration=timedelta(minutes=2, seconds=36)
    )
    song_serializer = SongSerializer()
    song_json_output = song_serializer.serialize(the_hit, 'yaml')
    print(song_json_output)
