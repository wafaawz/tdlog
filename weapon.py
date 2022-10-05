class Weapon:
    def __init__(self,ammunitions, range):
        self._ammunitions=ammunitions
        self._range=range
    def fire_at(self,x,y,z):
        print( "the weapon will fire at "(x,y,z))