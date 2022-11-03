
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
        
        
                
    

            
            
            


        

        
            