import random
class Island(object):
    def __init__(self,n,preyCnt=0,predatorCnt=0):
        #print n,preyCnt,predatorCnt
        self.gridSize=n
        self.grid=[]
        for i in range(n):
            row=[0]*n
            self.grid.append(row)
        self.initAnimal(preyCnt,predatorCnt)
    def __str__(self):
        s=""
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if self.grid[i][j]==0:
                    s+="."+"  "
                else:
                    s+=str(self.grid[i][j])+"  "
            s+="\n"
        return s
    def size(self):
        return self.gridSize
    def register(self,animal):
        x=animal.x
        y=animal.y
        self.grid[x][y]=animal
    def animal(self,x,y):
        if 0<=x<self.size()and 0<=y<self.size():
            return self.grid[x][y]
        else:
            return -1
    def initAnimal(self,preyCnt,predatorCnt):
        cnt=0
        while cnt<preyCnt:
            x=random.randint(0,self.size()-1)
            y=random.randint(0,self.size()-1)
            if self.animal(x,y)==0:
                newprey=Prey(island=self,x=x,y=y)
                self.register(newprey)
                cnt+=1
        cnt=0
        while cnt<predatorCnt:
            x=random.randint(0,self.size()-1)
            y=random.randint(0,self.size()-1)
            if self.animal(x,y)==0:
                newpredator=Predator(island=self,x=x,y=y)
                self.register(newpredator)
                cnt+=1
    def remove(self,animal):
        self.grid[animal.x][animal.y]=0
        
        
    
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
    def move(self):
        
##        offset=[(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
##        l=len(offset)
##        
##        while l>=0:
##            r=random.randint (0,len(offset)-1)
##            offset.append(offset[r])
##            offset.remove(offset[r])
##            l-=1
        #print offset
##        for i in range(len(offset)):
##            x=self.x+offset[i][0]
##            y=self.y+offset[i][1]
##            if self.island.animal(x,y)==0:
        location=self.checkGrid(int)
        if location:
            self.island.remove(self)
            self.x=location[0]
            self.y=location[1]
            self.island.register(self)
    def breed(self):
        if self.breedClock<=0:
            location=self.checkGrid(int)
            if location:
                self.breadClock=self.breedTime
                theClass=self.__class__
                newAnimal=theClass(self.island,x=location[0],y=location[1])
                self.island.register(newAnimal)
    def eat(self):
        location=self.checkGrid(Prey)
        if location:
            self.island.remove(self.island.animal(location[0],location[1]))
            self.island.remove(self)

            self.x=location[0]
            self.y=location[1]
            self.island.register(self)
            self.starveClock=self.starveTime
        
                
    def checkGrid(self,typeLookingFor=int):
        offset=[(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        result=0
        l=len(offset)
        
        while l>=0:
            r=random.randint (0,len(offset)-1)
            offset.append(offset[r])
            offset.remove(offset[r])
            l-=1
        for i in range(len(offset)):
            x=self.x+offset[i][0]
            y=self.y+offset[i][1]
            if not 0<=x<self.island.size() or\
               not 0<=y<self.island.size():
                continue
            if type(self.island.animal(x,y))==typeLookingFor:
                result=(x,y)
                break
        return result
            
class Prey(Animal):
    def __init__(self,island,x=0,y=0,s="O"):
        Animal.__init__(self,island,x,y,s)
        self.breedClock=self.breedTime
    def clockTick(self):
        self.breedClock-=1
class Predator(Animal):
    def __init__(self,island,x=0,y=0,s="X"):
        Animal.__init__(self,island,x,y,s)
        self.breedClock=self.breedTime
        self.starveClock=self.starveTime
    def clockTick(self):
        self.breedClock-=1
        self.starveClock-=1
        if self.starveClock<=0:
            self.island.remove(self)
    

def main(predBreed=6,predStarve=5,predInit=10,\
         preyBreed=3,preyInit=50,size=10,ticks=30):
    Predator.breedTime=predBreed
    Predator.starveTime=predStarve
    Prey.breedTime=preyBreed

    isle=Island(size,preyInit,predInit)
    
    for i in range (ticks):
        print isle
        animal_list=[]
        for x in range(size):
            for y in range(size):
                if isle.animal(x,y):
                    animal_list.append((x,y))
        for i in range(len(animal_list)):
            
            animal=isle.animal(animal_list[i][0],animal_list[i][1])
            if isinstance(animal,Predator):
                animal.eat()
                animal.move()
                animal.breed()
                animal.clockTick()
            
            
                
            




    
##    royale=Island(5,2,1)
##    timeSteps=20
##    islandSize=royale.size()
##    cnt=0
##    
##    while cnt<timeSteps:
##        print royale
##        animal_list=[]
##        for x in range(islandSize):
##            for y in range(islandSize):
##                if royale.animal(x,y):
##                    animal_list.append((x,y))
##                
##        for i in range(len(animal_list)):
##            animal=royale.animal(animal_list[i][0],animal_list[i][1])
##            animal.move()
##            #print "move"
##             
##        cnt+=1

main()
        
##royale=Island(10,3,4)
##moose1=Prey(royale,5,6,"m1")
##moose2=Prey(royale,4,7,"m2")
##print moose1
##print moose2
##royale.register (moose1)
##royale.register (moose2)
##print royale
##moose1.move()
##print royale
##moose2.move()
##print royale

