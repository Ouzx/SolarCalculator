from SolarCalculator.scripts import backup_functions as back
import json
import os

with open("../SolarCalculator/output_data/out.json", "r") as draft_output_file:
    draft_output = json.load(draft_output_file)


class Location:
    def __init__(self, address, setuptype):
        self.loc = address.lower().split(" ")
        # print(self.loc)
        (self.annaulGeneration, self.pathmap, self.pathave0,
                self.pathave1, self.pathturkey) = self.getSolarData(self.loc, setuptype)


    def getSolarData(self, address, setuptype):
        print(os.getcwd())
        base = "location_db/"
        os.chdir("../")
        dirs = os.listdir(base)
        for dir in dirs:
            if address[1] in dir:
                sbase = base + dir + "/"
                sdirs = os.listdir(sbase)
                for sdir in sdirs:
                    imgmap = sbase + "map.jpg"
                    if address[0] in sdir:
                        # print("yes")
                        ssbase = sbase + sdir + "/" + setuptype + "/"

                        pathann = ssbase + "annualgen.txt"
                        with open(pathann, "r") as annfile:
                            global anngen
                            anngen = round(float(annfile.read()), 2)
                            anngen = round(anngen / 100, 2) if setuptype == "medium" else anngen

                        imgave0 = ssbase + "ave0.jpg"
                        imgave1 = ssbase + "ave1.jpg"
                        imgfoto = base + "turkiye_fotovoltaik.png"

                        return (anngen, imgmap, imgave0, imgave1, imgfoto)



    def getMinEnergyGen(self):
        return 3

    def getAvgEnergyGen(self):
        return round(self.annaulGeneration / 365, 2)

    def getAverageGenerationPerYear(self):
        return self.annaulGeneration


class SolarPanelSystem:
    OUTPUT = []

    ProjectName = None
    CustomerInfo = None

    # system
    SystemPower = 0
    SetupType = None

    # items
    PanelType = None
    InverterModel = None
    ConstructionModel = None
    ControlBoardModel = None
    ConnectorModel = None
    SolarCableModel = None
    ACCableModel = None
    LaborModel = None

    EnergyPrice = 0
    InverterPrice = 0
    ConstructionPrice = 0
    ControlBoardPrice = 0
    ConnectorPrice = 0
    SolarCablePrice = 0
    ACCablePrice = 0
    LaborPrice = 0

    PanelNumber = 0
    InverterNumber = 0
    ConstructionNumber = 0
    ControlBoardNumber = 0
    ConnectorNumber = 0
    SolarCableNumber = 0
    ACCableNumber = 0
    LaborNumber = 0


    # outputs
    TotalPrice = 0
    AnnualEarning = 0
    AnnualEnergyGeneration = 0
    ReturnTime = 0



    # AnnualAverageConsumption(kWh), Area(m^2), Location(city, district, town, etc.),
    # SetupType(small_residential, medium_size_comercial, ground_mounted_largescale, floating_largescale
    # EnergyType(homeelectric, workelectric, fieldelectric, etc.)
    def __init__(self, ProjectName, CustomerInfo,AnnAvgCons, Area, Location_, SetupType, EnergyType):
        self.Location = Location(Location_, SetupType)
        self.ProjectName = ProjectName
        self.CustomerInfo = CustomerInfo

        self.Inventory = None

        self.calculateSystemDefinition(AnnAvgCons)

        self.analyiseItems(Area, SetupType)

        self.prepareOutputs(AnnAvgCons, Area, SetupType, EnergyType)




    # system W
    def calculateSystemDefinition(self, AnnAvgCons):
        self.SystemPower = back.getSystemDefinition(AnnAvgCons, self.Location)





    # panel, inverter, construction, controlboard, connector, solarcable
    # ACcable, labors
    def analyiseItems(self, Area, SetupType):
        self.PanelType, self.EnergyPrice, self.PanelNumber, self.SystemPower = back.getPanelAnalyise(self.SystemPower, Area)

        self.InverterModel, self.InverterPrice, self.InverterNumber = back.getInverterAnalyise(self.SystemPower)

        self.ConstructionModel, self.ConstructionPrice, self.ConstructionNumber = back.getConstructionAnalyise(self.PanelNumber, SetupType)

        self.ControlBoardModel, self.ControlBoardPrice, self.ControlBoardNumber = back.getControlBoardAnalyise()

        self.ConnectorModel, self.ConnectorPrice, self.ConnectorNumber = back.getConnectorAnalyise()

        self.SolarCableModel, self.SolarCablePrice, self.SolarCableNumber = back.getSolarCableAnalyise()

        self.ACCableModel, self.ACCablePrice, self.ACCableNumber = back.getACCableAnalyise()

        total = self.ACCablePrice + self.EnergyPrice + self.InverterPrice + self.ConstructionPrice + \
                self.ControlBoardPrice + self.ConnectorPrice + self.SolarCablePrice

        self.LaborModel, self.LaborPrice, self.LaborNumber = back.getLaborAnalyise(total)

        ## take item, price, quantity dictionaries
        back.getGeneralAnalyise(self)


    # totalprice, annualearning, annualenergygeneration, returntime
    def prepareOutputs(self, EnergyCons, Area, SetupType, EnergyType):
        self.TotalPrice = back.getTotalPrice(self.Inventory)
        self.AnnualEnergyGeneration, self.AnnualEarning = back.getAnnualEnergyGeneration(self.Location, EnergyType, self.SystemPower)
        self.ReturnTime = back.getReturnTime(self.TotalPrice, self.AnnualEarning)


        draft_output["info"]["system_name"] = self.ProjectName

        draft_output["element_1"]["yearly_revenue"] = "₺" + str(self.AnnualEarning)
        draft_output["element_1"]["pay_off_time"] = str(self.ReturnTime) + " Yıl"
        draft_output["element_1"]["investment_cost"] = "₺" + str(self.TotalPrice)
        draft_output["element_1"]["pay_off_percent"] = "%" + str(round(100 * self.AnnualEarning / self.TotalPrice, 2))

        draft_output["element_2"]["optimum_system_size"] = str(self.SystemPower)
        draft_output["element_2"]["daily_electric_usage"] = str(round(EnergyCons / 365, 2))
        draft_output["element_2"]["daily_electric_production"] = str(round(self.AnnualEnergyGeneration / 365, 0))
        draft_output["element_2"]["yearly_energy_production"] = str(self.AnnualEnergyGeneration)

        draft_output["element_3"]["monthly_average"] = self.Location.pathave0
        draft_output["element_3"]["monthly_irradiation"] = self.Location.pathave1

        draft_output["element_4"]["fotovoltaic_map"] = self.Location.pathturkey
        draft_output["element_4"]["system_location_map"] = self.Location.pathmap

        draft_output["project_details"]["location_text"] = self.Location.loc
        draft_output["project_details"]["yearly_consumption"] = str(EnergyCons) + " kWh"
        draft_output["project_details"]["settlement_area"] = str(Area) + "m\x5e2"
        draft_output["project_details"]["settlement_type"] = SetupType
        draft_output["project_details"]["energy_class"] = EnergyType
        draft_output["project_details"]["system"] = str(self.SystemPower) + "W Solar Enerji Sistemi"

        draft_output["system_details"]["panel"] = self.PanelType
        draft_output["system_details"]["panel_count"] = str(self.PanelNumber)
        draft_output["system_details"]["yearly_energy_production"] = str(self.AnnualEnergyGeneration) + " kWp"
        draft_output["system_details"]["daily_energy_production"] = str(int(self.AnnualEnergyGeneration / 365)) + " kWp"
        draft_output["system_details"]["yearly_revenue"] = str(self.AnnualEarning) + "₺"
        draft_output["system_details"]["pay_off_time"] = str(self.ReturnTime) + " Yıl"

        draft_output["project_cost"]["panel"]["name"] = self.PanelType
        draft_output["project_cost"]["panel"]["count"] = str(self.PanelNumber)
        draft_output["project_cost"]["inverter"]["name"] = self.InverterModel
        draft_output["project_cost"]["inverter"]["count"] = str(self.InverterNumber)
        draft_output["project_cost"]["construction"]["name"] = self.ConstructionModel
        draft_output["project_cost"]["construction"]["count"] = str(self.ConstructionNumber)
        draft_output["project_cost"]["control_panel"]["name"] = self.ControlBoardModel
        draft_output["project_cost"]["control_panel"]["count"] = str(self.ControlBoardNumber)
        draft_output["project_cost"]["connector"]["name"] = self.ConnectorModel
        draft_output["project_cost"]["connector"]["count"] = str(self.ConnectorNumber)
        draft_output["project_cost"]["solar_cable"]["name"] = self.SolarCableModel
        draft_output["project_cost"]["solar_cable"]["count"] = str(self.SolarCableNumber)
        draft_output["project_cost"]["ac_cable"]["name"] = self.ACCableModel
        draft_output["project_cost"]["ac_cable"]["count"] = str(self.ACCableNumber)
        draft_output["project_cost"]["investment_cost"]["count"] = str(self.TotalPrice)

        # print(os.getcwd())
        with open("SolarCalculator/output_data/output.json", "w", encoding='utf8') as outputFile:
            json.dump(draft_output, outputFile, ensure_ascii=False)


