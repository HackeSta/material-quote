import materialgenerator
import quotegenerator
import twitter
import facebook
import instagram
import os

dir = os.path.dirname(__file__)
mg = materialgenerator.MaterialGenerator()
qg = quotegenerator.QuoteGenerator()
caption = "Material Quote of the Day"
twitter_tags = " #QOTD #MaterialDesign #Quotes #quote #love #life #success #today #inspiration #quoteoftheday #change #motivation #image #lol #leadership"
instagram_tags = " #QOTD #quote #quotes #comment #comments #TagsForLikes #TFLers #tweegram #quoteoftheday #song #funny #life #instagood #love #photooftheday #igers #instagramhub #tbt #instadaily #true #instamood #nofilter #word #material #materialdesign"
quote = qg.get_quote()
image = mg.draw_image(quote['quoteText'], quote['quoteAuthor'], (4000, 4000))
image.save(os.path.join(dir,'image.jpg'),'JPEG')
twitter.upload_status(caption + twitter_tags,open(os.path.join(dir,'image.jpg'),'rb'))
facebook.upload_status(caption,os.path.join(dir,'image.jpg'))
instagram.upload_image(caption + instagram_tags,os.path.join(dir,'image.jpg'))
