import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/Volumes/QCI/NormativeModel/Prediction/Data/sum_BrainPro_ClinicalInfo.csv')

l = 'PSS'
res = data[l]

sns.distplot(res, bins=20, kde=False)
#, bins=20, kde=False, hist_kws={'color': 'black'}

# 去掉上面和右侧的线
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.xticks(size=14)
plt.yticks(size=14)
plt.ylabel('Num', fontsize=14)
plt.xlabel(l + ' Score', fontsize=14)

plt.show()

