import subprocess
import os
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "sure", "do it", "si", "yeah", "confirm"]
        self.cancel = ["no", "negative", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name.")
            elif "your" in text:
                self.respond("My name is Py Commander. How are you?")
        elif "open" in text:
            app = text.split(" ")[-1].lower()
            self.respond("Opening " + app)
            os.system("start " + app)
        else:
            f = Fetcher("https://www.google.com/search?q=")

    def respond(self, text):
        print(text)
        filename = "answer.txt"
        filepath = "./" + filename
        with open(filename, 'w+') as f:
            f.write(text)
            f.close()

        subprocess.call('cscript "C:\Program Files\Jampal\ptts.vbs" < ' + filepath, shell=True)
