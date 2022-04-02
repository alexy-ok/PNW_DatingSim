# name of the character.

define b = Character("Bord")
define p = Character("Peng")
define A = Character("Announcer")
default pronounsSub = ""
default pronounsPos = ""
default pronounsObj = ""
default adjPos = ""

# The game starts here.

label start:
    $ inv = []
    $ bordAffectionMeter = 0
    $ pengAffectionMeter = 0

    "Before we start the game, how would you like to be referred to?"
    menu:
        "he/him":
            $ pronounsSub= "he"
            $ pronounsObj = "him"
            $ pronounsPos = "his"
            $ adjPos = "his"
        "she/her":
            $ pronounsSub= "she"
            $ pronounsObj = "her"
            $ pronounsPos = "hers"
            $ adjPos = "her"
        "they/them":
            $ pronounsSub= "they"
            $ pronounsObj = "them"
            $ pronounsPos = "theirs"
            $ adjPos = "their"
        "other":
            jump OtherPronounSetter

label OtherPronounSetter:
    $pronounsSub = renpy.input("please enter your subject pronoun (he, she, they, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    $pronounsObj = renpy.input("please enter your object pronouns (him, her, them, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    $adjPos = renpy.input("please enter your possesive adjective (his, her, their, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    $pronounsPos = renpy.input("please enter your possesive pronouns (his, hers, theirs, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)

label scene1:
    scene sammamish

    "It's my first time at a FIRST event, I wonder what teams are competing today"
    A "Attention, the mascot fair will start momentarily"
    menu:
        "Look around the school":
            "The FIRST event splits the school into a few parts"
            "The Pits are located in the main area, this is where teams can work on their bots"
            "The Field and Stands are in the main gym, these are where robots compete"
            "Items,food, and drinks are all sold at the Concession stand"
            "The outside area is where you can socialize and eat lunch"
            "Finally the quiet room is accessed by the pause button, this is where you can chill without affecting the time"
    jump bordOurple



label bordOurple:
    # These display lines of dialogue.
    show bord at left
    b "Why he ourple?"
    menu:
        "buy roober":
            b "thank you for your purchase"
            $ inv.append("roobeer")
            $ bordAffectionMeter += 1
            b "you have [inv[0]]"
            b "meter is [bordAffectionMeter]"
        "no":
            b "oh"

    return















return
