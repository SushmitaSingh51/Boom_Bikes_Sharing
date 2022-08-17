print("all data_processing code related Boom_Bikes_Sharing")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import pandas as pd
path = ''
dataset = pd.read_csv(path+'bike_sharing_data.csv')
import os
path = ''
##Data Preparation
df = pd.read_csv(r" ")
df.head()
df.info()
#From the given data we can see that instant is an index column so we drop it
df.drop(['instant'],axis=1,inplace=True)
df.head()
#We can see column dteday and yr month are having same data so we can drop dteday to avoid confusion

df.drop(['dteday'],axis=1,inplace=True)
df.head()
#we know that casual+registered=cnt and cnt is our target variable so we will not consider casual and registered
df.drop(['casual','registered'],axis=1,inplace=True)
df.head()
#From data we can see that: season,yr,mnth,holiday,weekday,workingday,weathersit all are categorical variables
#We will replace season,weekday and weathersit with appropriate values

df['season'].replace({1:"spring",2:'summer',3:'fall',4:"winter"},inplace=True)

df['mnth'].replace({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'},inplace=True)

df['weekday'].replace({1:'Mon',2:'Tue',3:'Wed',4:'Thurs',5:'Fri',6:'Sat',7:'Sun'},inplace=True)

df['weathersit'].replace({1:"Clear_Few Clouds",2:"Mist_cloudy",3:"Light_rain",4:'Heavy_Rain'},inplace=True)
df.head()
df.info()
##Visualising numerical variables
# Pairplot of numerical variables
sns.pairplot(df,vars=['temp','atemp','hum','windspeed','cnt'])
plt.show()
