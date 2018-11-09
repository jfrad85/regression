# title           :Regression.py
# description     :Multiple regression model
# author          :JF
# date            :23/10/2018
# usage           :
# notes           :
# python_version  :3.6.3
#==============================================================================

import scipy
from sklearn import linear_model
from scipy import stats
import pandas as pd
from pandas import ExcelWriter
import math

f_drop_std = []
std_dev_df = []
rocof_std = []

path = ("C:/Users\mchirjf3/Dropbox/ResponseOptions/Analysis/PythonTest.xlsx")
mycols = "B,C,D,E,F,G,H,I,J,K,L,M,N"
dfx = pd.read_excel(path, sheet_name="Full_series",usecols=mycols)

std_dev_df.append(dfx["x1"].std())
std_dev_df.append(dfx["x2"].std())
std_dev_df.append(dfx["x3"].std())
std_dev_df.append(dfx["x4"].std())
std_dev_df.append(dfx["x5"].std())
std_dev_df.append(dfx["x6"].std())
std_dev_df.append(dfx["x7"].std())
std_dev_df.append(dfx["x8"].std())
std_dev_df.append(dfx["x9"].std())
std_dev_df.append(dfx["x10"].std())
std_dev_df.append(dfx["f_drop"].std())
std_dev_df.append(dfx["ROCOF"].std())

# scipy
#X1 = dfx ['x1']
#X2 = dfx ['x2']
#slope,intercept,R_value,p_value,std_err = scipy.stats.linregress(X1,Y)

#print ("scipy R^2 %f" %R_value**2)
#print ("scipy slope %.15f" %slope)

# sklearn F Drop
reg2 = linear_model.LinearRegression()
reg2.fit(dfx[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']],dfx.f_drop)

R_squared = reg2.score(dfx[['x1','x2','x3','x4',
                            'x5','x6','x7','x8','x9','x10']],dfx.f_drop)
R = math.sqrt(R_squared)

coes =((reg2.coef_))
b1 = coes[0]
b2 = coes[1]
b3 = coes [2]
b4 = coes [3]
b5 = coes [4]
b6 = coes [5]
b7 = coes [6]
b8 = coes [7]
b9 = coes [8]
b10 = coes [9]
##reg.predict([[x1 value for prediction,x2v value for prediction]]) 
b0 = reg2.intercept_

print("f drop \n R = %.4f \n R\xB2 = %.4f \n Intercept = %.4f \n"
       %(R,R_squared,b0))

##print('f Drop y = %f \n + %.9f(X1) \n+ %.9f(X2)\n + %.9f(X3)\n+ %.9f(X4) \n') , \
    #'+ %.9f(X5) \n+ %.9f(X6)\n+ %.9f(X7)\n+ %.9f(X8) \n+ %.9f(X9)\n + %.9f(X10)' \
    #%(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10)

f_drop_std.append(b1 *(std_dev_df[0]/std_dev_df[10]))
f_drop_std.append(b2 *(std_dev_df[1]/std_dev_df[10]))
f_drop_std.append(b3 *(std_dev_df[2]/std_dev_df[10]))
f_drop_std.append(b4 *(std_dev_df[3]/std_dev_df[10]))
f_drop_std.append(b5 *(std_dev_df[4]/std_dev_df[10]))
f_drop_std.append(b6 *(std_dev_df[5]/std_dev_df[10]))
f_drop_std.append(b7 *(std_dev_df[6]/std_dev_df[10]))
f_drop_std.append(b8 *(std_dev_df[7]/std_dev_df[10]))
f_drop_std.append(b9 *(std_dev_df[8]/std_dev_df[10]))
f_drop_std.append(b10 *(std_dev_df[9]/std_dev_df[10]))

A = f_drop_std
##print (f_drop_std)
data={'F Drop': [A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9]]}
frame = pd.DataFrame(data ,index = ["x1","x2","x3","x4",
                                    "x5","x6","x7","x8","x9","x10"])

# sklearn ROCOF
reg2 = linear_model.LinearRegression()
reg2.fit(dfx[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']],dfx.ROCOF)

R_squared1 = reg2.score(dfx[['x1','x2','x3','x4',
                             'x5','x6','x7','x8','x9','x10']],dfx.ROCOF)
R1 = math.sqrt(R_squared1)
coes =((reg2.coef_))
b1 = coes[0]
b2 = coes[1]
b3 = coes [2]
b4 = coes [3]
b5 = coes [4]
b6 = coes [5]
b7 = coes [6]
b8 = coes [7]
b9 = coes [8]
b10 = coes [9]
#reg.predict([[x1 value for prediction,x2v value for prediction]]) #put variables in to enable prediction
b01 = reg2.intercept_
#print ("ROCOF intercept %f" %b0)
#print ("Full y = %f + %.9f(X1) + %.9f(X2) + %.9f(X3)+ %.9f(X4) + %.9f(X5) + %.9f(X6)+ %.9f(X7)+ %.9f(X8) + %.9f(X9) + %.9f(X10)\n \n" %(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10))
print("ROCOF \n R = %.4f \n R\xB2 = %.4f \n Intercept = %.4f \n"
       %(R1,R_squared1,b01))
#print ("f Drop y = %f \n + %.9f(X1) \n+ %.9f(X2)\n + %.9f(X3)\n+ %.9f(X4) \n+ %.9f(X5) \n+ %.9f(X6)\n+ %.9f(X7)\n+ %.9f(X8) \n+ %.9f(X9)\n + %.9f(X10)"
      # %(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10))

rocof_std.append(b1 *(std_dev_df[0]/std_dev_df[11]))
rocof_std.append(b2 *(std_dev_df[1]/std_dev_df[11]))
rocof_std.append(b3 *(std_dev_df[2]/std_dev_df[11]))
rocof_std.append(b4 *(std_dev_df[3]/std_dev_df[11]))
rocof_std.append(b5 *(std_dev_df[4]/std_dev_df[11]))
rocof_std.append(b6 *(std_dev_df[5]/std_dev_df[11]))
rocof_std.append(b7 *(std_dev_df[6]/std_dev_df[11]))
rocof_std.append(b8 *(std_dev_df[7]/std_dev_df[11]))
rocof_std.append(b9 *(std_dev_df[8]/std_dev_df[11]))
rocof_std.append(b10 *(std_dev_df[9]/std_dev_df[11]))

B = rocof_std
c = std_dev_df

frame.loc[:,'ROCOF'] = [B[0],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9]]
frame.loc[:,'STD'] = [c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9]]
print (frame)

# sklearn Adjustable

reg5 = linear_model.LinearRegression()
reg5.fit(dfx[['x1']],dfx.ROCOF)


R_squared1 = reg5.score(dfx[['x1']],dfx.ROCOF)
R1 = math.sqrt(R_squared1)
coes =((reg5.coef_))
bx = coes[0]
b01 = reg5.intercept_
print(" ----------------ROCOF \n R = %.4f \n R\xB2 = %.4f \n Intercept = %.4f \n"
       %(R1,R_squared1,b01))
rocof_stdx = (bx *(std_dev_df[0]/std_dev_df[11]))
print(rocof_stdx)


