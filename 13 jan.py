class vehicle():
    def __init__(self,type,id):
        self.type = type
        self.id = id

class car(vehicle):
    def __init__(self, type, id, brandname, year, model, numberofseats):
        vehicle.__init__(self,type,id)
        self.brandname = brandname
        self.year = year
        self.model = model
        self.numberofseats = numberofseats

    def saveToFile(self):
        file = open("commands.txt", "w")
        file.write(self.id,"-",self.type,"-",self.brandname,"-",self.model,"-",self.year,"-",self.numebrofseats)


class bike(vehicle):
    def __init__(self, type, id, brandname, year, model, numberofseats,modelB,brandnameB):
        bike.__init__(self,type,id)
        self.brandnameB = brandnameB
        self.modelB = modelB


    def saveToFile(self):
        file = open("commands.txt", "w")
        file.write(self.id,"-", self.type,"-",self.brandnameB,"-",self.modelB)


class bus(vehicle):
    def __init__(self, type, id, brandname, year, model, numberofseats,modelB,brandnameB,numberofSeats, numberOfWheels):
        bus.__init__(self,type,id)
        self.numberofSeats = numberofSeats
        self.numberOfWheels = numberOfWheels


    def saveToFile(self):
        file = open("commands.txt", "w")
        file.write(self.id,"-", self.type,"-",self.numberofSeats,"-",self.numberOfWheels)



#vehicle class

# type
# id

#car->vehicle
#brandname, year, model, numberofseats
#cars.txt -> store all car infos -> id-type-brandname-model-year-numebrofseats

#bike->vehicle
#model,brandname
#bikes.txt ->store all bike infos  ->id-type-brandname-model


#bus->vehicle
#numberofSeats, numberOfWheels
#buses.txt -> id-type-numberofseats,numberofwheels
