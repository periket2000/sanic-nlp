from langdetect import detect

DEFAULT = "Not known"

class Nlp:
    def __init__(self):
        pass

    def lang(self, sentence):
        if sentence:
            try:
                lang = detect(sentence)
                return lang
            except:
                return DEFAULT
        else:
            return DEFAULT