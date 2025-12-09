import numpy as np
import matplotlib.pyplot as plt
import random
import math

class laohuji:
    def __init__(self,k):
        self.k = k
        self.realprobability = np.random.random(k)
        self.max_index = np.argmax(self.realprobability)
        self.max_value = self.realprobability[self.max_index]
    def step(self,p):
        if np.random.random(1) < self.realprobability[p]:
            return 1
        else:
            return 0
        
class solve:
    def __init__(self,laohuji):
        self.laohuji = laohuji
        self.res = 0
        self.reslist = []
        self.n = 0
        self.nlist = np.ones(self.laohuji.k)  ##防止后面除的时候出来除0
        self.action = []

    def update(self,p,reward=None):
        self.res += self.laohuji.max_value - self.laohuji.realprobability[p]
        self.reslist.append(self.laohuji.max_value - self.laohuji.realprobability[p])
        self.n+=1
        self.nlist[p]+=1
        self.action.append(p) 
        
    def choose(self):
        raise NotImplementedError("忘记重写策略了bro")
    
class e_algorithm(solve):
    def __init__(self,laohuji,e):
        super().__init__(laohuji)
        self.laohuji = laohuji
        self.e = e
        self.scorelist = np.zeros(self.laohuji.k)
    
    def choose(self):
        if np.random.random(1)>self.e:
            tempchoose = np.argmax(self.scorelist/self.nlist)
            return tempchoose
        else:
            num = random.randint(0,self.laohuji.k-1)
            return num
        
    def update(self,p,tempres):
        super().update(p,tempres)
        self.scorelist[p] += tempres

class e_change_algorithm(solve):
    def __init__(self,laohuji):
        super().__init__(laohuji)
        self.laohuji = laohuji
        self.scorelist = np.zeros(self.laohuji.k)
    
    def choose(self):
        if np.random.random(1)>1/(self.n+1):
            tempchoose = np.argmax(self.scorelist/self.nlist)
            return tempchoose
        else:
            num = random.randint(0,self.laohuji.k-1)
            return num
        
    def update(self,p,tempres):
        super().update(p,tempres)
        self.scorelist[p] += tempres

class ucb(solve):
    def __init__(self,p,laohuji):
        super().__init__(laohuji)
        self.laohuji = laohuji
        self.p = p
        self.ulist = np.full(n,ma)

        

        

          
        