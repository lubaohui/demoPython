import pygal

from die import Die
"""
    掷骰子
"""

# 创建D6和D10骰子
die_1 = Die()
die_2 = Die(10)
# 掷骰子多次，并将结果存储到一个列表中

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()

    results.append(result)

print(results)


# 分析结果 存储在列表中
frequencies = []
fredict = {}

max_result = die_1.num_sides + die_2.num_sides

#根据6面值，循环统计出现次数
for value in range(2, max_result+1):
    #统计出现次数
    frequency = results.count(value)
    #fredict[value] = frequency
    #放置到分析结果列表中
    frequencies.append(frequency)

print(frequencies)
print(fredict)



# 对结果进行可视化
hist = pygal.Bar()
#图片标题
hist.title = "掷骰子50000次，D6 + D10"
#x轴显示值
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
#x轴标题
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
#添加直方图内容
hist.add('D6 + D10', frequencies)

#生成直方图
hist.render_to_file('different_dice.svg')


