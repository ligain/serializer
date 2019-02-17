import json
import yaml


class SongSerializer:
    def __init__(self):
        self.serializers = {
            'json': self._serialize_to_json,
            'yaml': self._serialize_to_yaml
        }

    def serialize(self, song, output_format='json'):
        return self.serializers[output_format](song)

    def _validate_song(self, song):
        pass

    def _prepare_data(self, song):
        return {
            'title': song.title,
            'artist': '{} {}'.format(song.artist.first_name, song.artist.last_name),
            'duration': str(song.duration)
        }

    def _serialize_to_json(self, song):
        payload = self._prepare_data(song)
        return json.dumps(payload)

    def _serialize_to_yaml(self, song):
        payload = self._prepare_data(song)
        return yaml.dump(payload)


def serialize_object(serializeble, output_format):
    pass


class JsonSerializer:
    def __init__(self):
        self._current_obj = {}

    def app_property(self, name, value):
        self._current_obj[name] = value

    def to_str(self):
        return json.dumps(self._current_obj)


class YamlSerializer:
    def __init__(self):
        self._current_obj = {}

    def app_property(self, name, value):
        self._current_obj[name] = value

    def to_str(self):
        return yaml.dump(self._current_obj)
