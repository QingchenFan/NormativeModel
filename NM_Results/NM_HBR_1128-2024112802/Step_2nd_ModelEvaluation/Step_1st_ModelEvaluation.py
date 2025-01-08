import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def plotModel(ipath,opath,mark):
    data = pd.read_csv(ipath)
    normal_data = data[mark]

    plt.figure(figsize=(10, 8))
    # 使用kdeplot函数绘制核密度估计曲线
    sns.kdeplot(normal_data, shade=True, color='#5C5C5C',linewidth=0)

    ax = plt.gca()
    # 隐藏上边框和右边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 设置下边框和左边框的线宽
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)

    plt.gca().tick_params(axis='x', which='both', width=0, labelsize=16)
    plt.gca().tick_params(axis='y', which='both', width=0, labelsize=16)


    plt.xlabel('SMSE',size=16)
    plt.ylabel('Density',size=16)
    plt.savefig(opath ,dpi=300)
    # 显示图形
    plt.show()

ipath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_112802/StaResults/hbr_estimate_GrayVol246_ResSum.csv'
opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_112802/StaResults/ModelEvaluation_SMSE.png'
mark = 'SMSE'
plotModel(ipath,opath,mark)