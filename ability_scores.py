from enum import Enum, auto
from race import Race



class QuickStartAbilityScores():

    def __init__(self, race, class_):
        
     



class Races(Enum):
    DWARF = auto()
    ELF = auto()
    HALFLING = auto()
    HUMAN = auto()
    DRAGONBORN = auto()
    GNOME = auto()
    HALFELF = auto()
    HALFORC = auto()
    TIEFLING = auto()

class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()

# @dataclass
# class Race():

#     strength_increase=0
#     dexterity_increase=0
#     constitution_increase=0
#     intelligence_increase=0
#     wisdom_increase=0
#     charisma_increase=0
#     size
#     speed
#     languages: set
#     darkvision=False
#     dwarven_resilience=False
#     dwarven_combat_training=False
#     trance=False
#     keen_senses=False
#     fey_ancestry=False
#     elf_weapon_training=False
#     cantrip=False
#     extra_language=False
#     fleet_of_foot=False
#     mask_of_the_wild=False
#     superior_darkvision=False
#     sunlight_sensitivity=False
#     drow_magic=False
#     drow_weapon_training=False
#     lucky=False
#     brave=False
#     halfling_nimbleness=False
#     draconic_ancestry=False
#     breath_weapon=False
#     damage_resistence=False
#     gnome_cunning=False
#     artificers_lore=False
#     tinker=False
#     skill_versatility=False
#     menacing=False
#     relentless_endurance=False
#     savage_attacks=False
#     hellish_resistance=False
#     infernal_legacy=False

    



class Classes(Enum):
    BARBARIAN = auto()
    BARD = auto()
    CLERIC = auto()
    DRUID = auto()
    FIGHTER = auto()
    MONK = auto()
    PALADIN = auto()
    RANGER = auto()
    ROGUE = auto()
    SORCERER = auto()
    WARLOCK = auto()
    WIZARD = auto()
    




        
     


# Classes--Dnd suggests for "quick" builds of classes, simple min max strategies.
# Like for fighter--suggest make strength or dexterity highest ability score,
# followed by constitution.  Next highest score is constitution, followed by
# intelligence
 
# : 15, 14, 13, 12, 10, 8.
# Standard ability scores
 
# Quick

# You can make a fighter quickly by follow in g these
# suggestion s. First, m ake Strength or Dexterity your
# highest ability score, depen din g on w hether you
# w ant to focu s on m elee w eap on s or on archery (or
# fin esse w eapons). Your next-highest score should be
# Constitution, or Intelligence if you plan to adopt the
# Eldritch K night m artial archetype. Second , choose
# the soldier background

quick_build_fighter = AbilityScores(
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=12
    wisdom=10
    charisma=8
)


