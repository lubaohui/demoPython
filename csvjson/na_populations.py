import pygal

from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
# 颜色相关
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

"""
    在地图上显示数字
"""

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = World(style=wm_style)

wm.title = 'North, Central, and South America'

#第二个实参传递了一个字典而不是列表
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')




