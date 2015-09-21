#just say hello to the git
#change in dev branch
#Creating a new branch is quick & simple.
from numpy import *
data=mat([[1800,200,120],
    [1700,120,170],
    [2500,150,110],
    [1600,220,130]])

def normalization(data):
    m=data.shape[0]
    data=data-zeros(data.shape)
    cmin=data.min(0)
    crange=data.max(0)-cmin
    normdata=(data-tile(cmin,(m,1)))/tile(crange,(m,1))
    return normdata

def cosSim(i=0,j=1,data=normalization(data)):
    x=array(data[i])
    y=array(data[j])
    inner=sum(x*y)
    sim=inner/(sum(x**2)**0.5*sum(y**2)**0.5)
    return sim
 
def EuDis(i,j,data=normalization(data)):
    x=array(data[i])
    y=array(data[j])
    dis=sum((x-y)**2)
    return dis


print EuDis(1,3)

