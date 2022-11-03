
from weapon import Weapon
from weapon import LMAA
from weapon import LMAS
from weapon import LT

class Vessel:
    def __init__(self,coordinates,max_hits,weapon):
        self._coordinates=coordinates
        self._max_hits=max_hits
        self._weapon=weapon
    def go_to(self,x,y,z):
        self._coordinates=(x,y,z)
    def get_coordinates(self):
        return(self._coordinates)
    def fire_at(self,x,y,z):
        print("The Vessel will fire at",(x,y,z))
        
lmaa=LMAA()
lmas=LMAS()
lmas1=LMAS()
ltt=LT()
ltt1=LT()

        
class Cruiser(Vessel):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),6,lmaa)
    def go_to(self,x,y,z):
        if z!=0:
            print("The Cruiser can not reach this position")
        else :
            Vessel.go_to(self,x,y,z)
    def fire_at(self,x,y,z):
        a=self.get_coordinates()
        b=lmaa._range
        if self._max_hits==0:
            print("DestroyedError")
        if ((a[0]-x)**2+(a[1]-y)**2+(a[2]-z)**2)**(1/2)>b:
            print("OutOfRangeError")
            lmaa._ammunitions-=1
  
class Submarine(Vessel):
    def __init__(self,x,y,z):
        Vessel.__init__(self,(x,y,z),2,ltt)
    def go_to(self,x,y,z):
        if z!=0  and z!=-1:
            print("The Cruiser can not reach this position")
        else :
            Vessel.go_to(self,x,y,z)
    def fire_at(self,x,y,z):
        a=self.get_coordinates()
        b=ltt._range
        if self._max_hits==0:
            print("DestroyedError")
        if ((a[0]-x)**2+(a[1]-y)**2+(a[2]-z)**2)**(1/2)>b:
            print("OutOfRangeError")
            ltt._ammunitions-=1 
                    
class Fregate(Vessel):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),5,lmas)
    def go_to(self,x,y,z):
        if z!=0:
            print("The Cruiser can not reach this position")
        else :
            Vessel.go_to(self,x,y,z)
    def fire_at(self,x,y,z):
        a=self.get_coordinates()
        b=lmas._range
        if self._max_hits==0:
            print("DestroyedError")
        if ((a[0]-x)**2+(a[1]-y)**2+(a[2]-z)**2)**(1/2)>b:
            print("OutOfRangeError")
            lmas._ammunitions-=1
            
class Destroyer(Vessel):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),4,ltt1)
    def go_to(self,x,y,z):
        if z!=0:
            print("The Cruiser can not reach this position")
        else :
            Vessel.go_to(self,x,y,z)
    def fire_at(self,x,y,z):
        a=self.get_coordinates()
        b=ltt1._range
        if self._max_hits==0:
            print("DestroyedError")
        if ((a[0]-x)**2+(a[1]-y)**2+(a[2]-z)**2)**(1/2)>b:
            print("OutOfRangeError")
            ltt1._ammunitions-=1
            
class Aircraft(Vessel):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,1),1,lmas1)
    def go_to(self,x,y,z):
        if z!=1:
            print("The Cruiser can not reach this position")
        else :
            Vessel.go_to(self,x,y,z)
    def fire_at(self,x,y,z):
        a=self.get_coordinates()
        b=lmas1._range
        if self._max_hits==0:
            print("DestroyedError")
        if ((a[0]-x)**2+(a[1]-y)**2+(a[2]-z)**2)**(1/2)>b:
            print("OutOfRangeError")
            lmas1._ammunitions-=1
            

        
        
                
    

            
            
            


        

        
            
