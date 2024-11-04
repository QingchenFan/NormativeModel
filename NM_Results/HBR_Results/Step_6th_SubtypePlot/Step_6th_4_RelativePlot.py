import matplotlib.pyplot as plt
import numpy as np

# 假设有两组人的数据，每组有5个特征
import pandas as pd

df = pd.read_csv('/Users/fan/PycharmProjects/pythonProject/abide/71/combat_latest_abide.csv',index_col=0)
features = df.columns[6:34]
print(features)

d1 = pd.read_csv('/Users/fan/PycharmProjects/pythonProject/abide/71/group_01_mean.csv') # 随机生成第一组数据
group1=d1.loc[:,'0'].values
d2 = pd.read_csv('/Users/fan/PycharmProjects/pythonProject/abide/71/group_11_mean.csv') # 随机生成第一组数据
group2=d2.loc[:,'0'].values

# 设置雷达图的参数
num_vars = len(features)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制第一组数据
values = np.concatenate((group1, [group1[0]]))  # 闭合图形
angles += angles[:1]  # 闭合图形
ax.fill(angles, values, color='#A4CBA8', alpha=0.25)
ax.plot(angles, values, color='#A4CBA8', linewidth=2, linestyle='solid')


# 绘制第二组数据
values = np.concatenate((group2, [group2[0]]))
ax.fill(angles, values, color='#93B8DB', alpha=0.25)
ax.plot(angles, values, color='#93B8DB', linewidth=2, linestyle='solid')

# 设置雷达图的刻度和标签
ax.set_thetagrids(np.degrees(angles[:-1]), features)
plt.savefig('/Users/fan/PycharmProjects/pythonProject/abide/71/figures/14.png',dpi=300)

# 显示图形
plt.show()