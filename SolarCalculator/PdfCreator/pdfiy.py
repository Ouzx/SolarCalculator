from fpdf import FPDF


class Pdfiy:
    def __init__(self, name):
        self.name = name
        self.pdf = FPDF()

    def create_pdf(self):
        self.pdf.add_page()
        self.pdf.image("source/export/pages/1.png", 0, 0, w=210, h=297)
        self.pdf.add_page()
        self.pdf.image("source/export/pages/2.png", 0, 0, w=210, h=297)
        self.pdf.add_page()
        self.pdf.image("source/export/pages/3.png", 0, 0, w=210, h=297)
        self.pdf.add_page()
        self.pdf.image("source/export/pages/4.png", 0, 0, w=210, h=297)

    def save_pdf(self):
        self.pdf.output('source/export/pdf/' + self.name + '.pdf', 'F')
