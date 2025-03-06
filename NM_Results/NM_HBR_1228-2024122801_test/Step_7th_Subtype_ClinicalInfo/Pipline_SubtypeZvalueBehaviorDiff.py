import pandas as pd
import glob
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# subtype1 与 subtype2 行为上的差异（这里比较的是两个亚型对应的量表总分之间的差异）
def showDiff(subtype1_data, subtype2_data, savepath, datatype, Mark):
    # Read the CSV files into pandas DataFrames
    # 为每组数据添加标签


    # Extract the HAMD scores from both datasets
    subtype1_mark = subtype1_data[Mark]
    subtype2_mark = subtype2_data[Mark]


    # Perform an independent t-test to check for differences in HAMD scores
    t_stat, p_value = stats.ttest_ind(subtype1_mark, subtype2_mark)
    print(Mark, f' t_stat:{t_stat}', f' p_value:{p_value}' )
    subtype1_data['Group'] = 'Subtype1'
    subtype2_data['Group'] = 'Subtype2'
    # 独立样本 T 检验
    t_stat, p_value = stats.ttest_ind(subtype1_mark, subtype2_mark)
    print(Mark, f't_stat: {t_stat}', f'p_value: {p_value}')



    # 合并数据
    combined_data = pd.concat([subtype1_data[[Mark, 'Group']], subtype2_data[[Mark, 'Group']]])

    # 绘制箱线图
    plt.figure(figsize=(10, 6))
    sns.set(style="white")

    sns.boxplot(data=combined_data, x='Group', y=Mark, linewidth=2, width=0.6, fliersize=6)

    # 设置标签和标题
    plt.xticks([0, 1], ['Subtype 1', 'Subtype 2'], fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylabel(Mark + ' Score', labelpad=25, fontsize=16)
    #plt.title(f'Comparison of {Mark} Scores\nT-test p-value: {p_value:.2f}', fontsize=12)

    # 美化轴线
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['left'].set_color('black')

    # 设置刻度颜色
    plt.gca().tick_params(axis='x', colors='black')
    plt.gca().tick_params(axis='y', colors='black')
    out = savepath + '/' + datatype+'_'+Mark + '.png'
    plt.savefig(out, dpi=300)


csvdata = glob.glob("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/ClinicalInfo/*.csv")

for b in csvdata:
  box = []
  name = b.split('/')[-1].split('_')[-1][:-4]

  for i in range(1, 3):
      file_1 = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801_test/Step_5th_Subtype/' \
                  'step2_group_subtype' + str(i) + '.csv'

      df1 = pd.read_csv(file_1)
      df2 = pd.read_csv(b)
      df_new = pd.merge(df2, df1, on='subID', how='inner')

      box.append(df_new)
      df_new.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/subtypeClinical/'
                    'Step5_1_subtype'+str(i)+'_Zvalue_'+name+'.csv', index=False)

  showDiff(box[0], box[1], datatype='BrainPro', Mark=name, savepath='./')


