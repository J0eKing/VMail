import webview
import threading
import os
x = os.getcwd() + "/GUI"


def start_client():
    import Email.main
    Email.main.start()


if __name__ == '__main__':
    s = threading.Thread(target=start_client)
    s.start()

    # Master window
    webview.create_window('main', url="GUI/index.html", width=800, height=600)