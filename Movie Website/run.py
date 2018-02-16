from entertainment_center import app
import threading
import time
import webbrowser

def start_browser():
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000/')

browser_thread = threading.Thread(target=start_browser)
browser_thread.start()
app.run()
