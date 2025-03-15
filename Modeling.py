import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import special

m=int(input("Enter the no. of SubPackets \n"))
Eb=1.5+0.22174
No=1
Pb=1/2*special.erfc(np.sqrt(Eb/No))
Lpkt_Range=np.arange(10,101,1)
delay=[0]*len(Lpkt_Range)
for j in range(0,len(Lpkt_Range)):
    Lpkt=Lpkt_Range[j]
    pe=1-((1-Pb)**Lpkt)
    state_Visits=np.zeros(m,dtype=(int))
    c,it,i=0,0,0
    while(i<100000):
        c=0
        while(c!=m):
         it+=1
         state_Visits[c]+=1
         randomnumber=random.random()
         if(randomnumber>=pe):
          c+=1
        i+=1
        
    SSP=state_Visits/it  
    x=(1-pe)*SSP[m-1]  #Successful recieve of M SubPkts
    delay[j]=1/x
    print("Lpkt = "+str(Lpkt)+"       iter = "+str(it)+'\n')
    print("state_Visits = "+str(state_Visits)+'\n')
    print("Steady_State_Prop = "+str(SSP)+'\n') 
    print("Delay = "+str(delay[j])+'\n')
    print("==============================================================")

plt.figure()
plt.xlabel("Length of pkt")
plt.ylabel("Delay")
plt.plot(Lpkt_Range,delay)
