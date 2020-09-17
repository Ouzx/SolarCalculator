from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
from PdfCreator.Imager import Imager


class Painter:
    def __init__(self, filename='01.png'):
        self.width = 2480
        self.height = 3508
        self.img = Image.open(filename)

        self.draw = ImageDraw.Draw(self.img)

    def show_img(self):
        self.img.show()

    def save(self):
        file_name = ("source/export/pages/" + os.path.basename(self.img.filename))
        self.img.save(file_name)
        print("Page saved to: " + file_name)

    def grid_system(self, x):
        img = Image.open(self.img.filename)
        draw = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('arial', 15)
        counter_i = 0
        counter_j = 0

        for i in range(0, img.size[0], x):
            draw.text((i, 0), str(counter_i), (0, 0, 0), fnt)
            counter_i += 1

            draw.line(((i, 0), (i, img.size[1] - 1)), fill="red", width=0)

        for j in range(0, img.size[1], x):
            draw.text((0, j), str(counter_j), (0, 0, 0), fnt)
            counter_j += 1

            draw.line((((img.size[0] - 1), j), (0, j)), fill="red", width=0)

        img.save(img.filename + '_' + str(x) + '_grid.png')

    @staticmethod
    def calc_deflection(pos, size):
        temp = [0, 0]
        temp[0] = pos[0] - (5 / 215 * size)
        temp[1] = pos[1] - (5 / 27 * size)
        return temp

    @staticmethod
    def calc_pt(size):
        # [ps] pt to [py] pt
        return size * 130 / 31

    @staticmethod
    def right_align(pos, size):
        temp = [0, 0]
        temp[0] = pos[0] - size[0]
        # temp[1] = pos[1] - size[1]
        temp[1] = pos[1]
        return temp

    @staticmethod
    def mid_align(pos, size):
        temp = [0, 0]
        temp[0] = pos[0] - (size[0] / 2)
        # temp[1] = pos[1] - (size[1] / 2)
        temp[1] = pos[1]
        return temp

    @staticmethod
    def make_transparent(path):
        img = Image.open(path)
        img = img.convert("RGBA")
        data = img.getdata()

        new_data = []
        for item in data:
            if item[0] == 228 and item[1] == 228 and item[2] == 228 \
                    or item[0] == 255 and item[1] == 255 and item[2] == 255:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        return img

    @staticmethod
    def make_transparent(img):
        data = img.getdata()

        new_data = []
        for item in data:
            if item[0] == 228 and item[1] == 228 and item[2] == 228 \
                    or item[0] == 255 and item[1] == 255 and item[2] == 255:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        return img

    def place_text(self, position, text, pt, is_bold, align='', color=(255, 255, 255)):
        size = int(self.calc_pt(pt))

        fnt = ImageFont.truetype("source/fonts/arial.ttf", size=size, encoding="utf-8")
        if is_bold:
            fnt = ImageFont.truetype("source/fonts/arial_bold.tf", size=size, encoding="utf-8")

        pos = self.calc_deflection(position, size)
        if align == 'right':
            pos = self.right_align(pos, self.draw.textsize(text, fnt))
        elif align == 'mid':
            pos = self.mid_align(pos, self.draw.textsize(text, fnt))

        self.draw.text(pos, text, color, fnt)

    def place_image(self, pos, path, is_graph, img_type):
        if is_graph:
            # img = self.make_transparent(path)
            # img = self.make_transparent(Imager(path, img_type).get_image().convert("RGBA"))
            img = Imager(path, img_type).get_image().convert("RGBA")
            self.img.paste(img, pos, img)

        else:
            img = Image.open(path)
            self.img.paste(img, pos)

    def element_0(self, is_header, system_name):
        print("Placing element0...")
        if is_header:
            pos = [2280, 209]
            self.place_text(pos, system_name, 8, False, 'right')

            pos = [2280, 249]
            dt = datetime.now()
            self.place_text(pos, dt.strftime("%x"), 8, False, 'right')

        else:
            pos = [1200, 2850]
            self.place_text(pos, system_name, 30, False)

            pos = [1200, 3030]
            dt = datetime.now()
            self.place_text(pos, dt.strftime("%x"), 30, False)
        print("element0 placed.")

    def element_1(self, element_1_data):
        print("Placing element1...")

        pos = [370, 852]
        self.place_text(pos, element_1_data["yearly_revenue"], 15, False, 'mid', (35, 45, 58))

        pos = [950, 852]
        self.place_text(pos, element_1_data["pay_off_time"], 15, False, 'mid', (35, 45, 58))

        pos = [1530, 852]
        self.place_text(pos, element_1_data["investment_cost"], 15, False, 'mid', (35, 45, 58))

        pos = [2100, 852]
        self.place_text(pos, element_1_data["pay_off_percent"], 15, False, 'mid', (35, 45, 58))

        print("element1 placed.")

    def element_2(self, element_2_data):
        print("Placing element2...")

        pos = [350, 1197]
        self.place_text(pos, element_2_data["optimum_system_size"], 15, False, 'mid')

        pos = [940, 1197]
        self.place_text(pos, element_2_data["daily_electric_usage"], 15, False, 'mid')

        pos = [1530, 1197]
        self.place_text(pos, element_2_data["daily_electric_production"], 15, False, 'mid')

        pos = [2120, 1197]
        self.place_text(pos, element_2_data["yearly_energy_production"], 15, False, 'mid')

        print("element2 placed.")

    def element_3(self, element_3_data, pos, img_type):
        print("Placing element3...")

        self.place_image(pos, element_3_data, True, img_type)

        print("element3 placed.")

    def element_4(self, element_4_data, pos, img_type):
        print("Placing element4...")

        self.place_image(pos, element_4_data, False, img_type)

        print("element4 placed.")

    def element_5(self, element_5_data, element_6_data, element_7_data):
        print("Placing element5...")

        print("Printing project details")
        pos = [1177, 1872]
        self.place_text(pos, element_5_data["location_text"][0] + ", " + element_5_data["location_text"][1], 8, True,
                        'right', (0, 0, 0))

        pos = [1177, 1942]
        self.place_text(pos, element_5_data["yearly_consumption"], 8, True, 'right', (0, 0, 0))

        pos = [1177, 2007]
        self.place_text(pos, element_5_data["settlement_area"], 8, True, 'right', (0, 0, 0))

        pos = [1177, 2077]
        self.place_text(pos, element_5_data["settlement_type"], 8, True, 'right', (0, 0, 0))

        pos = [1177, 2142]
        self.place_text(pos, element_5_data["energy_class"], 8, True, 'right', (0, 0, 0))

        pos = [1177, 2207]
        self.place_text(pos, element_5_data["system"], 8, True, 'right', (0, 0, 0))

        print("Printing System details")
        pos = [2143, 1872]
        self.place_text(pos, element_6_data["panel"], 8, True, 'right', (0, 0, 0))

        pos = [2143, 1942]
        self.place_text(pos, element_6_data["panel_count"], 8, True, 'right', (0, 0, 0))

        pos = [2143, 2007]
        self.place_text(pos, element_6_data["yearly_energy_production"], 8, True, 'right', (0, 0, 0))

        pos = [2143, 2077]
        self.place_text(pos, element_6_data["daily_energy_production"], 8, True, 'right', (0, 0, 0))

        pos = [2143, 2142]
        self.place_text(pos, element_6_data["yearly_revenue"], 8, True, 'right', (0, 0, 0))

        pos = [2143, 2207]
        self.place_text(pos, element_6_data["pay_off_time"], 8, True, 'right', (0, 0, 0))

        print("Printing Project Cost Names ")
        pos = [1290, 2457]
        self.place_text(pos, element_7_data["panel"]["name"], 8, True, 'mid', (0, 0, 0))

        pos = [1290, 2522]
        self.place_text(pos, element_7_data["inverter"]["name"], 8, True, 'mid', (0, 0, 0))

        pos = [1290, 2587]
        self.place_text(pos, element_7_data["construction"]["name"], 8, True, 'mid', (0, 0, 0))

        pos = [1290, 2652]
        self.place_text(pos, element_7_data["control_panel"]["name"], 8, True, 'mid', (0, 0, 0))

        pos = [1290, 2717]
        self.place_text(pos, element_7_data["connector"]["name"], 8, True, 'mid', (0, 0, 0))

        pos = [1290, 2782]
        self.place_text(pos, element_7_data["solar_cable"]["name"], 8, True, 'mid', (0, 0, 0))

        pos = [1290, 2849]
        self.place_text(pos, element_7_data["ac_cable"]["name"], 8, True, 'mid', (0, 0, 0))

        print("Printing Project Cost Counts ")
        pos = [1820, 2457]
        self.place_text(pos, element_7_data["panel"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2522]
        self.place_text(pos, element_7_data["inverter"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2587]
        self.place_text(pos, element_7_data["construction"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2652]
        self.place_text(pos, element_7_data["control_panel"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2717]
        self.place_text(pos, element_7_data["connector"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2782]
        self.place_text(pos, element_7_data["solar_cable"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2849]
        self.place_text(pos, element_7_data["ac_cable"]["count"], 8, True, 'right', (0, 0, 0))

        pos = [1820, 2983]
        self.place_text(pos, element_7_data["investment_cost"]["count"], 8, True, 'right', (0, 0, 0))

        print("element5 placed.")
