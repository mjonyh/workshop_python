'''
Exercise 1:
------------------------------------------------------------------------

For a satellite, orbiting around the earth with a time period, T.
The height/altitude of the satellite can be given as

h = (GMT^2/4pi^2)^(1/3) - R

where G = 6.67x10^(-11) m^3kg^-1s^-2, M = 5.97x10^24 kg and R = 6371 km.
'''
pi = 3.1416
G = 6.67e-11
M = 5.97e24
R = 6371.0e3

T = input('Please enter the time period of the satellite: ')

nume = (G*M*T**2)
denom = (4*pi**2)
h = (nume/denom)**(1./3.) - R

print 'If the time period is ', T, ' s, altitude will be ', h, ' m'

if h < 0:
    print '\n Negative height!\n'
