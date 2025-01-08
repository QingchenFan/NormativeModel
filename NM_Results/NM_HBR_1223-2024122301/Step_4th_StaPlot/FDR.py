
import statsmodels.stats.multitest as smm

pvalue = [0.00015149637754190547,3.38529662647462e-07,0.0645159115106406]
rejected, fdr_pvalue, _, _ = smm.multipletests(pvalue, alpha=0.05, method='fdr_bh')
print(fdr_pvalue)
