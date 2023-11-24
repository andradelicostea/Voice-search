import pyttsx3
from bs4 import BeautifulSoup
from audio.get_answer import Fetcher


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

class Commands:

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet. :(")
            else:
                self.respond("My name is pyguy.  How you doin'? :)")
        else:
            f = Fetcher("https://www.google.ca/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)
    
    def respond(self, response):
        print(response)
        say(response)
        