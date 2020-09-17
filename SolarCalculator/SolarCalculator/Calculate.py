from SolarCalculator.scripts.calculator import SolarPanelSystem


# project name: string
# custormer_information: dictionary -> {"Name": "Abdullah Kasım Günaydın", "MobilePhoneNumber": "05xxxxxxxxx"}
# annual_avg_consumption: float
# usage_area: float
# location_address: string, ascii characters -> "Ahiboz, Golbasi, Ankara" (town, district, city) or (district, city)
# setup_type: string -> "Düz Çatı Kurulumu" or "Eğimli Çatı Kurulumu" or "Arazi Kurulumu")
# energy_class: string -> "Mesken" or "Ticarethane" or "Sanayi" or "Tarımsal Sulama" or "Aydınlatma

def Calculate(project_name, customer_information, annual_avg_consumption, usage_area, location_address, setup_type,
              energy_class):
    setuptype_cvt = {
        "Düz Çatı Kurulumu": "medium",
        "Eğimli Çatı Kurulumu": "small",
        "Arazi Kurulumu": "ground"
    }

    energytype_cvt = {
        "Mesken": "Domicile",
        "Ticarethane": "Business",
        "Sanayi": "Industry",
        "Tarımsal Sulama": "AgrcltWatering",
        "Aydınlatma": "Lightning"
    }

    system = SolarPanelSystem(project_name, customer_information, annual_avg_consumption,
                              usage_area, location_address, setuptype_cvt[setup_type], energytype_cvt[energy_class])


