#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:08:45 2017

@author: Jorge Lazo
"""

import pivot_1 as pv
import numpy as np
import random 
import matplotlib.pyplot as plt
import os
import copy




t=1
k=1
tu=1
fa=1
nu=1

T=[]
Es=[]

E=[]
C=[]
Temp=[]
En=[]
Emins=[]
Structmins=[]
#define the name of the file

temp0=2
tmax=10000
times=50

structure='URULULULDDRDDLULUULUR'


sequence='PHPPHHHHHHHHHPHHHHHPPH'   ##-----------1      
#sequence='PHPPHHHHHHHHHPHHPHHPPH'  ##-----------2        #-11
#sequence='PHPPHHHHHHHHHPPHHHHPPH'  ##-----------3       #-11 
#sequence='PHPPHHHHHHHHHPPHPHHPPH'  ##-----------4       #-11     

#sequence='PHPPHHHPHHHHHPHHHHHPPH'  ##-----------5       #-11
#sequence='PHPPHHHPHHHHHPHHPHHPPH'  ##-----------6       #-11    
#sequence='PHPPHHHPHHHHHPPHHHHPPH'  ##-----------7       #-11
#sequence='PHPPHHHPHHHHHPPHPHHPPH'  ##-----------8       #-11

#sequence='PHPPHPHHHHHHHPHHHHHPPH'  ##-----------9       #-11
#sequence='PHPPHPHHHHHHHPHHPHHPPH'  ##-----------10      #-11
#sequence='PHPPHPHHHHHHHPPHHHHPPH'  ##-----------11      #-11
#sequence='PHPPHPHHHHHHHPPHPHHPPH'  ##-----------12      #-11

#sequence='PHPPHPHPHHHHHPHHHHHPPH'  ##-----------13      #-11
#sequence='PHPPHPHPHHHHHPHHPHHPPH'  ##-----------14      #-11
#sequence='PHPPHPHPHHHHHPPHHHHPPH'  ##-----------15      #-11
#sequence='PHPPHPHPHHHHHPPHPHHPPH'  ##-----------16      #-11

datafile_path =os.getcwd()
save_dir=datafile_path+'/'+str(temp0)+'_'+sequence+'_minim_guess'+str(tmax)
print(save_dir)

En=[]

for ii in range(0,times):
    
    En[:]=[]
    Temp[:]=[]
    chain =pv.HPChain()   
    minchain =pv.HPChain()
    chain1 =pv.HPChain()
    
    chain.sequence=sequence    
    minchain.sequence=sequence
    chain1.sequence=sequence
    
    chain.structure=structure    
    minchain.structure=structure
    chain1.structure=structure
    #print(chain.energy)
    E0=-chain.energy
    temp=temp0
    t=1    
    while t<tmax:
     
        new_chain=pv.propose_move(chain)  
        chain1.structure=new_chain[0]
        b=k/temp
        
        if -chain1.energy-E0<=0:
            chain.structure=new_chain[0]
            E0=-chain.energy
            tu=tu+1
        
        elif np.exp(-b*(-chain1.energy-E0))>=random.random():
    
            chain.structure=new_chain[0]
            fa=fa+1
            E0=-chain.energy
            
        else:
            nu=nu+1
            #print('false')
                
                
        
        #En.append(-chain.energy)
        En.append(-chain.energy)
        minima=min(En)
        
        if  minima>=-chain.energy:
            struct=chain.structure    
            
        T.append(t)
        
        ##------------------logarithmic---------
        temp=temp0/(np.log(t+np.exp(1)))**1        
        Temp.append(temp)            
        t=t+1
        #print(t)
        Ecopy=list(En)
        mincopi=copy.copy(minima)     
        minstruct=copy.copy(struct)
        
        
    Es.append(Ecopy)
    print(ii)
    minchain.structure=struct
    #print(minchain)
    #print(-minchain.energy)
    Emins.append(minima)
    Structmins.append(struct)
    #dat=np.column_stack((dat,En[]))   

    #print(chain)
    #print(-chain.energy)
    
    dat=np.column_stack((Temp,Es[0]))   

for jj in range(1,len(Es)):
        dat=np.column_stack((dat,Es[jj]))  
#save energies
np.savetxt(save_dir, dat , fmt='%.18g', delimiter=' ', newline=os.linesep)
#save min stuctures
dat2=np.column_stack((Emins,Structmins))
save_dir2=save_dir+'_structures'
np.savetxt(save_dir2, dat2 , fmt='%s', delimiter=' '+sequence+' ', newline=os.linesep)