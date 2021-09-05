class Vehicle:
    default_ve = 'pa'
    def __init__(self,engine,tires):
        self.engine = engine
        self.tires =tires

    @classmethod
    def bicycle(cls,wheelnum , tires = None):
        if not tires:
            tires = [cls.default_ve , cls.default_ve]
        print('calling whell inside class method')
        cls.wheel(wheelnum)
        return cls(None , tires)
    
    @staticmethod
    def wheel(radius):
        
        print(2*1.45*radius)


v = Vehicle('4 cycle' , None)
bike = v.bicycle(1)
print(bike.tires)


v.wheel(12)
Vehicle.wheel(1)
