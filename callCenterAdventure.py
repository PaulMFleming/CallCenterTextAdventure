from random import *
from time import *
import os,sys

locations = ['kitchen', 'managers desk', 'bathroom', 'computer a', 'computer b', 'computer c']
username = ""

# define functions here

def kitchen():
    print "\n\tYou walk into the kitchen."
    sleep(1)
    print "\n\tThe kitchen table is covered in empty chocolate bar wrappers and paper plates.\n\n\tThere's coffee stains on the floor."
    sleep(1.5)
    if raw_input("\n\tThere's a piece of cake still sitting there... Do you take it? y/n: ") == "y":
        print "\n\tIt's looks a little funny."
        sleep(1)
        if raw_input("\n\tEat it anyway? y/n: ") == "y":
            print "\n\tIt's really good, but..."
            sleep(1.5)
            print "\n\tHolding your stomach you run to the bathroom..."
            thinking()
            bathroom_cake()
        else:
            print "\n\tYou put the cake down and walk away slowly..."
            sleep(1)
            direction_question()
    else:
        print "\n\tYou'd prefer not to risk it and get a glass of water instead."
        sleep(2)
        print "\n\tIt's refreshing."
        sleep(1)
        print "\n\tNow, how to get out of here?"
        sleep(2)
        direction_question()

def bathroom_cake():
    print "\n\tYou push the cleaner trolley aside and slam through the toilet doors ignoring the 'closed for cleaning' sign."
    print "\n\tThe cleaner roars at you as you shove her aside and leap for the nearest toilet bowl."
    print "\n\tYour feet slip on the wet floor and you land heavily on your back."
    print "\n\tThe cleaner curses at you in Polish, and hits you repeatedly with her mop."
    print "\n\tWhile scrambling to get up you notice the words DONT EAT THE CAKE written on the wall."
    sleep(3)
    print "\n\tYou rush passed her and back out the door."
    sleep(2)
    choose = raw_input("\n\tWhat do you do? Use the other toilet, or run back to the call center? (toilet/call center): ")
    if choose == "toilet":
        print "\n\tYou clean yourself off and head back in..."
        sleep(2)
        direction_question()
    elif choose == "call center":
        print "\n\tFeeling slightly embarrassed you wipe yourself down and head back in..."
        sleep(2)
        direction_question()
    else:
        print "\n\tChoose: 'toilet' or 'call center' "
        sleep(2)
        bathroom_cake()

def managers_desk():
    print "\n\tYou walk up to the managers desk."
    direction_question()

def bathroom():
    print "\n\tThe bathroom is closed for cleaning."
    enter_anyway = raw_input("\n\tEnter anyway? y/n: ")
    if enter_anyway == "y":
        print "\n\tYou push the door open slightly but it slams shut in your face."
        sleep(1)
        print "\n\tSomeone roars angrily at you from the other side."
        sleep(1)
        if raw_input("\n\tLook for another bathroom?") == 'y':
            sleep(1)
            bathroom_search()
        else:
            sleep(1)
            direction_question()
    else:
        print "\n\tYou decide it's best to go back and try get that call."
        sleep(1)
    direction_question()

def bathroom_search():
    print "\n\tYou wander around looking for another bathroom but every door you find is locked, except one that leads outside..."
    sleep(2)
    if raw_input("\n\tDo you go outside? y/n: ") == 'y':
        print "\n\tThe door slams shut as you step outside."
        sleep(2)
        print "\n\tThere's a keypad to unlock the door. You don't know the code to get back in."
        sleep(2)
        door_choice = raw_input("\n\tWhat do you do?\tpress '1' to go home\tpress '2' to call the manager")
        if door_choice == "1":
            go_home()
        elif door_choice == '2':
            call_manager()
    else:
        print "\n\tYou decide it's best to go back and try to get that call"
        sleep(1)
        direction_question()

def go_home():
    print "\n\tOn the way home you get a text from the manager that says:"
    sleep(2)
    print "\n\tYou're fired"
    sleep(1)
    print "\n\tGAME OVER\n"
    print "\n\tYOU OBVIOUSLY DON'T HAVE WHAT IT TAKES TO WORK IN A CALL CENTER\n\n\n\n\n"

def call_manager():
    print "You explain your situation to the manager who says simply:"
    sleep(2)
    print "\n\tYou're fired"
    sleep(1)
    print "\n\tGAME OVER\n"
    print "\n\tYOU OBVIOUSLY DON'T HAVE WHAT IT TAKES TO WORK IN A CALL CENTER\n\n\n\n\n"

def computer_a():
    print "\n\tYou sit at the computer."
    sleep(1)
    print "\n\tIt looks like the computer is already dialling..."
    sleep(1.5)
    headset_on = raw_input("\n\tDo you want to put on the headset? y/n ")
    if headset_on == "y":
        print "\n\tYou put on the headset"
        sleep(1)
        print "\n\tYou hear someone talking..."
        sleep(1)
        silly_respondant()
    else:
        print "\n\tYou decide you've had enough dialling for now."
        sleep(1)
        direction_question()


def computer_b():
    print "\n\tYou sit at the computer."
    password = raw_input("\n\tEnter password: ")

    if password == "DONT EAT THE CAKE":
        print "\n\tYOU WIN! NOW, YOU CAN GO HOME!"
        print """








        """
    else:
        print"nope..."
        direction_question()

def computer_c():
    print "\n\tYou sit at the computer."
    global username
    username = raw_input("\n\tEnter Username: ")
    raw_input("\n\tHi %s, hit enter to begin dialling" % username)
    thinking()
    angry_resp()

def direction_question():
    print """
    You look around and see a %s, the %s, the %s, %s, %s and %s.
        """ % (locations[0], locations[1], locations[2], locations[3], locations[4], locations[5])

    userchoice = raw_input("\tWhere do you want to go? ")
    if 'kitchen' in userchoice:
        kitchen()
    elif 'managers desk' in userchoice:
        managers_desk()
    elif 'bathroom' in userchoice:
        bathroom()
    elif 'computer a' in userchoice:
        computer_a()
    elif 'computer b' in userchoice:
        computer_b()
    elif 'computer c' in userchoice:
        computer_c()
    else:
        print "\n\tThat's not a location in the call center!"
        direction_question()

def begining():
    print """
    It's your first day working in the call center. You have completed the initial training.

    Now you must get a complete call or you cannot go home.
            """

def thinking():
    for i in range(0, 3):
        sleep(0.6)
        print "\n\t. . . ."

def angry_resp():
    possible_response1 = ['Whaa?', 'Who the fuck is this?', "You're calling from where?", "Who's MRBI when they're at home?"]
    possible_response2 = ['Go and have a shite with yerself!', "Fuck Off!", 'Go on outta that will ya!', "I'd rather piss in me own mouth"]
    i = randint(0, 3)
    response1 = possible_response1[i]
    response2 = possible_response2[i]

    print ("\n\tYou:\tHello this is %s from MRBI. Would you like to take part in a survey?" % username)
    sleep(3)
    print ("\n\tRespondant:\t%s" % response1)
    sleep(2)
    raw_input("\n\tWhat do you say? (Convince them... go on...): ")
    sleep(1)
    print ("\n\tRespondant:\t%s" % response2)
    sleep(1)
    print "\n\tThe line goes dead..."
    sleep(1)
    if raw_input("\n\tWant to try again? y/n? ") == "y":
        angry_resp()
    else:
        direction_question()
possible_response1 = []


def silly_respondant():
    possible_response1 = ["I can't hear you...", "Who's this?", "Hallo... Hallo... Hallo...", "Is there somebody there?", "Is that Johnny taking the piss again?"]
    possible_response2 = ["And who are they now?", "Oh, right", "Are you from the bank?", "Pull the other one!", "How's about that then?"]
    possible_response3 = ["Doing what?", "Is that so?", "Sure I'll give it a go", "You've got three minutes, and if I'm bored by then I'll hang up", "What's that now?"]
    possible_response4 = ["Oh god no, I don't do any of that", "Not my cup of tea mate", "I haven't got that long", "I just remembered that I'm driving", "Call me back in about an hour, I'm in the nip!"]
    i = randint(0, 4)

    response1 = possible_response1[i]
    response2 = possible_response2[i]
    response3 = possible_response3[i]
    response4 = possible_response4[i]

    print ("\n\tRespondant:\t%s" % response1)
    sleep(2)
    print "\n\tYou:\tHi it's..."
    name = raw_input("\n\tEnter your name: ")
    sleep(1)
    print "\n\tYou:\tHi it's %s, from MRBI" % name
    sleep(2)
    print ("\n\tRespondant:\t%s" % response2)
    sleep(2)
    raw_input("\n\tWhat do you say? (Remember your training...):")
    sleep(1)
    print ("\n\tRespondant:\t%s" % response3)
    sleep(2)
    raw_input("\n\tWhat do you say? (Convince them... go on...): ")
    sleep(1)
    print ("\n\tRespondant:\t%s" % response4)
    sleep(2)
    print "\n\tThe line goes dead..."
    sleep(1)

    if raw_input("\n\tWant to try again? y/n ?") == "y":
        silly_respondant()
    else:
        direction_question()


# game starts here

begining()
direction_question()




