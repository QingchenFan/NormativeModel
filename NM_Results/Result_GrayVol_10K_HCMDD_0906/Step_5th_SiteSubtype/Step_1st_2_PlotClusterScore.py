import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# 读取CSV文件
df = pd.read_csv('./Step1_1_silhouette_score.csv')

# 假设CSV文件中只有一列数据，列名是 '0'
values = df['0'].values

# 创建自定义的横坐标标签，从2到10
categories = list(range(2, 11))

# 检查数据点的数量是否超过8（横坐标的范围）
if len(values) > 10:
    print("数据点数量超过横坐标的范围（2到10），请调整数据或横坐标范围。")
else:
    # 绘制灰色的柱状图
    plt.bar(categories, values, color='#A9A9A9')  # 设置柱状图颜色为灰色

    # 去掉上框和右框
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # 可以添加一个星星，这里以第5个数据点为例
    # star_x = 2  # 星星的横坐标位置
    # star_y = values[star_x - 2]  # 星星的纵坐标位置，这里假设是第5个数据点的值
    # plt.scatter(star_x, star_y, color='gold', zorder=5)  # 星星使用散点图绘制

    # 设置横坐标的范围
    plt.xlim(1, 11)  # 确保横坐标的范围正确

    # 设置横坐标的刻度
    plt.xticks(categories)  # 使用自定义的横坐标标签作为刻度

    # 添加标题和标签
    plt.xlabel('Number of clusters')  # 添加横坐标标签
    plt.ylabel('Silhouette Coefficient')  # 添加纵坐标标签
    plt.savefig('./step1_2_clusterscore_Data135.png', dpi=300)

    # 显示图形
    plt.show()