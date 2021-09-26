import numpy as np
import pandas as pd
#I ran logistic regression initially, but the results were poor
#but this was the package I was using, for reference
#from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#set the plot font size
plt.rc("font", size=14)
import seaborn as sns
#set the seaborn descriptive analysis colors
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import os

#load the election data
#I modified the original data to ONLY include the two parties who ultimately ran in the general election
#and I edited the data to include whether the campaign was successful or not (won the presidential election)
def load_election_data():
    csv_path = os.path.join("mysite", "data.csv")
    return pd.read_csv(csv_path)

#import the data and give it a name
elections = load_election_data()

#process the elections data:
#Since there are too many different forms of each color, I am cleaning
#the data to reflect simply the presence of each color in the election
#campaign color palette with a 1 for true and a 0 for false
elections['whiteHex']=np.where(elections['whiteHex'] == '#ffffff',
                             1 , elections['whiteHex'])
elections['whiteHex']=np.where(elections['whiteHex'] != 1,
                             0, elections['whiteHex'])

elections['redHex']=np.where(elections['redHex'].isnull(),
                             0, elections['redHex'])
elections['redHex']=np.where(elections['redHex'] != 0,
                             1, elections['redHex'])

elections['blueHex']=np.where(elections['blueHex'].isnull(),
                             0, elections['blueHex'])
elections['blueHex']=np.where(elections['blueHex'] != 0,
                             1, elections['blueHex'])

elections['other1Hex']=np.where(elections['other1Hex'].isnull(),
                             0, elections['other1Hex'])
elections['other1Hex']=np.where(elections['other1Hex'] != 0,
                             1, elections['other1Hex'])

elections['presidencyWin']=np.where(elections['presidencyWin'] =='Y',
                             1, elections[ 'presidencyWin'])
elections['presidencyWin']=np.where(elections['presidencyWin'] =='N',
                             0, elections[ 'presidencyWin'])

elections['nominationnWin']=np.where(elections['nominationnWin'] =='Y',
                             1, elections[ 'nominationnWin'])
elections['nominationnWin']=np.where(elections['nominationnWin'] =='N',
                             0, elections[ 'nominationnWin'])

elections['RWB']=np.where(elections['RWB'] =='Y',
                             1, elections[ 'RWB'])
elections['RWB']=np.where(elections['RWB'] =='N',
                             0, elections[ 'RWB'])

elections['other2Hex']=np.where(elections['other2Hex'].isnull(),
                             0, elections['other2Hex'])
elections['other2Hex']=np.where(elections['other2Hex'] != 0,
                             1, elections['other2Hex'])

elections['other3Hex']=np.where(elections['other3Hex'].isnull(),
                             0, elections['other3Hex'])
elections['other3Hex']=np.where(elections['other3Hex'] != 0,
                             1, elections['other3Hex'])

#Set relevant data for testing - 'RWB', 'redHex', 'other1Hex', 'other2Hex'
indeVarsCols = ['RWB', 'redHex', 'other1Hex', 'other2Hex']
X = elections[indeVarsCols]
y = elections.presidencyWin

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.10,random_state=16) 
# because the sample size is so small, very small test size - 10% of set
#in my testing of the data, this produced the most reasonable outcomes
#in the confusional matrix
#although the sample size is so small that this is a very tenuous prediction at all

#Importing Bernoulli Naive Bayes
from sklearn.naive_bayes import BernoulliNB
bnb = BernoulliNB()
bnb.fit(X_train, y_train.astype(int))
y_pred = bnb.predict(X_test)
#print(y_train, X_train)

#this gives an output of a percentage of probability that the trained algorithm
#gives for campaign success given
#the chosen colors
def runprediction(rwb, red, other1, other2):
    results = bnb.predict_proba([[rwb, red, other1, other2]])[:,1]*100
    return results[0].astype(int)

#these were the tests I ran for sample output
#results1 = runprediction(1, 1, 0, 0)
#print("Your chosen colors have a ", results1, "percent chance of winning an election!")
