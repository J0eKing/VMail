from . import audiorecog, compose, gui
import pyttsx3 as p
import time


def say(thing):
    e = p.init()
    e.say(thing)
    e.runAndWait()


def read(bodies, subjects, senders, u, p):
    y = len(bodies)
    if y == 0:
        say("you have no emails to read")
    else:
        for i in range(0, len(bodies)):
            if senders[i] is None:
                break
            gui.showUnread(u, senders[i], subjects[i], bodies[i])
            say("email from " + senders[i])
            say("subject is " + subjects[i])
            say("body is " + bodies[i])
            time.sleep(2)
            say("do you want to reply")
            x = audiorecog.listen()
            isInaudible = True
            while isInaudible:
                if x == "@#":
                    say("i couldnt get that, repeat?")
                    x = audiorecog.listen()
                elif x == "no":
                    isInaudible = False
                    break
                elif x == "yes":
                    y = senders[i][senders[i].index('<') + 1:len(senders[i]) - 1]
                    compose.compos(y, "Re: " + subjects[i], u, p)
                    isInaudible = False
                else:
                    say("say a valid command")
                time.sleep(2)
                x = audiorecog.listen()
                y = y - 1

