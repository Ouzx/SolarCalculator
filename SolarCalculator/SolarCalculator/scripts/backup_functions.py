import json
import os
## source files

with open("../SolarCalculator/scripts/sources/PriceSource.json", "r") as priceSrcFile:
    PriceData = json.load(priceSrcFile)





# loc = Location(("Ankara", "Beypazarı"))



### SYSTEM DEFINITION
def getSystemDefinition(average, location):
    minSunbath = location.getAvgEnergyGen()
    daily = average * 1000 / 365

    # round to hundred
    return round(daily / minSunbath, -2)




### ITEM ANALYISE
def getPanelAnalyise(systempower, Area):
    paneltype = "320W Solar Panel"

    panelnumber = int(systempower / 320) + 1
    while panelnumber * 2 > Area:
        panelnumber -= 1

    energyprice = int(PriceData["PanelEnergyPrice"] * 320 * panelnumber)

    newsystempower = panelnumber * 320

    return paneltype, energyprice, panelnumber, newsystempower


def getInverterAnalyise(systempower):
    inverters = []

    for inverter in PriceData["InverterCatalog"]:
        if inverter["power"] >= systempower and len(inverters) > 0:
            if inverter["power"] == inverters[0]["power"]:
                inverters.append(inverter)
        if inverter["power"] >= systempower and len(inverters) == 0:
            inverters.append(inverter)


    inv = None
    temp = inverters[0]["price"]
    for inverter in inverters:
        if inverter["price"] <= temp:
            inv = inverter
            temp = inverter["price"]


    invnumber = 1


    return inv["model"], inv["price"], invnumber


def getConstructionAnalyise(panelnumber, setuptype):
    model = "Alüminyum " + setuptype + " Konstrüksiyonu"

    price = panelnumber * PriceData["ConstructionUPrice"]

    consnumber = 1

    return model, price, consnumber



def getControlBoardAnalyise():
    return "Kontrol Panosu", PriceData["ControlBoard"], 1



def getConnectorAnalyise():
    return "MC4 Branch Y Bağlantı Konnektörü", PriceData["Y_ConnectorUPrice"] * 5, 5


def getSolarCableAnalyise():
    return "1x6mm2 Solar Kablo (Siyah & Kırmızı)", PriceData["SolarCablePrice"] * 30, 30


def getACCableAnalyise():
    return "3x2.5mm2 AC Kablo", PriceData["ACCablePrice"] * 1, 1


def getLaborAnalyise(total):
    return "İşçilik", round(PriceData["LaborPercentage"] * total, 1), 1


def getGeneralAnalyise(object):
    object.Inventory = {
        "panel": {
            "cost": object.EnergyPrice
        },
        "inverter": {
            "cost": object.InverterPrice
        },

        "construction": {
            "cost": object.ConstructionPrice
        },

        "controlboard": {
            "cost": object.ControlBoardPrice
        },

        "connector": {
            "cost": object.ConnectorPrice
        },

        "solarcable": {
            "cost": object.SolarCablePrice
        },

        "accable": {
            "cost": object.ACCablePrice
        },

        "labor": {
            "cost": object.LaborPrice
        }
    }


# OUTPUT FUNCTIONS
def getTotalPrice(inventory):
    # return int(sum(list(inventory.values()["cost"])) * PriceData["Dollar"])
    sum = 0
    for item in inventory:
        sum += inventory[item]["cost"]

    return int(sum * PriceData["Dollar"])

def getAnnualEnergyGeneration(location, energytype, systempower):
    loc = location

    return round(loc.getAverageGenerationPerYear() * systempower / 1000, 0), \
           int(loc.getAverageGenerationPerYear() * PriceData["EnergyPrice"][energytype])



def getReturnTime(total, annual):
    return round(total / annual, 1)