#!/usr/bin/python
import ephem
import datetime

somewhere = ephem.Observer()
somewhere.lat = '28.637226298731484' # <== change me
somewhere.lon = '-96.45818956200321' # <== and change me
somewhere.elevation = 7
print somewhere.date

sun = ephem.Sun()
r1 = somewhere.next_rising(sun)
s1 = somewhere.next_setting(sun)

somewhere.horizon = '-0:34'
r2 = somewhere.next_rising(sun)
s2 = somewhere.next_setting(sun)
print ("Visual sunrise %s" % r1)
print ("Visual sunset %s" % s1)
print ("Naval obs sunrise %s" % r2)
print ("Naval obs sunset %s" % s2)
