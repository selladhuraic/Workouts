class Fibonacci:
    #first two terms need to initialize
    firstValue = 0
    secondValue = 1
    #variable to intialize in loop
    count = 0
    #variable to get fibonacci series
    #nSeries = int(input("Enter How many fibonacci series required? "))
   
        
    def FibonacciSeries(self,nSeries):
        try: 
            #condition to check valid no.
            fiboResult=""
            fiboList=[]
            if nSeries <=0:
                raise Exception("Number should be positive integer")
                #print("Number should be positive integer")
            #if it is only one series, then return firstValue
            elif nSeries ==1:
                
                fiboList.append(self.firstValue)
            #display fibonacci series
            else:
               
                while self.count <nSeries:
                    fiboList.append(self.firstValue)
                    #print(self.firstValue)
                    sumValue=self.firstValue + self.secondValue
                    #assign next two values by swap
                    self.firstValue=self.secondValue
                    self.secondValue=sumValue
                    self.count +=1
            fiboResult = ','.join(map(str, fiboList))
            return fiboResult
        except Exception as error:
            print("Something went wrong:",error)

           
