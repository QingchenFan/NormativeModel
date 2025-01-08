import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# processing_dir = "/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/"
# os.chdir(processing_dir)
# pro_dir = os.getcwd()
# output_path = os.path.join(pro_dir, 'Models/')
# log_dir = os.path.join(pro_dir, 'log/')
# allHC_te = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/allHC_te.csv')
# idps = allHC_te.columns.tolist()
#
# # test_covariate = {'sex': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
# #                 'sitenum':[1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2],
# #                           'age': [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36, 0.38, 0.40]
# #                   }
# # test_covariate = pd.DataFrame(data=test_covariate)
# test_covariate = pd.read_csv('/Users/qingchen/Desktop/test_qc.csv')
# X_test = (test_covariate['age']).to_numpy(dtype=float)
# with open('test_covariate.pkl', 'wb') as file:
#     pickle.dump(pd.DataFrame(X_test), file)
# testcovfile = os.path.join(pro_dir, 'test_covariate.pkl')
#
# batch_effects_test = test_covariate[['site','sex']].to_numpy(dtype=int)
# with open('test_tsbefile.pkl', 'wb') as file:
#     pickle.dump(pd.DataFrame(batch_effects_test), file)
# tsbefile = os.path.join(pro_dir, 'test_tsbefile.pkl')
# outputsuffix = 'TJtest'
# ptk.normative.predict(
#                             covfile=testcovfile,
#                             respfile=None,
#                             tsbefile=tsbefile,
#                             alg='hbr',
#                             log_path=log_dir,
#                             binary=True,
#                             model_path=output_path,
#                             outputsuffix=outputsuffix,
#                             savemodel=True
# )
# exit()
# confidence interval calculation at x_forward
def confidence_interval(s2,x,z):
  CI = np.zeros((len(x_forward),len(idps)))
  for i,xdot in enumerate(x_forward):
    ci_inx = np.isin(x,xdot)
    S2 = s2[ci_inx]
    S_hat = np.mean(S2,axis=0)
    n = S2.shape[0]
    CI[i,:] = z*np.power(S_hat/n,.5)
  return CI
yhat_forward = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/yhat_TJtest.pkl')   # 测试集的yhat
yhat_forward = yhat_forward.iloc[:,:].to_numpy(dtype=float)

print('yhat_forward-',yhat_forward.shape)

test_covariate = pd.read_csv('/Users/qingchen/Desktop/test_qc.csv')
x_forward = (test_covariate['age']).to_numpy(dtype=float)

#x_forward = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

data_test = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/allHC_te.csv')

x = np.array(data_test['age'])

print('x-',x.shape)
y = data_test.iloc[:,6:]# 训练集的y

idps = data_test.columns.tolist()
del idps[0:6]

s2 = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/ys2_estimate.pkl')   # 只有HCP训练集时，所输出的yhat
s2 = s2.iloc[:,:].to_numpy(dtype=float)
print('s2-',s2.shape)
CI_95=confidence_interval(s2,x,1.96)
CI_99=confidence_interval(s2,x,2.58)

for idp_num,idp_name in enumerate(idps):

    print(y[idp_name])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(x_forward,yhat_forward[:,idp_num], linewidth=4, label='Normative trejactory')


    ax.plot(x_forward,CI_95[:,idp_num]+yhat_forward[:,idp_num], linewidth=2,linestyle='--',c='g', label='95% confidence interval')
    ax.plot(x_forward,-CI_95[:,idp_num]+yhat_forward[:,idp_num], linewidth=2,linestyle='--',c='g')

    ax.plot(x_forward,CI_99[:,idp_num]+yhat_forward[:,idp_num], linewidth=1,linestyle='--',c='k', label='99% confidence interval')
    ax.plot(x_forward,-CI_99[:,idp_num]+yhat_forward[:,idp_num], linewidth=1,linestyle='--',c='k')

    ax.scatter(x,y[idp_name],c='r', label=idp_name)
    plt.legend(loc='upper right')
    plt.title('Normative trejectory')
    plt.savefig('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Tr/'+idp_name+'.png')
    #plt.show()
    #plt.close()