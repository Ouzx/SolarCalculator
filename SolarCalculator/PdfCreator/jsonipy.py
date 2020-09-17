import json

ex_data = {
    "info": {
        "system_name": "Test Ges Ankara",
        "location": "1232154.4464, 564654615.4652456"
    },
    "element_1": {
        "yearly_revenue": "$18.488,88",
        "pay_off_time": "4 Yıl",
        "investment_cost": "$69.904,40",
        "pay_off_percent": "%29,09"
    },
    "element_2": {
        "optimum_system_size": "110,0",
        "daily_electricity_usage": "782,8",
        "daily_electricity_production": "436,3",
        "yearly_energy_procution": "999.999,0"
    },
    "element_3": {
        "monthly_average": "source/element source/11.png",
        "monthly_irradiation": "source/element source/22.png"
    },
    "element_4": {
        "fotovoltaic_map": "source/element source/21.png",
        "system_location_map": "source/element source/31.png"
    },
    "project_details": {
        "location_text": "Ankara, Beypazarı",
        "yearly_consumption": "1460 kWh",
        "settlement_area": "20m\u00b2",
        "settlement_type": "Arazi Kurulumu",
        "energy_class": "Mesken Tipi",
        "system": "1600W Solar Enerji Sistemi"
    },
    "system_details": {
        "panel": "320W Solar Panel",
        "panel_count": "5 adet",
        "yearly_energy_production": "2351 kWh",
        "daily_energy_production": "163 kWh",
        "yearly_revenue": "116.000$",
        "pay_off_time": "12 yıl"
    },
    "project_cost": {
        "panel": {
            "name": "320W Solar Panel",
            "count": "5 adet"
        },
        "inverter": {
            "name": "GW2000-XS Smart",
            "count": "1 adet"
        },
        "construction": {
            "name": "Alüminyum(Arazi)",
            "count": "1 adet"
        },
        "control_panel": {
            "name": "Kontrol Panosu",
            "count": "3 adet"
        },
        "connector": {
            "name": "MC4 Branch Y",
            "count": "3 adet"
        },
        "solar_cable": {
            "name": "1x6 mm\u00b2",
            "count": "30 adet"
        },
        "ac_cable": {
            "name": "3x2.5mm\u00b2",
            "count": "1 adet"
        },
        "workmanship": {
            "name": "İşçilik"
        },
        "investment_cost": {
            "count": "$12.984"
        }
    }
}


def dict_to_json(path, data):
    with open("source/json/out.json", "w") as outfile:
        json.dump(data, outfile)


def json_to_dict(path):
    with open(path, encoding='utf8') as json_file:
        data = json.load(json_file)
        return data
