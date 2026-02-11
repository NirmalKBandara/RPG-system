from enum import Enum

from character_types.archer import Archer
from character_types.healer import Healer
from character_types.mage import Mage
from character_types.shielder import Shielder
from character_types.warrior import Warrior

class CharacterType(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ARCHER = "Archer"
    HEALER = "Healer"
    SHIELDER = "Shielder"

class CharacterFactory:
    _character_classes = {
        CharacterType.WARRIOR: Warrior,
        CharacterType.MAGE: Mage,
        CharacterType.ARCHER: Archer,
        CharacterType.HEALER: Healer,
        CharacterType.SHIELDER: Shielder
    }

@classmethod
def create_character(cls, char_type, name):
    char_class = cls._character_classes.get(char_type)
    if not char_class:
        raise ValueError(f"Invalid character type: {char_type}")
    return char_class(name)