import json

import pygal.maps.world
from pygal.style import RotateStyle

from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    

        
#创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    pop_dict['Year'] =='2010'
    country = pop_dict['Country Name']
    population = int(float(pop_dict['Value']))
    code = get_country_code(country)
    if code:
        cc_populations[code] = population
        
#根据人口数量将所有国家分为三组
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
        
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
        
    else:
        cc_pop_3[cc] = pop
        


        
#看看分组包含多少个国家
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))
            
wm = pygal.maps.world.World()
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'world populations in 2010,by country'

wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)   
 
wm.render_to_file('world_populations.svg')
