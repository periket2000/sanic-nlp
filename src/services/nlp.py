from langdetect import detect

DEFAULT = "Not known"

class Nlp:
    def __init__(self):
        pass

    def lang(self, sentence):
        if sentence:
            return detect(sentence)
        else:
            return DEFAULT