import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
# 柱状图
# 假设的字典数据
info = {'num': [1, 2, 3, 4, 5, 10], 'sum': [798, 518, 365, 281, 222, 82]}

# 提取num和sum的值
x = list(range(len(info['num'])))  # 创建0到len(info['num'])-1的索引作为x轴的值
y = info['sum']

# 绘制柱状图
plt.bar(x, y, color='gray')
# 只保留左侧和下侧的轴线
plt.gca().spines['top'].set_visible(False)  # 去掉上侧轴线
plt.gca().spines['right'].set_visible(False)  # 去掉右侧轴线
plt.gca().spines['bottom'].set_color('black')  # 设置下侧轴线为黑色
plt.gca().spines['left'].set_color('black')  # 设置左侧轴线为黑色
# 添加标题和轴标签
plt.title('Sum by Number')

# 设置x轴刻度标签
plt.xticks(x, info['num'])
plt.xlabel('Brain Regions')
plt.ylabel('Sum')

# 显示图表
plt.show()
