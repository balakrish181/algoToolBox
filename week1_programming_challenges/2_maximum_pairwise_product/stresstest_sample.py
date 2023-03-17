import random

def max_product_fast(data):
    #n = int(input())
    values = data.copy()
    n = len(values)
    #values = list(map(int,input().split()))
    max1,max2,index = 0,0,0
    for i in range(n):
        if values[i]>max1:
            max1 = values[i]
            index = i
    values.pop(index)

    for i in range(n-1):
        if values[i]>max2:
            max2 = values[i]      
    return max1*max2

def max_product_slow(values):
    #n = int(input())
    #values = list(map(int,input().split()))
    product = 0
    for i in range(len(values)):
        for j in range(len(values)):
            if i!=j:
                if values[i]*values[j]>product:
                    product = values[i]*values[j]

    return product


def stressTest(N,M):
    while True:
        set=[]
        n = random.randint(2,N)
        for i in range(n):
            set.append(random.randint(0,M))

        print('The set is {0}'.format(set))
        
        res1 = max_product_fast(set)
        res2 = max_product_slow(set)
        

        if res1 == res2:
            print('OK')

        else:
            print("wrong answer", res1 , res2, set)



if __name__=='__main__':
    stressTest(20,1000000)




