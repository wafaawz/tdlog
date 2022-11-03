class Weapon:
    def __init__(self,ammunitions, range):
        self._ammunitions=ammunitions
        self._range=range
    def fire_at(self,x,y,z):
        print( "the weapon will fire at ",(x,y,z))
        
class LMAS(Weapon):
    def __init__(self):
        Weapon.__init__(self,40,30)
    def fire_at(self,x,y,z):
        if self._ammunitions==0:
            print('NoAmmunitionError')
        elif z!=0:
            self._ammunitions-=1
            print("OutofRangeError")
        else:
            print("The Lance-missiles antisurface will fire at",(x,y,z))
            
class LMAA(Weapon):
    def __init__(self):
        Weapon.__init__(self,50,40)
    def fire_at(self,x,y,z):
        if self._ammunitions==0:
            print('NoAmmunitionError')
        elif z<=0:
            self._ammunitions-=1
            print("OutofRangeError")
        else:
            print("The Lance-missiles anti-air will fire at",(x,y,z))
            
class LT(Weapon):
    def __init__(self):
        Weapon.__init__(self,15,20)
    def fire_at(self,x,y,z):
        if self._ammunitions==0:
            print('NoAmmunitionError')
        elif z>0:
            self._ammunitions-=1
            print("OutofRangeError")
        else:
            print("The Lance-torpilles will fire at",(x,y,z))
            
