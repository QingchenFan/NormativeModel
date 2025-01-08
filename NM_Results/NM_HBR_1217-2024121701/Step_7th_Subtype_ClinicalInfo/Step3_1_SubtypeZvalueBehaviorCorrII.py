import glob
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import statsmodels.stats.multitest as smm


cldata = glob.glob('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtypeClinical/*subtype2*.csv')
for j in cldata:
    sbty = j.split('/')[-1].split('_')[4]
    print(sbty)
    df = pd.read_csv(j)
    regions = df.columns.tolist()
    bio = regions[1]
    del regions[0:2]
    srvalue = []
    spvalue = []
    rvalue = []
    pvalue = []
    regionbox = []
    for i in regions:
        print(i)

        # 筛选A8m_R小于-1.96的行
        filtered_df = df[df[i] > 1.96]

        # 提取这些行的A8m_R值和对应的age
        x = filtered_df[i].values
        y = filtered_df[bio].values
        print(x)
        print(y)
        if len(x)<= 2:continue
        regionbox.append(i)
        # 计算相关性
        #correlation = pd.Series(a8m_r_values).corr(pd.Series(ages))
        corr, p_value = pearsonr(x, y)
        rvalue.append(corr)
        pvalue.append(p_value)

        scorr, sp_value = spearmanr(x, y)
        srvalue.append(scorr)
        spvalue.append(sp_value)
        if sp_value < 0.05:
            print(f"Spearman相关系数: {scorr}", f"p值: {sp_value}")
        #print(f"Pearson相关系数: {corr}", f"p值: {p_value}")

    rejected, fdr_pvalue, _, _ = smm.multipletests(pvalue, method='fdr_bh')
    srejected, sfdr_pvalue, _, _ = smm.multipletests(spvalue, method='fdr_bh')
        #print(f"相关系数: {correlation}", f"p值: {p_value}")
    result_df = pd.DataFrame({
        'region': regionbox,

        'rvalue-s': srvalue,
        'pvalue-s': spvalue,
        'fdr-pvalue-s': sfdr_pvalue,

        'rvalue': rvalue,
        'pvalue': pvalue,
        'fdr-pvalue': fdr_pvalue,

    })
    result_df.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtypeClinical/CorrII/'
                     'Step5_3_sbutype2''_Zvalue_Corr_'+sbty, index=False)
    exit()