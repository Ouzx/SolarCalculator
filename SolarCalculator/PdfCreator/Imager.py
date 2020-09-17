from PIL import Image


class Imager:
    def __init__(self, img_path, img_type):
        self.path = img_path
        self.stretched = self.stretch(img_type, self.crop())

    def get_image(self):
        return self.stretched

    def crop(self):
        orj = Image.open(self.path)
        left = 11
        top = 18
        right = 577
        bottom = 232
        return orj.crop((left, top, right, bottom))

    def stretch(self, img_type, img):
        if img_type == 11:
            return img.resize((1958, 740), Image.ANTIALIAS)
        elif img_type == 22:
            return img.resize((1945, 732), Image.ANTIALIAS)

        """ # maps
        elif img_type == 21:
            pass
        elif img_type == 31:
            pass
        """
