import materialgenerator
import quotegenerator
import os

dir = os.path.dirname(__file__)
mg = materialgenerator.MaterialGenerator()
qg = quotegenerator.QuoteGenerator()
quote = qg.get_quote()
image = mg.draw_image(quote['quoteText'], quote['quoteAuthor'], (4000, 4000))
image.save(os.path.join(dir,'data/mqotd_image.jpg'), 'JPEG')
