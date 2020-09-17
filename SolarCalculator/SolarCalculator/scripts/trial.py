from SolarCalculator.scripts.calculator import SolarPanelSystem


# solar = SolarPanelSystem(4*365, 20, ("Ankara", "Beypazarı"), "Arazi Kurulumu", "Domicile")
solar = SolarPanelSystem("Test Ges Ankara", ("Abdullah_Kasım_Günaydın", "05052053320"), 5*365, 20, "Ahiboz, Golbasi, Ankara", "small", "Business")

# print("Yıllık Tüketimi:", str(4*365), "kWh")
# print("Kurulum Alanı:", "20 m^2")
# print("Lokasyon:", "Ankara, Beypazarı")
# print("Kurulum Tipi:", "Arazi Kurulumu")
# print("Enerji Sınıflandırması:", "Mesken Tipi")
#
# print("\nSistem Tanımı   :\t", solar.SystemPower, "W Solar Enerji Sistemi")
#
# print("Panel\t\t\t:\t", solar.PanelType, "\t\t\t\t\t\t\t", solar.EnergyPrice, "$\t\t", solar.PanelNumber, "adet")
#
# print("Inverter\t\t:\t", solar.InverterModel, "\t\t\t\t\t", solar.InverterPrice, "$\t\t", solar.InverterNumber, "adet")
#
# print("Konstrüksiyon\t:\t", solar.ConstructionModel, "\t", solar.ConstructionPrice, "$\t\t", solar.ConstructionNumber, "adet")
#
# print("Kontrol Panosu\t:\t", solar.ControlBoardModel, "\t\t\t\t\t\t\t", solar.ControlBoardPrice, "$\t\t", solar.ControlBoardNumber, "adet")
#
# print("Konnektör\t\t:\t", solar.ConnectorModel, "\t\t\t", solar.ConnectorPrice, "$\t\t", solar.ConnectorNumber, "adet")
#
# print("Solar Kablo\t\t:\t", solar.SolarCableModel, "\t\t", solar.SolarCablePrice, "$\t\t", solar.SolarCableNumber, "adet")
#
# print("AC Kablo\t\t:\t", solar.ACCableModel, "\t\t\t\t\t\t\t", solar.ACCablePrice, "$\t\t", solar.ACCableNumber, "adet")
#
# print("İşçilik\t\t\t:\t\t\t\t\t\t\t\t\t\t\t\t", solar.LaborPrice, "$")
#
# print("\nYatırım Maliyeti\t\t : ", solar.TotalPrice, "₺")
# print("Yatırım Maliyeti(KDV%18) : ", int(solar.TotalPrice * 1.18), "₺")
# print("Yıllık Enerji Üretimi\t : ", solar.AnnualEnergyGeneration, "kWh")
# print("Yıllık Kazanç\t\t\t : ", solar.AnnualEarning, "  ₺")
# print("Kendini Tamamlama Süresi : ", solar.ReturnTime, "yıl")