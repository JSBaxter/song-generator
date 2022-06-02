from song_generator import __version__
from song_generator.model import PitchClass

import pytest


def test_version():
    assert __version__ == "0.1.0"


def test_create_PitchClass_raises_type_error_for_no_input():
    with pytest.raises(TypeError) as err:
        pitch_class = PitchClass()


def test_create_PitchClass_raises_value_error_for_invalid_pitch_class():
    with pytest.raises(ValueError) as err:
        pitch_class = PitchClass("H")
    with pytest.raises(ValueError) as err:
        pitch_class = PitchClass(13)


def test_create_PitchClass_assigns_semitone():
    c = PitchClass("C")
    assert c.semitone == 0
    b = PitchClass("B")
    assert b.semitone == 11
    d = PitchClass("D")
    assert d.semitone == 2
    c = PitchClass("Cb")
    assert c.semitone == 11
    c = PitchClass("C#")
    assert c.semitone == 1
