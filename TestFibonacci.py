from Fibonacci import Fibonacci
class TestFibonacci:
    obj=Fibonacci()
    st=obj.FibonacciSeries(8)
    print(st)
    #it has to raise error message
    st=obj.FibonacciSeries(-8)
    print(st)
    
