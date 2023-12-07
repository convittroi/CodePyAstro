import numpy as np
from scipy import stats
def SRL(x,y):
    x=np.array(x)
    y=np.array(y)
    sx=x.std()
    sy=y.std()
    r,p = stats.pearsonr(x,y)
    b1=r*(sy/sx)
    b0= y.mean()-b1*x.mean()
    numerator= 0.;denominator=0.
    for i in range(len(x)):
        temp=b0 + b1*x[i]
        numerator +=(y[i]-temp)**2
        denominator +=(x[i]-x.mean())**2
    Sb=np.sqrt(numerator)/np.sqrt(denominator)
    Sb*=np.sqrt(1/(len(y)-2))
    t_score=b1/Sb
    return b0,b1,r,Sb,t_score



x=[500, 800, 1000, 1500, 2200]
y=[6000 ,15000, 20000, 30000, 39000]
b0,b1,r,Sb,t_score=SRL(x,y)
df = len(y) - 2
p_value = stats.t.sf(np.abs(t_score), df)*2
print("b0=",b0,"b1=",b1,"r=",r,"Sb=",Sb,"t_score=",t_score)