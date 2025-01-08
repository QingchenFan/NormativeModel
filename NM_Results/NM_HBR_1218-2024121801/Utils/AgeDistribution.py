import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#  --all HC--
def HC(path):
    data = pd.read_csv(path)
    # 提取男性和女性的年龄数据
    male_age_data = data[data['sex'] == 1]['age']
    female_age_data = data[data['sex'] == 2]['age']

    # 设置绘图风格为Seaborn默认风格
    sns.set()
    sns.set_style('white')
    # 绘制直方图
    sns.histplot(data=data, x='age', hue='sex', multiple='stack')
    sns.despine()
    plt.xticks([20, 25, 30, 35, 40])
    plt.xticks(fontsize=14)  # 设置x轴刻度字体大小
    plt.yticks(fontsize=14)
    # 设置图表的标题和轴标签
    plt.title('Population by Age and Gender - All HC')
    plt.xlabel('Age')
    plt.ylabel('Population')

    # 添加图例
    plt.legend(['Male', 'Female'])

    # 显示图表
    plt.show()
    plt.close()
#---------------------------------
#  --all MDD--
def MDD(path):
    data = pd.read_csv(path)

    # 提取男性和女性的年龄数据
    male_age_data = data[data['sex'] == 1]['age']
    female_age_data = data[data['sex'] == 2]['age']

    # 设置绘图风格为Seaborn默认风格
    sns.set()
    sns.set_style('white')
    # 绘制直方图
    sns.histplot(data=data, x='age', hue='sex', multiple='stack')
    sns.despine()
    plt.xticks([20, 25, 30, 35])
    # plt.yticks([5, 10, 15, 20])
    plt.xticks(fontsize=16)  # 设置x轴刻度字体大小
    plt.yticks(fontsize=16)

    # 设置图表的标题和轴标签
    plt.title('Population by Age and Gender - MDD')
    plt.xlabel('Age')
    plt.ylabel('Population')

    # 添加图例
    plt.legend(['Male', 'Female'])

    # 显示图表
    plt.show()
    plt.close()
#---------------------------------
#------重叠-------
# 读取两个CSV文件
def HCMDD(hcpath,mddpath):
    df1 = pd.read_csv(hcpath, usecols=['age'])
    df2 = pd.read_csv(mddpath, usecols=['age'])

    # 为数据框中的年龄列设置相同的名称
    df1.rename(columns={'age': 'age'}, inplace=True)
    df2.rename(columns={'age': 'age'}, inplace=True)
    print(df1['age'])
    # 使用Seaborn的distplot函数绘制直方图
    sns.distplot(df1['age'], hist=True, color='gray', kde=False, bins=15, label='S1',hist_kws={"edgecolor": "white", "linewidth": 1})
    sns.distplot(df2['age'], hist=True, color='r',kde=False, bins=15, label='S2',hist_kws={"edgecolor": "white", "linewidth": 1})
    sns.despine()
    ax = plt.gca()
    # 设置x轴线条粗细
    ax.spines['bottom'].set_linewidth(1)
    # 设置y轴线条粗细
    ax.spines['left'].set_linewidth(1)
    plt.xticks([20,  25,  30, 35])
    plt.xticks(fontsize=14)  # 设置x轴刻度字体大小
    plt.yticks(fontsize=14)
    plt.tick_params(axis='both', which='both',labelsize=14, bottom=False, top=False, left=False, right=False)
    # 设置图表的标题和轴标签
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Population')

    # 添加图例
    plt.legend()

    # 显示图表
    plt.show()
    plt.close()


hcpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/Feature/allHC_GrayVol246_nocombat_final1129.csv'
#HC(hcpath)
mddpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/Feature/allMDDGrayVol246_sum_1129.csv'
#MDD(mddpath)
#HCMDD(hcpath,mddpath)
s1 = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1129-2024112901/Step_7th_Subtype_ClinicalInfo/subtype1_age.csv'
s2 = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1129-2024112901/Step_7th_Subtype_ClinicalInfo/subtype2_age.csv'
MDD(s2)
#HCMDD(s1,s2)
