from Planet_classes import *
import pytest

earth = planet('Earth','Blue',4.26e-5)
jupiter = planet('Jupiter','Orange',0.00046)
saturn = planet('Saturn','Purple',0.000389)

luna = moon('Moon','White',1.16e-5,True,earth)
base = moon('Base','White',1.16,True,earth)

europa = moon('Europa','White',1560,True,jupiter)
league = moon('League','White',15,False,jupiter)

hyperion = moon('Hyperion','White',1560,False,saturn)
thor = moon('Thor','White',12,True,saturn)

def test_planet_update():
    europa.update_planet()
    luna.update_planet()
    hyperion.update_planet()
    league.update_planet()
    first_moon = jupiter.moon_list[0]
    assert first_moon.name =="Europa"
