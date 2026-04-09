import time
import webbrowser

def open_websites(websites, delay=0.5):
    for url in websites:
        webbrowser.open_new_tab(url)
        time.sleep(delay)