from random import choice
class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            #表示向右走的1，要么是表示向左走的-1
            x_direction = choice([1, -1])
            #沿指定的方向走多远
            x_distance = choice([0, 1, 2, 3, 4])
            #动方向乘以移动距离，确定x轴的移动距离，x_step为正，将向右移动，为负将向左移动，而为零将垂直移动
            x_step = x_direction * x_distance

            # 表示向右走的1，要么是表示向左走的-1
            y_direction = choice([1, -1])
            # 沿指定的方向走多远
            y_distance = choice([0, 1, 2, 3, 4])
            #动方向乘以移动距离，确定Y轴的移动距离，y_step 为正，就意 味着向上移动，为负意味着向下移动，而为零意味着水平移动
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)