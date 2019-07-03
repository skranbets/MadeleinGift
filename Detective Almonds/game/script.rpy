# The script of the game goes in this file.
#python:
#    class DeskInvestigation:
#       def __init__(self):
#            self.searchedbody = False
#            self.searcheddesk = False
#            self.talkedisabelle = False
#            self.talkedresetti = False

#       def isFinished(self):
#           return self.searchedbody and self.searcheddesk and self.talkedisabelle and self.talkedresetti


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define isabelle = Character("Isabelle")
define kitty = Character("Kitty")
define resetti = Character("Mr.Resetti")
define tom = Character("Tom Nook")
define hazel = Character("Hazel")
define doctor = Character("Doctor")
default searchedbody = False
default searcheddesk = False
default talkedisabelle = False
default talkedresetti = False
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
    isabelle "Okay, [name]... Oh yes, I see you on the list. You can head right in, the mayor is waiting for you."
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
    
    isabelle "it's locked... well, good thing Mr.Resetti has the key. Let me call him."
    hide worriedisabelle
    #play sound "phone sound"
    "After a few minutes, Mr. Resetti came."
    show resettiangry
    resetti "So the dummy locked himself in the office again? God, I should just get rid of that lock, make thing easier."
    isabelle "I'm sorry, Mr.Resetti, may you please open the door."
    resetti "Fine."
    "{i}Click{/i}"
    #play sound "trying to open a locked door"
    scene office with Dissolve(.5)
    pause .5

    isabelle "MAYOR!!!!!" 
    menu: 
        resetti "Jesus christ... is.. is he dead?"
        "I think he is...":
            jump next

        "Nah, he's just sleeping.":
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
    while not searchedbody or not searcheddesk or not talkedisabelle or not talkedresetti:
        menu:
            "What should I investigate?"
            
            "Body" if not searchedbody:
                jump body
            "Desk" if not searcheddesk:
                jump desk
            "Talk to Isabelle" if not talkedisabelle:
	            $ talkedisabelle = True
	            isabelle "I cannot believe this..."
                jump isabelleinvest
            "Talk to Mr.Resetti" if not talkedresetti:
			    resetti "Urg... what a mess"
                jump resettiinvest
    #jump finishedoffice
    return

label body:
    $ searchedbody = True
    "You approch the body and notice several things:"
    "1) The victim appear to have died from asphyxiation"
    "2) There is a smell of almonds near the victim's mouth"
    "3) That same almond smell is on a muffin, next to the mayor, half eaten"
    jump investigation
    return

label desk:
    $ searcheddesk = True
    player "Hmm, what's this basket on the desk?"
    show basket
    isabelle "Oh, that was a gift the mayor got for his birthday. I think he received it during his last meeting."
    player "Interesting."
	"You notice a note on the basket."
	show note
	return

default askedSchedule = False
default askedIsabelleEnnemy = False

label isabelleinvest:
	while not askedSchedule or not askedIsabelleEnnemy:
	    menu:
		    "Who did the mayor met with today?":
			    $ askedSchedule = True
				isabelle "Well, I do not have his meetings memorized, but I do have a list of it."
				jump isabelleinvest
			"Did the mayor have any ennemies?":
			    $ askedIsabelleEnnemy = True
				isabelle "Oh heavens no, the mayor is very popular."
				isabelle "In fact, he is always actively involved with the community. Every body loves him."
				player "Well, he is a mayor, doesn't that mean he has to be the bad guy at times? Like firing staff or denying legislation?"
				isabelle "Well, since mayor is always trying to please everyone, he doesn't enjoy bringing bad news."
				player "So who does then?"
				isabelle "That would be me... I'm in charge of everything the mayor does not want to handle."
				player "I see, thank you for your time."
				jump isabelleinvest



label resettiinvest:
    player "This is a true tragedy."
	resetti "Yeah... I feel really bad comme."



        


    
    
    # This ends the game.
return
    