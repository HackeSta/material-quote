import json
import random
import os

class QuoteGenerator:

    def get_quote(self):
        dir = os.path.dirname(__file__)
        quotes = json.load(open(os.path.join(dir,'data/quotes.json'),encoding='latin1'))
        quote = random.choice(quotes)
        return quote

