from textblob import TextBlob

DEFAULT = "Not known"

class NlpGoogle:
    def __init__(self):
        pass

    def lang(self, sentence):
        if sentence:
            try:
                lang = TextBlob(sentence).detect_language()
                return lang
            except:
                return DEFAULT
        else:
            return DEFAULT