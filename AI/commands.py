import subprocess
import os
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm", "yep"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "do not", "cancel", "nope"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Python Commander. How are you?")
        else:
            f = Fetcher("https://www.google.com/search?source=hp&ei=Sg9pWveDAc7OjwONy4m4Cw&q=" + text)
            answer = f.lookup()
            self.respond(answer)

        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            self.respond("Opening " + app)
            os.system("start " + app + ".exe")

    def respond(self, response):
        #print(response)
        subprocess.call("echo " + response, shell=True)
