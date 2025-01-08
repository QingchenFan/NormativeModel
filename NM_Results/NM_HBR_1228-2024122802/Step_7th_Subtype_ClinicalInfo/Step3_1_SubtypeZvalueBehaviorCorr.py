import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import statsmodels.stats.multitest as smm
import glob

file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/subtypeClinical/*.csv'
csv = glob.glob(file_1)

for i in csv:
    print(i)

    sbty = i.split('/')[-1].split('_')[2]

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(i)

    behscore = np.array(df1.iloc[:, 1])

    brainRegion = df1.columns.tolist()
    cl = brainRegion[1:2]

    del brainRegion[:2]
    print(brainRegion)
    srvalue = []
    spvalue = []
    rvalue = []
    pvalue = []
    regionbox = []
    for i in brainRegion:
        regionbox.append(i)
        x = np.array(df1[i])

        y = behscore

        corr, p_value = pearsonr(x, y)
        rvalue.append(corr)
        pvalue.append(p_value)

        scorr, sp_value = spearmanr(x, y)
        srvalue.append(scorr)
        spvalue.append(sp_value)

        # print(f"Spearman相关系数: {scorr}", f"p值: {sp_value}")
        # print(f"Pearson相关系数: {corr}", f"p值: {p_value}")

    # 对p值进行FDR校正
    rejected, fdr_pvalue, _, _ = smm.multipletests(pvalue, method='fdr_bh')
    srejected, sfdr_pvalue, _, _ = smm.multipletests(spvalue, method='fdr_bh')

    # 创建DataFrame，将rvalue、pvalue、fdr_pvalue对应保存
    result_df = pd.DataFrame({
        'region': regionbox,

        'rvalue-s': srvalue,
        'pvalue-s': spvalue,
        'fdr-pvalue-s': sfdr_pvalue,

        'rvalue': rvalue,
        'pvalue': pvalue,
        'fdr-pvalue': fdr_pvalue,

    })

    # 将结果保存到CSV文件中，可根据实际需求修改文件路径及文件名
    result_df.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/subtypeClinical/Corr/'
                     'Step5_3_'+sbty+'_Zvalue_'+cl[0]+'Corr.csv', index=False)