class Perceptron:
    def __init__(self,x1,x2,t,w1,w2,bias,a,theta):

        self.w1 = w1
        self.w2 = w2
        self.x1 = x1
        self.x2 = x2
        self.t = t
        self.b = bias
        self.alpha = a
        self.theta = theta

    def binary(self, z):
        if(z>=self.theta):
            return 1
        else:
            return 0

    def bipolar(self, z):
        if(z>=self.theta):
            return 1
        else:
            return -1

    def Calculate_weight(self,i):
        yin = 0
        yin = self.b + (self.x1[i]*self.w1 + self.x2[i]*self.w2 )
        return yin

    def updateWeights(self,i):

        self.w1 = self.w1 + ( self.alpha*self.x1[i]*self.t[i] )
        self.w2 = self.w2 + ( self.alpha*self.x2[i]*self.t[i] )
        self.b = self.b + ( self.alpha*self.t[i])
        return "Weight Updated as "+str(self.w1)+" , "+str(self.w2)+" , bias - "+str(self.b)
    
    def predict(self,test1,test2,fn):
        yin = self.b + ( test1*self.w1 + test2*self.w2)
        if(fn == "binary"):
            yout = self.binary(yin)
        else:
            yout = self.bipolar(yin)

        print("For given test data : "+str(test1)+" , "+str(test2)+" Predicted Result = "+str(yout))
        print("Weights are "+str(self.w1)+" , "+str(self.w2))

    # def train(self):

    #     yin = 0
    #     y = 0
    #     epoch = 0
    #     flag = [0]*len(self.x1)

    #     while 0 in flag:

    #         for i in range(0,len(self.x1)):
    #             yin = self.netInput(i)
    #             y = self.bipolar(yin)

    #             if(y != self.t[i]):
    #                print(self.updateWeights(i))
    #             else:
    #                 flag[i]=1

    #         epoch+=1
    #         print(str(epoch)+" Completed")

    #         if 0 not in flag:
    #             break
        
    #         flag = [0]*len(self.x1)

    #     print("Training Completed")

    def fit(self):

        yin = 0
        y = 0
        epoch = 0

        while True:
            crt = True
            for i in range(0,len(self.x1)):
                yin = self.Calculate_weight(i)
                y = self.bipolar(yin)

                if(y != self.t[i]) :
                   crt = False
                   print(self.updateWeights(i))

            epoch+=1
            print(str(epoch)+" Completed")

            if crt:
                break

        print("Training Completed")

x1 = [-1,-1,1,1]
x2 = [-1,1,-1,1]
t1 = [1,1,1,-1]
print("\n AND Gate:\n")
p1 = Perceptron(x1,x2,t1,0,0,0,1,0)

p1.fit()
p1.predict(-1,1,"bipolar")

print("\nOR Gate:\n")
t2 = [-1,1,1,1]
p2 = Perceptron(x1,x2,t2,0,0,0,1,0)
p2.fit()
p2.predict(-1,1,"bipolar")

print("\nAND NOT Gate:\n")
t3 = [1,-1,-1,-1]
p3 = Perceptron(x1,x2,t3,0,0,0,1,0)
p3.fit()
p3.predict(-1,1,"binary")