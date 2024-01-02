class Preceptron:
    def __init__(self,x1,x2,t,w1,w2,bias,theta,a):
        self.x1=x1
        self.x2=x2
        self.t=t
        self.w1=w1
        self.w2=w2
        self.theta=theta
        self.alpha=a
        self.b=bias

    def bipolar(self,value):
        if value>=self.theta:
            return 1
        else:
            return -1
        
    def binary(self,value):
        if value>=self.theta:
            return 1
        else:
            return -1
    
    def calc_weight(self,i):
        yin=0
        yin=self.b+(self.x1[i]*self.w1 + self.x2[i]*self.w2)
        return yin
    
    # def update_weight(self,i):
    #     self.w1=self.w1+(self.alpha * self.x1[i]*self.t[i])
    #     self.w2=self.w2+(self.alpha*self.x2[i]*self.t[i])
    #     self.b=self.b+(self.alpha*self.t[i])
    #     return print("updated weight w1:"+ str(self.w1)+ ", w2" +str(self.w2)+"," )
    
    def update_weight(self,i):

        self.w1 = self.w1 + ( self.alpha*self.x1[i]*self.t[i] )
        self.w2 = self.w2 + ( self.alpha*self.x2[i]*self.t[i] )
        self.b = self.b + ( self.alpha*self.t[i])
        return "Weight Updated as "+str(self.w1)+" , "+str(self.w2)+" , bias - "+str(self.b)

    
    def predict(self,test1,test2,fn):
        yin=self.b+(test1*self.w1+ test2 * self.w2)
        if(fn=="binary"):
            yout=self.binary(yin)
        else:
            yout=self.bipolar(yin)

        return print(" test 1:" +str(test1)+ "test2:" +str(test2)+ "predicted result :"+str(yout)+ "w1: "+str(self.w1)+ "w2:"+str(self.w2))
    
    # def fit(self):
    #     yin=0
    #     y=0
    #     epoch=0

    #     while True:
    #         crt = True
    #         for i in range (0, len(self.x1)):
    #             yin=self.calc_weight(i)
    #             y=self.bipolar(yin)
                
    #             if y!=self.t[i]:
    #                 crt= False
    #                 print(self.update_weight(i))
                
    #         epoch+=1
    #         print( " epoch :"+str(epoch)+ "-- completed" )

    #         if crt:
    #             break

    #     print("training completed")


    def fit(self):
        yin = 0
        y = 0
        epoch = 0

        while True:
            crt = True
            for i in range(len(self.x1)):
                yin = self.calc_weight(i)
                y = self.bipolar(yin)
                
                if y != self.t[i]:
                    crt = False
                    print(self.update_weight(i))

            epoch += 1
            print("Epoch: " + str(epoch) + " - Completed")

            if crt:
                break

        print("Training Completed")


print("AND GATE")
print()
x1=[-1,-1,1,1]
x2=[-1,1,-1,1]
t=[-1,1,1,1]
p1=Preceptron(x1,x2,t,0,0,1,0,0)
p1.fit()
p1.predict(-1,1,"bipolar")



