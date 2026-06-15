import subprocess
import os
import time
import apps
import main

def open_the_app(app, what,url):
    if what == "search":
        subprocess.Popen([app, url])
