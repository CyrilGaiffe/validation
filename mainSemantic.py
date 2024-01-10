import semantics
import semantics2RG
from oneBitClock import oneBitClock
from parcours import parcours_en_largeur
from parcours import ParentTraceur


# syntax for calling upon one bit clock semantics
clock = oneBitClock()
# print(clock.initial())
# for state in clock.initial():
#     print(clock.execute(clock.actions([state])[0], [state]))
adaptator = semantics2RG(clock)
