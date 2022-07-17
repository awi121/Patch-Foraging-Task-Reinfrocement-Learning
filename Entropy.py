#!/usr/bin/env python
# coding: utf-8

# In[1]:


B1=[3, 2, 7, 5, 7, 5, 7, 3, 2, 5, 7, 3, 2, 5, 7, 3, 2]
from matplotlib import pyplot
import math
p3=0.25
p2=0.25
p7=0.25
p5=0.25
sum2=4
sum23=1
sum25=1
sum27=1
sum22=1
ent=[]
step=0
s=[]
for i in B1:
    step=step+1
    s.append(step)
    sum2=sum2+1
    if(i==3):
        sum23=sum23+1
        p3=sum23/sum2
    if(i==2):
        sum22=sum22+1
        p2=sum23/sum2
    if(i==5):
        sum25=sum25+1
        p5=sum25/sum2
    if(i==7):
        sum27=sum27+1
        p7=sum27/sum2
    Entropy=-p2*math.log(p2,2)-p3*math.log(p3,2)-p5*math.log(p5,2)-p7*math.log(p7,2)
    ent.append(Entropy)
pyplot.plot(s, ent, marker='.')
pyplot.title('Probability vs Information')
pyplot.xlabel('Probability')
pyplot.ylabel('Information')
pyplot.show()


# In[ ]:




