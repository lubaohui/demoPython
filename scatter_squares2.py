import matplotlib.pyplot as plt
"""
    绘制散点图
"""
#绘制单个散点
#plt.scatter(2, 4, s=200)
"""随机x轴数据，绘制一系列散点"""
x_values = list(range(1, 1001))
"""x轴数据的平台"""
y_values = [x**2 for x in x_values]


"""
    edgecolor='none' 删除数据点轮廓 
    c='red' 自定义数据点颜色
    cmap=plt.cm.Blues 颜色映射，渐变色
"""
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#plt.scatter(x_values, y_values, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
#plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
#plt.show()
"""
    第一个参数：保存图表的名称
    第二个参数：图表多余的空白区域截掉
"""
plt.savefig('squares_plot.png', bbox_inches='tight')
