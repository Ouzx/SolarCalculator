from PdfCreator.pagebuilder import PageBuilder
from PdfCreator import jsonipy
from PdfCreator import pdfiy
import sys
import os
from SolarCalculator import Calculate


project_name = sys.argv[1]
customer_information = {"Name": sys.argv[2], "MobilePhoneNumber": sys.argv[3]}
annual_avg_consumption = sys.argv[4]
usage_area = sys.argv[5]
location_address = sys.argv[6]
setup_type = sys.argv[7]
energy_class = sys.argv[8]
"""
project_name = "Testing"
customer_information = {"Name": "Abdullah Kasım Günaydın", "MobilePhoneNumber": "05xxxxxxxxx"}
annual_avg_consumption = 1840
usage_area = 20
location_address = "Gölbaşı Ankara"
setup_type = "Düz Çatı Kurulumu"
energy_class = "Ticarethane"
"""

def main():
    Calculate.Calculate(project_name, customer_information, annual_avg_consumption, usage_area, location_address,
                        setup_type, energy_class)

    os.chdir("PdfCreator")
    data = jsonipy.json_to_dict("../SolarCalculator/output_data/output.json")
    PageBuilder(project_name, data)
    pdf = pdfiy.Pdfiy(project_name)
    pdf.create_pdf()
    pdf.save_pdf()

main()
