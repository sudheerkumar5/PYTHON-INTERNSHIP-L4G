def factorslist(x):
     factors = []
    for i in range(1,x+1):
        if(x % i == 0):
            factors.append(i)
    return factors

def Isprime(x):
    if x > 1:
        for i in range(2,x):
            if(x % i == 0):
                print("Not prime")
                break
        else:
            print("prime")
    else:
         print("Not prime")
            
def factorialnum(n):
    factorial=1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

def averageoffactorial(N):
    s = 0
    for j in range(1,N+1):
        k = factorialnum(j)
        s = s + k
    average = s / N
    print(average)