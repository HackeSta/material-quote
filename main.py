import materialgenerator
import quotegenerator
import twitter
import facebook
import instagram
import os

dir = os.path.dirname(__file__)
mg = materialgenerator.MaterialGenerator()
qg = quotegenerator.QuoteGenerator()
caption = "Material Quote of the Day #QOTD #MaterialDesign #Quotes #quote #love #life #success #today #inspiration #quoteoftheday #change #motivation #image #lol #leadership"
quote = qg.get_quote()
image = mg.draw_image(quote['quoteText'], quote['quoteAuthor'], (4000, 4000))
image.save(os.path.join(dir,'image.jpg'),'JPEG')
twitter.upload_status(caption,open(os.path.join(dir,'image.jpg'),'rb'))
facebook.upload_status(caption,os.path.join(dir,'image.jpg'))
instagram.upload_image(caption,os.path.join(dir,'image.jpg'))
