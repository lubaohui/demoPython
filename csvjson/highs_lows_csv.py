import csv

from matplotlib import pyplot as plt
from datetime import datetime



"""
    分析csv文件
"""

#filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

# 从文件中获取日期、最高气温和最低气温
with open(filename) as f:
    reader = csv.reader(f)
    """分析文件头"""
    header_row = next(reader)

    print(header_row)

    #打印文件头及位置
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #读取数据
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            highs.append(int(row[1]))
            lows.append(int(row[3]))
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)

    print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)

    #给图表区域着色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)

    #绘制斜的日期标签 避免重叠
    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

