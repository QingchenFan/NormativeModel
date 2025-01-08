import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the CSV files

def showDiff(subtype1_path, subtype2_path,savepath,datatype,Mark):
    # Read the CSV files into pandas DataFrames
    subtype1_data = pd.read_csv(subtype1_path)
    subtype2_data = pd.read_csv(subtype2_path)


    # Extract the HAMD scores from both datasets
    subtype1_mark = subtype1_data[Mark]
    subtype2_mark = subtype2_data[Mark]
    # Perform an independent t-test to check for differences in HAMD scores
    t_stat, p_value = stats.ttest_ind(subtype1_mark, subtype2_mark)
    print('Mark: ',Mark,' t_stat: ',t_stat,' p_value: ', p_value)



    plt.figure(figsize=(10, 6))
    sns.set(style="white")  # 去掉背景网格线

    # 创建箱体图
    sns.boxplot(data=[subtype1_mark, subtype2_mark], linewidth=2, width=0.6, fliersize=6)

    # 设置标签和标题
    plt.xticks([0, 1], ['Subtype 1', 'Subtype 2'], fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylabel(Mark+' Score', labelpad=25, fontsize=16)
    plt.title(f'Comparison of {Mark} Scores\nT-test p-value: {p_value:.2f}', fontsize=12)

    # 只保留左侧和下侧的轴线
    plt.gca().spines['top'].set_visible(False)  # 去掉上侧轴线
    plt.gca().spines['right'].set_visible(False)  # 去掉右侧轴线
    plt.gca().spines['bottom'].set_color('black')  # 设置下侧轴线为黑色
    plt.gca().spines['left'].set_color('black')  # 设置左侧轴线为黑色

    # 设置刻度颜色为黑色
    plt.gca().tick_params(axis='x', colors='black')
    plt.gca().tick_params(axis='y', colors='black')
    out = savepath + '/' + datatype+'_'+Mark + '.png'
    #plt.savefig(out,dpi=300)


subtype1_path = './subtype1_HAMD.csv'
subtype2_path = './subtype2_HAMD.csv'
df = pd.read_csv(subtype1_path)
iterm = df.columns.tolist()
for i in iterm:
    print(i)
    if i != 'subID':
        showDiff(subtype1_path,subtype2_path, datatype='HAMD',Mark=i, savepath='./')

#showDiff(subtype1_path,subtype2_path, datatype='HAMD',Mark='', savepath='./')
