from PdfCreator.painter import Painter


class PageBuilder:
    def __init__(self, system_name, data):
        self.system_name = system_name
        self.data = data

        self.page_1()
        self.page_2()
        self.page_3()
        self.page_4()

    def page_1(self):
        print("Creating page 1...")

        canvas = Painter("source/pages/1.png")
        canvas.element_0(False, self.system_name)

        canvas.save()

    def page_2(self):
        print("Creating page 2...")

        canvas = Painter("source/pages/2.png")
        canvas.element_0(True, self.system_name)

        canvas.element_1(self.data["element_1"])
        canvas.element_2(self.data["element_2"])

        pos = [284, 2075]
        canvas.element_3("../"+self.data["element_3"]["monthly_average"], pos, 11)

        canvas.save()

    def page_3(self):
        print("Creating page 3...")

        canvas = Painter("source/pages/3.png")
        canvas.element_0(True, self.system_name)

        pos = [95, 598]
        canvas.element_4("../"+self.data["element_4"]["fotovoltaic_map"], pos, 21)

        pos = [290, 2156]
        canvas.element_3("../"+self.data["element_3"]["monthly_irradiation"], pos, 22)

        canvas.save()

    def page_4(self):
        print("Creating page 4...")

        canvas = Painter("source/pages/4.png")
        canvas.element_0(True, self.system_name)

        pos = [260, 610]
        canvas.element_4("../"+self.data["element_4"]["system_location_map"], pos, 31)
        canvas.element_5(self.data["project_details"], self.data["system_details"], self.data["project_cost"])

        canvas.save()
