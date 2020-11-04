import smtplib
from . import audiorecog as a, gui
import webview
import os

def send(user, passw, to, subject, msg):
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()

    s.login(user, passw)

    message = "\r\n".join([
        "From: " + user,
        "To: " + to,
        "Subject: " + subject,
        "",
        msg
    ])
    s.sendmail(user, to, message)

def compos(t='', r='', f='', p='', body=''):
    done = False
    subj = ''
    gui.showUnread(t, f, r, body)
    while not done:
        if t == '':
            a.say("Who do you want to send this email to")
            to = a.listen()
            while to == "@#":
                a.say("i didnt catch that, could you repeat")
                to = a.listen()
        else:
            to = t
        to = to.replace(' ', '')
        gui.showUnread(to, f, subj, body)
        if r == '':
            a.say("What is the subject")
            subj = a.listen()
            while subj == "@#":
                a.say("i didnt catch that, could you repeat")
                subj = a.listen()
        else:
            subj = r
        gui.showUnread(to, f, subj, str(body))
        a.say("What is the body")
        bdone = False
        body = ""
        while not bdone:
            x = a.listen()
            if x == '@#':
                a.say("i didn't catch that, could you repeat")
                continue
            body = body + ' ' + x
            gui.showUnread(to, f, subj, body)
            a.say("are you done with the body")
            s = a.listen()
            if s == "yes":
                bdone = True
                break
            elif s == 'no':
                print("ok")
            else:
                a.say("yes or no")
        if to.lower() == "proto":
            to = to + "@protonmail.com"
        elif to.index("@") != -1:
            print(to)
        else:
            to = to + "@gmail.com"
        gui.showUnread(to, f, subj, body)
        a.say("To: " + to)
        a.say("subject: " + subj)
        a.say("body: " + body)
        a.say("are you done, and ready to send")
        v = a.listen()
        while v not in ["yes, no"]:
            if v == "yes":
                send(f, p, to, subj, body)
                print("sent")
                a.say("sent")
                done = True
                webview.load_url("file://" + os.getcwd() + "/GUI/index.html")
                print("file://" + os.getcwd() + "/GUI/index.html")
                a.say("read, to read out your unread emails, new, to compose a new email, refresh, to refresh your inbox, close, to close this app")
                break

            elif v == "no":
                break
            else:
                a.say("i couldnt catch that, please repeat")
            v = a.listen()
