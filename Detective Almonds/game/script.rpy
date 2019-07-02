# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define isabelle = Character("Isabelle")
define kitty = Character("Kitty")
define resetti = Character("Mr.Resetti")
define tom = Character("Tom Nook")
define hazel = Character("Hazel")
define doctor = Character("Doctor")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene frontdesk  with Dissolve(.5)
    pause .5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show isabellehappy


    # These display lines of dialogue.

    isabelle "Hello there, Welcome to our town! You are here for your meeting with the mayor right?"

    isabelle "Can I please get the name for the meeting?"
    python:
        name = renpy.input("Please enter your name")
    define player = Character("[name]")
    isabelle "Okay, [name]... Oh yes, I see you on the list. You can head right in, the mayor is waiting for you"
    hide isabellehappy
    "{i}You walk to the mayor's office and you knock on the door{/i}"
    "Knock Knock Knock"
    #play sound "knock.mp3"
    "..."
    "Knock Knock Knock"
    #play sound "knock.mp3"
    "..."
    player "Um... He isn't answering."
    show worriedisabelle
    isabelle "Really? That's weird, lemme try."
    "Knock Knock Knock"
    #play sound "knock.mp3"
    isabelle "Mayor? Your 10'o clock is here!"
    "..."
    isabelle "That's weird... Well, let's just go in and see what's up, maybe he fell asleep."
    "{i}Click clang{/i}"
    #play sound "trying to open a locked door"
    
    isabelle "it's locked... well, good thing Mr.Resetti has the key. Let me call him"
    hide worriedisabelle
    #play sound "phone sound"
    "After a few minutes, Mr. Resetti came."
    show resettiangry
    resetti "So the dummy locked himself in the office again? God, I should just get rid of that lock, make thing easier"
    isabelle "I'm sorry, Mr.Resetti, may you please open the door"
    resetti "Fine"
    "{i}Click{/i}"
    #play sound "trying to open a locked door"
    scene office with Dissolve(.5)
    pause .5

    isabelle "MAYOR!!!!!" 
    menu: 
        resetti "Jesus christ... is.. is he dead?"
        "I think he is...":
            jump next

        "Nah, he's just sleeping":
            jump joke

label joke:
    isabelle "WHAT IS WRONG WITH YOU! HOW CAN YOU JOKE AT A TIME LIKE THIS."
    resetti "Pretty sure he is dead."
    jump next
    return

label next:
    isabelle "Poor mayor... How could this happen."
    player "We need to investigate what happened here. Everyone please stay away from the body."
    jump investigation
    return

label investigation:
    $ searchedbody = False
    $ searcheddesk = False
    $ talkedisabelle = False
    $ talkedresetti = False
    
    if not searchedbody or not searcheddesk or not searcheddesk or not searcheddesk:
        menu:
            "What should I investigate?"
            
            "Body" if not searchedbody:
                jump body
            "Desk" if not searcheddesk:
                jump desk
            "Isabelle" if not talkedisabelle:
                jump isabelleinvest
            "Mr.Resetti" if not talkedresetti:
                jump resettiinvest
    #jump finishedoffice
    return

label body:
    "You approch the body and notice several things:"
    "1) The victim appear to have died from asphyxiation"
    "2) There is a smell of almonds near the victim's mouth"
    "3) That same almond smell is on a muffic, next to the mayor, half eaten"
    jump investigation
    return

label desk:
    player "Hmm, what's this basket on the desk?"
    show basket
    isabelle "Oh, that was a gift the mayor got for his birthday. I think he received it during his last meeting."
    player "Interesting"

        


    
    
    # This ends the game.
return
    