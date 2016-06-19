class Klima:
    TempData=[1] #Eigenschaften
    HumyData=[1] #Eigenschaften
    Temp=[1]
    i=0
    def add_Temp(self,wert):
        self.Temp[0] = wert
        self.TempData += self.Temp
    def add_Humy(self,wert):
        self.Temp[0] = wert
        self.HumyData += self.Temp
    def ausgabe(self):
        print(self.TempData, self.HumyData)
    def get_Temp(self):
        return self.TempData
    def get_Humy(self):
        return self.HumyData

Buro=Klima()
Buro.ausgabe()
Buro.add_Temp(23.1)
Buro.add_Humy(45)
Buro.ausgabe()
Buro.add_Temp(26.2)
Buro.add_Humy(43)
Buro.ausgabe()
Data= Buro.get_Temp()
print(Data)
Data= Buro.get_Humy()
print(Data)
    
