import pygal

from die import Die
"""
    掷骰子
"""
# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)


# 分析结果 存储在列表中
frequencies = []
fredict = {}

#根据6面值，循环统计出现次数
for value in range(1, die.num_sides+1):
    #统计出现次数
    frequency = results.count(value)
    fredict[value] = frequency
    #放置到分析结果列表中
    frequencies.append(frequency)

print(frequencies)
print(fredict)



# 对结果进行可视化
hist = pygal.Bar()
#图片标题
hist.title = "Results of rolling one D6 1000 times."
#x轴显示值
hist.x_labels = ['1', '2', '3', '4', '5', '6']
#x轴标题
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
#添加直方图内容
hist.add('D6', frequencies)

#生成直方图
hist.render_to_file('die_visual.svg')


