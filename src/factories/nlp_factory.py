from services.nlp import Nlp
from services.nlp_google import NlpGoogle

services = {
    'langdetect': Nlp,
    'textblob': NlpGoogle
}

class NlpFactory:
    def __init__(self):
        pass

    @staticmethod
    def instance(kind=None):
        return services.get(kind, Nlp)()
