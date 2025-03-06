import numpy as np
from scipy.spatial.distance import pdist, squareform
import pandas as pd
import matplotlib.pyplot as plt


d1 = pd.read_csv('/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801_test/Step_5th_Subtype/step2_group_subtype1.csv', index_col=0)
d1=d1.iloc[:, 1:].values
print(d1)

d2 = pd.read_csv('/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801_test/Step_5th_Subtype/step2_group_subtype2.csv', index_col=0)
d2=d2.iloc[:, 1:].values
print(d2.shape)



X = np.vstack((d1,d2))
print(X)
print(X.shape)

# 计算欧氏距离
D = pdist(X, 'euclidean')
print(D.shape)

# 将距离向量转换为相似性矩阵
#S = 1.0 / (D + 1)  # 示例使用，根据需要可以调整相似性计算方式
S = squareform(D)

df = pd.DataFrame(S)
df.to_csv('./step3_distance.csv')


from sklearn.metrics import pairwise_distances
similarity_matrix = pairwise_distances(X, metric='euclidean')

import matplotlib.pyplot as plt
import numpy as np

# 使用matplotlib绘制色块图
plt.imshow(S, cmap=plt.cm.Reds)  # cmap参数指定色彩映射
cbar = plt.colorbar(orientation='vertical')  # 竖直方向的颜色条
cbar.set_label('Euclidean distance',rotation=270,labelpad=20)
# plt.gca().invert_yaxis()  # To make smaller values darker

# 隐藏坐标轴

plt.savefig('./step3_Intersubject.png', dpi=300)

# 显示图形
plt.show()