import semantics
import semantics2RG
from oneBitClock import oneBitClock
import parcours

clock = oneBitClock()
print(clock.initial())
print(clock.actions(clock.initial()))