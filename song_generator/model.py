from dataclasses import dataclass
from typing import ClassVar


@dataclass
class PitchClass:

    name: str
    _pitch_class_names: ClassVar[dict] = {
        "Cb": 11,
        "Db": 1,
        "Eb": 3,
        "Fb": 4,
        "Gb": 6,
        "Ab": 8,
        "Bb": 10,
        "C": 0,
        "D": 2,
        "E": 4,
        "F": 5,
        "G": 7,
        "A": 9,
        "B": 11,
        "C#": 1,
        "D#": 3,
        "E#": 5,
        "F#": 6,
        "G#": 8,
        "A#": 10,
        "B#": 0,
    }
    _pitch_class_numbers: ClassVar[dict] = {
        11: ["Cb", "B"],
        1: ["Db", "C#"],
        3: ["Eb", "D#"],
        4: ["Fb", "E"],
        6: ["Gb", "F#"],
        8: ["Ab", "G#"],
        10: ["Bb", "A#"],
        0: ["C", "B#"],
        2: ["D"],
        5: ["F", "E#"],
        7: ["G"],
        9: ["A"],
    }

    def __init__(self, name):
        if type(name) is str:
            name = name.capitalize()
            if name in self._pitch_class_names:
                self.semitone = self._pitch_class_names[name]
                names = self._pitch_class_numbers[self.semitone]
                
                if len(names) == 1:
                    self.name = name
                else: 
                    pc1, pc2 = names
                    if len(pc1) == 1:
                        name = pc1
                    elif len(pc2) == 1:
                        name = pc2
                    else:
                        name = f'{pc1}/{pc2}'
            else:
                raise ValueError(
                    f"Invalid pitch class type, valid pitch classes are {', '.join(self._pitch_class_names)}"
                )
        else:
            raise ValueError(
                f"Invalid pitch class type, valid pitch classes are {', '.join(self._pitch_class_names)}"
            )

