def fibonacci(m, n):
    a,b=0,1

    if n<=0:
            return 0
    else: 
        a,b=0,1
        for i in range(2,n+1):
            a,b = b, (a+b)%10 
        return b
    

if __name__ == '__main__':
    m,n map(int, input.split())
    print(fibonacci(m,n)
