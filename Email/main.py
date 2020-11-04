from . import audiorecog as a, compose, reademails, refresh
import webview

def start():
    email = refresh.Email("email@gmail.com", "password")
    email.login()
    email.get_new_emails()
    email.say()
    x = a.listen()
    while True:
        if x == "help":
            a.say("read, to read out your unread emails, new, to compose a new email, refresh, to refresh your inbox, close, to close the app")
        elif x == "read":
            reademails.read(email.body, email.subject, email.sender, email.user, email.passw)
        elif x == "new":
            compose.compos(f=email.user, p=email.passw)
        elif x == "@#":
            a.say("i didnt catch that, could you repeat it")
        elif x == "close":
            webview.destroy_window()
            email.close()
            exit()
        elif x == "refresh" or "reference":
            email.get_new_emails()
            email.say()
        else:
            a.say("say a valid command")
        x = ''
        x = a.listen()

