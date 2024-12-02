from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as np
import pandas as pd



Data = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1128/StaResults/AllMDD_FirstEpisode.csv")


# all Regions feature
brainRegion = Data.columns.tolist()
del brainRegion[:2]

x_data = np.array(Data[brainRegion])

y_label = np.array(Data['FirstEpisode'])
# Initialize the Logistic Regression model
logreg = LogisticRegression()

# Initialize Stratified KFold cross-validator
strat_k_fold = StratifiedKFold(n_splits=10)

# Perform KFold cross-validation
scores = cross_val_score(logreg, x_data, y_label, scoring='accuracy', verbose=6,cv=strat_k_fold)
print(scores)
# Calculate the mean accuracy
mean_accuracy = scores.mean()
print(mean_accuracy)
