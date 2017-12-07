from PIL import Image, ImageDraw, ImageFont
import materialcolors as colors
import textwrap
import os

class MaterialGenerator:


    def draw_image(self, text,author, size):
        COPYRIGHT_TEXT = "@MaterialQOTD"
        dir = os.path.dirname(__file__)
        im = Image.new('RGB', size)  # create the image
        draw = ImageDraw.Draw(im)  # create a drawing object that is
        # used to draw on the new image
        # Now, we'll do the drawing:
        draw.rectangle(((0,0),size), fill=colors.get_random_color()) #fill the background with random material color
        font = ImageFont.truetype(os.path.join(dir,'fonts/OpenSans-Regular.ttf'),320)  #material font
        lines = textwrap.wrap(text, 25) #wraps text to 25 letters
        if author != "":        # add author details only if present
            lines.append(' ')
            lines.append('- ' + author)
        line_dimensions = [draw.textsize(line, font=font) for line in lines]
        offset = (size[1] - sum(h for w, h in line_dimensions)) // 2
        for line in lines:
            w,h = draw.textsize(line,font=font)
            pos = ((size[0] - w)/2, offset)
            draw.text(pos, line, font=font, fill=(255,255,255))
            offset += font.getsize(line)[1]


        #draw copyright
        font = ImageFont.truetype(os.path.join(dir,'fonts/OpenSans-Regular.ttf'),220)

        w, h = draw.textsize(COPYRIGHT_TEXT, font=font)
        pos = ((size[0] - w) / 2, size[1] - h)
        draw.text(pos, COPYRIGHT_TEXT, font=font, fill=(255, 255, 255))

        del draw  # I'm done drawing so I don't need this anymore


        return im
