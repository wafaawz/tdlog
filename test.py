from TDLOG import Weapon
from TDLOG import LT
from TDLOG import LMAA
from TDLOG import LMAS
from TDLOG import Vessel
from TDLOG import Cruiser
from TDLOG import Fregate
from TDLOG import Submarine
from TDLOG import Destroyer
from TDLOG import Aircraft
from TDLOG import Espace
a=Weapon(30,40)
a.fire_at(0,0,0)
b=LMAA()
b.fire_at(0,0,-1)
c=LT()
c.fire_at(0,0,1)
d=LMAS()
d.fire_at(0,0,5)
e=Cruiser(1,1)
e.go_to(1,1,1)
e.fire_at(100,100,100)
f=Fregate(2,3)
f.go_to(1,5,1)
f.fire_at(1,1,1)
A=Espace(1,2,1,[e])
A.ajouter(f)
print(A._listeV)
A.recevoircoup(2,3,0)



