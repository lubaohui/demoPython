import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

"""
    使用WebApi，访问URL，返回json数据
"""

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 处理结果 打印json数据的keys
print(response_dict.keys())

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
#打印该仓库的包含的关键字总数
print("\nKeys:", len(repo_dict))
#打印关键字
#for key in sorted(repo_dict.keys()):
#    print(key)

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])


# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
print("\nSelected information about each repository:")

names, stars = [], []
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }

    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    stars.append(plot_dict)

print(stars)
# 可视化
my_style = LS('#333366', base_style=LCS)

"""
    x_label_rotation 让标签绕x 轴旋转45度
    隐藏了图例(show_legend=False )
"""
#创建配置对象，并设置配置信息
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
#将较长的项目名缩短为15个字符
my_config.truncate_label = 15
#隐藏图表中的水平线
my_config.show_y_guides = False
#设置了自定义宽度
my_config.width = 1000

#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)

chart.render_to_file('python_repos2.svg')





