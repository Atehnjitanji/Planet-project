import pandas as pd

df = pd.read_csv('planet_data.csv', index_col='eName')

dff = df[['isPlanet','meanRadius','orbit_type','orbits']]

class planet(): 
    def __init__(self,name, color = "blue", radius = 1):
        self.color = color
        self.radius = radius
        self.name = name
        self.moon_list = []
class moon():
    def __init__(self,name, color = "white", radius = 1,tidally_locked=False, planet_companion = None):
        self.name = name
        self.color = color
        self.radius = radius
        self.tidally_locked = tidally_locked
        self.planet_companion = planet_companion
    def update_planet(self):
        my_planet = self.planet_companion
        my_planet.moon_list.append(self)

def print_largest(pl): 
    largest = None 
    for moon in pl.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius: largest = moon      
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")

planet_d = dict()
moon_d = dict() 
for index, row in dff.iterrows(): 
    if row['isPlanet'] is True:
        planet_d[index] = planet(name = index,radius= row['meanRadius'])

for index, row in dff.iterrows():
    if row['isPlanet'] is False:
        moon_d[index] = moon(name = index,radius= row['meanRadius'], planet_companion= planet_d[row['orbits']], tidally_locked= row['orbit_type'])

'''for key, val in planet_d.items():
    print(key, val.radius)'''

'''for key, val in moon_d.items():
    val.update_planet()
    print(key, val.radius, val.planet_companion.name)'''

'''for key, val in planet_d.items():
    print_largest(val)
    print(key, [moon.name for moon in val.moon_list])'''
for key, val in moon_d.items():
    val.update_planet()

def order_planet(planet_ls):
    planet_dict=dict(planet_ls)
    moons = {}
    for index, row in df.iterrows():
        if row['isPlanet'] is True:
            planet_dict[index] = row['semimajorAxis_AU']
    planet_data = pd.DataFrame({'Planet':planet_dict.keys(),'Distance':planet_dict.values()})
    planet_data.sort_values(by='Distance',inplace=True)
    
    for i in planet_ls.values():
        moons_list2 = i.moon_list
        for l in moons_list2:
            moons_list2[moons_list2.index(l)]=l.name
        moons[i.name]= moons_list2
    for index, row in planet_data.iterrows():
        print(row['Planet'],row['Distance'],moons[row['Planet']])

order_planet(planet_d)

def no_moon(planet_ls):
    no_moon=[]
    for i in planet_ls.values():
        if i.moon_list == []:
            no_moon.append(i.name)
    print(no_moon)
no_moon(planet_d)
