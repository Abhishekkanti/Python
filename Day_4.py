class Person:
    def __init__(self, initialAge):
        self.age= initialAge
        if(self.age<0):
            self.age=0
            print("Age is not valid, setting age to 0.")
            
    def yearPasses(self):
        self.age +=1
        #print(f"{self.age} done")
        
    def amIOld(self):
        if(self.age < 13):
            print("You are young.")
        elif(self.age >= 13 and self.age < 18):
            print("You are a teenager.")
        else:
            print("You are old.")
       

#obj = Person(10)
#obj.yearPasses()
#obj.check()


#t = int(input())
#for i in range(0, t):
#    age = int(input())         
#    p = Person(age)  
#    p.amIOld()
#    for j in range(0, 3):
#        p.yearPasses()       
#    p.amIOld()
#    print("")