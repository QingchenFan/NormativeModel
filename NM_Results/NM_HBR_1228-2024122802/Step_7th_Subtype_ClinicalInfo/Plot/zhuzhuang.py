import matplotlib.pyplot as plt
import pandas as pd

# 准备数据
data = {
    "Retardation": 0.83,
    "Work and Interests": 0.31,
    "Depressed": 0.23
}
df = pd.DataFrame.from_dict(data, orient='index', columns=['Loading'])

# 创建图像
fig, ax = plt.subplots(figsize=(4, 5))

# 设置柱子的位置，让它们更紧凑
x_positions = [i for i in range(len(df))]  # 紧凑排列的x轴位置

# 绘制线条和红色的点
for i, (category, row) in enumerate(df.iterrows()):
    ax.plot([x_positions[i], x_positions[i]], [0, row['Loading']], color='gray', linewidth=2)  # 垂直线
    ax.plot(x_positions[i], row['Loading'], 'o', color='red', markersize=10)  # 顶部的红色圆点

# 设置x轴和y轴
ax.set_xticks(x_positions)
ax.set_xticklabels(df.index, rotation=0, ha='center', fontsize=12)  # 增大x轴字体大小
ax.set_ylabel("Loading", fontsize=14)  # 增大y轴标题字体大小
ax.set_ylim(0, 1)  # 根据最大值调整y轴范围

# 设置 y 轴刻度字体大小
ax.tick_params(axis='y', labelsize=12)  # 增大y轴刻度字体大小
plt.yticks([0.2, 0.4, 0.6, 0.8, 1])
# 隐藏右侧和上方的边框线
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# 调整布局
plt.tight_layout()
plt.show()
