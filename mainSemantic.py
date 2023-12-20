import semantics
import semantics2RG
from oneBitClock import oneBitClock
import parcours

clock = oneBitClock()
print(clock.initial())
for state in clock.initial():
    print(clock.actions([state]))