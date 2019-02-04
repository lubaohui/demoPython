import json

from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
# 颜色相关
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_json.json'

# 创建一个包含人口数量的字典
cc_populations = {}

with open(filename) as f:
    pop_data = json.load(f)
    # 打印每个国家2010年的人口数量
    for pop_dict in pop_data:
        #print(pop_dict)
        if pop_dict['Year'] == 2016:
            country_name = pop_dict['Country Name']
            population = pop_dict['Value']
            code = get_country_code(country_name)

            if code:
                #print(code + ": " + str(population))
                cc_populations[code] = population
            else:
                print('ERROR - ' + country_name)

            #print(country_name + ": " + str(population))



"""
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country)
        print(country + ' ' + str(code))
        if code:
            cc_populations[code] = population

"""

print(cc_populations)

# 为了使颜色分层更加明显
cc_populations_1,cc_populations_2, cc_populations_3 = {}, {}, {}

for cc, population in cc_populations.items():
    if population < 10000000:
        cc_populations_1[cc] = population
    elif population < 1000000000:
        cc_populations_2[cc] = population
    else:
        cc_populations_3[cc] = population
# 看看每组分别包含多少个国家
print(len(cc_populations_1),len(cc_populations_2),len(cc_populations_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

world = World(style=wm_style)

world.title = 'World Population in 2016, by Country'


#第二个实参传递了一个字典而不是列表
#wm.add('2016', cc_populations)
world.add('0-10m', cc_populations_1)
world.add('10m-1bn', cc_populations_2)
world.add('>1bn', cc_populations_3)

world.render_to_file('world_population_cc.svg')

