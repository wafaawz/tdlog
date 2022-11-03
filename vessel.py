
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
            
class Espace:
    def __init__(self,x,y,z,listeV):
        if 0<=x<=100 and 0<=y<=100 and (z==0 or z==1 or z==-1):
            self._x=x
            self._y=y
            self._z=z
        self._listeV=listeV
    
    def ajouter(self,V):
        a=0
        c=0
        for j in range(0,len(self._listeV)):
            a+=j._max_hits
            if j.getcoordinates()==V.getcoordinates():
                c=1
        if c==0 and a<=22:
            self._listeV = self._listeV + [V]
    
    def recevoircoup(self,x,y,z):
        b=0
        for k in range(0,len(self._listeV)):
            if k.getcoordinates()==(x,y,z):
                b=1
        if b==1:
            return(True)
        else :
            return(False)
        
        
                
    

            
            
            


        

        
            
