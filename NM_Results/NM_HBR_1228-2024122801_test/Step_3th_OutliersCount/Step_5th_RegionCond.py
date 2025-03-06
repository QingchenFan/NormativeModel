import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.stats.multitest as smm
def cohen_d(group1, group2):
    """
    计算Cohen's d
    :param group1: 第一组数据（一维数组或列表）
    :param group2: 第二组数据（一维数组或列表）
    :return: Cohen's d值
    """
    n1, n2 = len(group1), len(group2)
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (mean1 - mean2) / pooled_std
HCdata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/GrayVol246_Z_AllHCestimate.csv', index_col=0)
MDDdata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/GrayVol246_Z_AllMDD.csv', index_col=0)
region = HCdata.columns.tolist()
print(region)
cod = []
rg = []

pvalue = []
for i in region:
    print(i)
    rg.append(i)
    hc = np.array(HCdata[i])
    mdd = np.array(MDDdata[i])

    cohend = cohen_d(hc, mdd)
    cod.append(cohend)

    t, p = ttest_ind(hc, mdd)

    pvalue.append(p)
srejected, fdr_pvalue, _, _ = smm.multipletests(pvalue, method='fdr_bh')
res = pd.DataFrame({
        'region': rg,
        'cohen_d': cod,
    'pvalue-s': pvalue,
    'fdr-pvalue-s': fdr_pvalue,

})
res.to_csv('./Step5_MDDHCCond.csv', index=False)