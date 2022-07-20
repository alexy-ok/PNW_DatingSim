# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:
    $ rng4dice= 0
    $ score = 0
    $ buggy = 0
    "The stands rumble with excitement"
    "DING DING DING"
    "Automation has started!"
    if buggy == 0:
        $rng4dice = renpy.random.randint(0,3)
        $score = score + rng4dice
        "Your robot whirs and spins in excitement"
        "NO BUGS"
        "Your robot lines up for a shot"
        if score == 0:
            "And misses them all D:"
        elif:
            "And scores [rng4dice] into the basket!"
        
    return
