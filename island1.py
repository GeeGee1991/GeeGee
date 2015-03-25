class Island(object):
    def __init__(self,n,preyCnt=0,predatorCnt=0):
        print n,preyCnt,predatorCnt
        self.gridSize=n
        self.grid=[]
        for i in range(n):
            row=[0]*n
            self.grid.append(row)
        self.initAnimal
    def __str__(self):
        s=""
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if self.grid[i][j]==0:
                    s+="."+" "
                else:
                    s+=str(self.grid[i][j])+" "
            s+="\n"
        return s
    def size(self):
        return self.gridSize
    def register(self,animal):
        x=animal.x
        y=animal.y
        self.grid[x,y]=animal
    
class Animal(object):
    def __init__(self,island,x=0,y=0,s="A"):
        self.island=island
        self.x=x
        self.y=y
        self.name=s
    def __str__(self):
        return self.name
    def position(self):
        return self.x,self.y
class Prey(Animal):
    def __init__(self,island,x=0,y=0,s="O"):
        Animal.__init__(self,island,x,y,s)
class Predator(Animal):
    def __init__(self,island,x=0,y=0,s="O"):
        Animal.__init__(self,island,x,y,s)
    

        
royale=Island(10)
print royale
