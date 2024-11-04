import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置样式
#sns.set(style="whitegrid")

# 读取数据
data = pd.read_csv('/Volumes/QCI/NormativeModel/Prediction/Data/sum_BrainPro_ClinicalInfo.csv')

y = 'PSS'
# 创建图形
plt.figure(figsize=(12, 8))

# 绘制箱体图，颜色设置为灰色
sns.boxplot(x='site', y=y, data=data, color='#d3d7d4', showfliers=False)

# 添加散点图，设置为灰色
sns.stripplot(x='site', y=y, data=data, color='darkgray', alpha=0.6, jitter=True)

# 去掉上面和右侧的线
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 添加标题和标签
plt.title(y+' Distribution', fontsize=16)
plt.xticks(size=12)
plt.yticks(size=12)

plt.xlabel('Site', fontsize=14)
plt.ylabel(y + ' Score', fontsize=14)

# 显示图形
plt.show()