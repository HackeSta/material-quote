import materialgenerator
import quotegenerator
import twitter
import os

dir = os.path.dirname(__file__)
mg = materialgenerator.MaterialGenerator()
qg = quotegenerator.QuoteGenerator()
caption = "Material Quote of the Day #QOTD #MaterialDesign #Quotes #Quote"
quote = qg.get_quote()
image = mg.draw_image(quote['quoteText'], quote['quoteAuthor'], (4000, 4000))
image.save(os.path.join(dir,'image.png'),'PNG')
twitter.upload_status(caption,open(os.path.join(dir,'image.png'),'rb'))
