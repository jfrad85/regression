# title           :Regression.py
# description     :Multiple regression model
# author          :JF
# date            :23/10/2018
# usage           :checks how correlated inputs are to either ROCOF or Nadir
# notes           :
# python_version  :3.6.3
#==============================================================================

import math
import scipy
import pandas as pd
from scipy import stats
from pandas import ExcelWriter
from sklearn import linear_model

f_drop_std = []
std_dev_df = []
rocof_std = []

datapath = ('C:/Users/mchirjf3/Dropbox/ResponseOptions/Analysis/'
            'PythonTest.xlsx')
worksheet = 'Full_series'
mycols = 'B,C,D,E,F,G,H,I,J,K,L,M,N'
dfx = pd.read_excel(datapath,sheet_name=worksheet,usecols=mycols)

std_dev_df.append(dfx['x1'].std())
std_dev_df.append(dfx['x2'].std())
std_dev_df.append(dfx['x3'].std())
std_dev_df.append(dfx['x4'].std())
std_dev_df.append(dfx['x5'].std())
std_dev_df.append(dfx['x6'].std())
std_dev_df.append(dfx['x7'].std())
std_dev_df.append(dfx['x8'].std())
std_dev_df.append(dfx['x9'].std())
std_dev_df.append(dfx['x10'].std())
std_dev_df.append(dfx['f_drop'].std())
std_dev_df.append(dfx['ROCOF'].std())

# scipy version for single independent variable
##X1 = dfx['x1']
##X2 = dfx['x2']
##slope,intercept,R_value,p_value,std_err = scipy.stats.linregress(X1,Y)
##print ("scipy R^2 %f" %R_value**2)
##print ("scipy slope %.15f" %slope)

# sklearn F Drop
reg2 = linear_model.LinearRegression()
reg2.fit(dfx[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']],dfx.f_drop)

R_squared = reg2.score(dfx[['x1','x2','x3','x4',
                            'x5','x6','x7','x8','x9','x10']],dfx.f_drop)
R = math.sqrt(R_squared)

coes =((reg2.coef_))

##reg.predict([[x1 value for prediction,x2 value for prediction]]) 
intercept = reg2.intercept_

print("f drop \n R = %.4f \n R\xB2 = %.4f \n Intercept = %.4f \n"
       %(R,R_squared,intercept))

f_drop_std.append(coes[0] * (std_dev_df[0]/std_dev_df[10]))
f_drop_std.append(coes[1] * (std_dev_df[1]/std_dev_df[10]))
f_drop_std.append(coes[2] * (std_dev_df[2]/std_dev_df[10]))
f_drop_std.append(coes[3] * (std_dev_df[3]/std_dev_df[10]))
f_drop_std.append(coes[4] * (std_dev_df[4]/std_dev_df[10]))
f_drop_std.append(coes[5] * (std_dev_df[5]/std_dev_df[10]))
f_drop_std.append(coes[6] * (std_dev_df[6]/std_dev_df[10]))
f_drop_std.append(coes[7] * (std_dev_df[7]/std_dev_df[10]))
f_drop_std.append(coes[8] * (std_dev_df[8]/std_dev_df[10]))
f_drop_std.append(coes[9] * (std_dev_df[9]/std_dev_df[10]))

a = f_drop_std
data={'F Drop': [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]]}
frame = pd.DataFrame(data ,index = ['x1','x2','x3','x4',
                                    'x5','x6','x7','x8','x9','x10'])
# sklearn ROCOF
reg2 = linear_model.LinearRegression()
reg2.fit(dfx[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']],dfx.ROCOF)

R_squared1 = reg2.score(dfx[['x1','x2','x3','x4',
                             'x5','x6','x7','x8','x9','x10']],dfx.ROCOF)
R1 = math.sqrt(R_squared1)
coes =((reg2.coef_))
intercept = reg2.intercept_

print('ROCOF \n R = %.4f \n R\xB2 = %.4f \n Intercept = %.4f \n'
       %(R1,R_squared1,intercept))

rocof_std.append(coes[0] * (std_dev_df[0]/std_dev_df[11]))
rocof_std.append(coes[1] * (std_dev_df[1]/std_dev_df[11]))
rocof_std.append(coes[2] * (std_dev_df[2]/std_dev_df[11]))
rocof_std.append(coes[3] * (std_dev_df[3]/std_dev_df[11]))
rocof_std.append(coes[4] * (std_dev_df[4]/std_dev_df[11]))
rocof_std.append(coes[5] * (std_dev_df[5]/std_dev_df[11]))
rocof_std.append(coes[6] * (std_dev_df[6]/std_dev_df[11]))
rocof_std.append(coes[7] * (std_dev_df[7]/std_dev_df[11]))
rocof_std.append(coes[8] * (std_dev_df[8]/std_dev_df[11]))
rocof_std.append(coes[9] * (std_dev_df[9]/std_dev_df[11]))

b = rocof_std
c = std_dev_df

frame.loc[:,'ROCOF'] = [b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9]]
frame.loc[:,'STD'] = [c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9]]
print (frame)



