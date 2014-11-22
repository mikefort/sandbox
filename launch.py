#requirements

from random import randrange
import time

#define launch timer time
launch_timer = 5
print "Launching rocket in...."
#countdown
while launch_timer >= 0:
    print launch_timer
    launch_timer -= 1
    time.sleep(1)

print "Rocket launched!"
print "Patiently awaiting status update of the crew!"
print "....."
print ""

crew_delay = randrange(4)
time.sleep(crew_delay)
print "Crew report that ship is intact upon leaving orbit. Crew is traveling toward Moon at this time"
print "Crew will be reporting back soon on status of Moon landing"
print ""
print ""
#randomly decide if rocket survives
rand_number = randrange(10)
moon_delay = randrange(3)
if rand_number % 2 == 0:
    time.sleep(moon_delay)
    print "Rocket entered space and landed on moon safely"
else:
    time.sleep(moon_delay)
    print "Rocket crashed into moon and all 3 crew members died"