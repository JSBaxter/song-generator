from song_generator import __version__
from song_generator.model


def test_version():
    assert __version__ == '0.1.0'

def test_create_note_raises_value_error_for_invalid_note():
    