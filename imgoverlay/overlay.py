from PIL import Image, ImageDraw, ImageFont, ImageColor

class ImageOverlay:
    image_file = None

    TEXT_COLOURS = {
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0,255,0),
        'white': (255,255,255) }
    
    text_colour = 'black'
    text_size = 72
    
    def __init__(self, image_file):
        self.image_file = image_file[0]

    def set_text_colour(self, set_text_colour):
        if set_text_colour:
            self.text_colour=set_text_colour

    def set_style(self, text_size, set_text_colour=None):
        if set_text_colour:
            self.text_colour=set_text_colour


    def overlay_text(self, text):
        print('Image file: %s' % self.image_file)
        with Image.open(self.image_file) as image:
            image_draw = ImageDraw.Draw(image)
            image_font = ImageFont.truetype('HelveticaNeue.ttc', self.text_size)
            print('<%s>' % text)
            image_draw.text((150,100), text[0], self.TEXT_COLOURS[self.text_colour], font=image_font)

            extn_loc = self.image_file.rfind('.')
            output_file_name = self.image_file[:extn_loc] + '_overlay' + self.image_file[extn_loc:]

            image.save(output_file_name)
