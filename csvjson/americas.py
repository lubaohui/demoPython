import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
# 颜色相关
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

"""
    北美、中美和南美的简单地图:
"""
#wm = pygal.Worldmap()

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = World(style=wm_style)

wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')


