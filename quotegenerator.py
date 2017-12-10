import json
import random
import os

class QuoteGenerator:

    def get_quote(self):
        dir = os.path.dirname(__file__)
        quotes = self.filter_quotes(json.load(open(os.path.join(dir,'data/quotes.json'),encoding='latin1')),150,15)
        quote = random.choice(quotes)
        return quote

    def filter_quotes(self,quotes,lenQ,lenA):
        _quotes = []
        for quote in quotes:
            lQ = quote['quoteText'].__len__()
            lA = quote['quoteAuthor'].__len__()
            if lQ <= lenQ and lA <= lenA:
                _quotes.append(quote)
        return _quotes