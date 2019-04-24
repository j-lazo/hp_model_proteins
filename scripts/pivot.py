from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist, squareform



class Switcher(object):
    """
    a class to switch cases and calculate the hh contacts in each SAW sequence
    """
    
    def __init__(self,seq, xpos, ypos):

        self.seq = seq      # HP list which contains of  0=P & 1=H 
        self.xpos = xpos    # x_position of elements
        self.ypos = ypos    # y_position of elements
        self.n = len(seq)

        # any_in will be used to ckeck SAW (self-avoiding walk)
        self.any_in = lambda a, b: any(i in b for i in a)
        # calculating distance
        self.dist = lambda d : np.sqrt((d ** 2).sum(axis=1))

        
    def pivot(self):
        
        k = np.random.randint(1, self.n - 1) # random pivot point 

        # set the origin to (0,0) for chunk[k+1:]
        x_tmp = [a - self.xpos[k] for a in  self.xpos[k+1:]]
        y_tmp = [b - self.ypos[k] for b in  self.ypos[k+1:]]
        n_tmp = len(x_tmp)
         
        
        g = np.random.randint(0, 7) # random rotation cases
        method_name = 'case_' + str(g)
        method = getattr(self, method_name, lambda: "nothing")
        
        # transform the chunk[k+1:]
        x_rot,y_rot = method(x_tmp, y_tmp, n_tmp )
        


        # move back to the origin
        x_new = self.xpos[:k+1] + [a + self.xpos[k] for a in  x_rot]
        y_new = self.ypos[:k+1] + [b + self.ypos[k] for b in  y_rot]
        
        new_stat = list(zip(x_new, y_new))

             
        
        # check if the new state is a SAW      
        if self.any_in(new_stat[:k+1], new_stat[k+1:]):           
            print(new_stat, '  NOT SAW')
            # recursive pivot - until it is saw 
            # incase of keeping the old state comment the next line
            return self.pivot()   
        else:
            # if it is SAW calculate HH contacts
            print(new_stat, '  SAW')
            self.new_stat = new_stat
            return('HH contacts  ',self.hh_contact())
                    


    def hh_contact(self):
        #calculate HH contacts
        seq = np.array(self.seq)
        n_stat = np.array(self.new_stat)
        dist =  squareform( pdist(n_stat, metric='euclidean'))
        arr =np.triu (dist, 2)
        index = np.argwhere(arr==1)
        E = 0
        for c in index:
            if seq[c].all()==1:
                E+=1        
        return E

      
    
    @staticmethod
    def case_0( x, y, n):        #+90 rotation
        for i in range(n):
            tmp = x[i]
            x[i] = - y[i]
            y[i] = tmp
        return  x , y
    
    @staticmethod
    def case_1(x, y, n):        #-90 rotation
        for i in range(n):
            tmp = x[i]
            x[i] =  y[i]
            y[i] = -tmp 
        return x ,  y
    
    @staticmethod   
    def case_2(x, y, n):        #180 rotation
        for i in range(n):
            x[i] = - x[i]
            y[i] = - y[i]
        return  x , y
        
    @staticmethod    
    def case_3(x, y, n):        # mirror(1,0)
        for i in range(n):
            y[i] = - y[i]
        return  x , y

    @staticmethod    
    def case_4(x, y, n):        # mirror(0,1)
        for i in range(n):
            x[i] = - x[i]
        return   x ,  y

    @staticmethod
    def case_5(x, y, n):        # mirror(1,1)
        for i in range(n):
            tmp = x[i]
            x[i] =  y[i]
            y[i] =  tmp
        return   x ,  y
    
    @staticmethod        
    def case_6(x, y, n):        # mirror(1,-1)
        for i in range(n):
            tmp = x[i]
            x[i] = - y[i]
            y[i] = - tmp
        return   x ,  y
  
        

if __name__ == '__main__':
    seq = [0,1,1,1,1,0]#[1,0,0,1,1]  # vector holding the amino acid sequence (1 for H, and 0 for P)
    xpos = [0,1,1,2,2,3]#[0,1,1,1,2] # x positions for sequence
    ypos = [1,1,2,2,1,1]#[1,1,2,3,3] # y position for sequence 
    
    for i in range(1,100):
        s=Switcher(seq,xpos,ypos)
        print(s.seq,s.xpos,s.ypos)
        s.pivot()
        print('olakease')
        print(s.hh_contact())
        print(s.seq,s.xpos,s.ypos)
    #print(seq,xpos,ypos)
    #s.hh_contact()
    #print(s.seq,s.xpos,s.ypos)
    
    #s.pivot()    
    # TODO: Implement your metropolis algorithm
